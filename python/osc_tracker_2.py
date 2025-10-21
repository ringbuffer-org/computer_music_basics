#!/usr/bin/env python3
import argparse, time
from collections import defaultdict

import cv2
import numpy as np
import mediapipe as mp
from pythonosc.udp_client import SimpleUDPClient

def parse_args():
    ap = argparse.ArgumentParser(description="Camera tracker (hands/head/body) -> OSC")
    ap.add_argument("--mode", choices=["hands","head","body"], default="hands",
                    help="Select tracker: hands | head | body")
    ap.add_argument("--camera", type=int, default=0, help="v4l2 device index")
    ap.add_argument("--width", type=int, default=1280)
    ap.add_argument("--height", type=int, default=720)
    ap.add_argument("--ip", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=9000)
    ap.add_argument("--flip", action="store_true", help="horizontal mirror")
    ap.add_argument("--draw", action="store_true", help="show preview window")
    ap.add_argument("--smooth", type=float, default=0.2, help="EMA smoothing [0..1], 0=off")
    ap.add_argument("--min_det", type=float, default=0.5, help="min detection confidence")
    ap.add_argument("--min_trk", type=float, default=0.5, help="min tracking confidence (hands)")
    return ap.parse_args()

def ema_update(state, key, vec, a):
    if a <= 0 or vec is None: return vec
    if key not in state:
        state[key] = np.array(vec, dtype=float)
    else:
        state[key] = a*np.array(vec, dtype=float) + (1.0-a)*state[key]
    return state[key].tolist()

def clamp01(x):
    return max(0.0, min(1.0, float(x)))

def draw_bbox(frame, norm_bbox, color=(0,255,0), label=None):
    h, w = frame.shape[:2]
    x,y,bw,bh = norm_bbox
    p1 = (int(x*w), int(y*h))
    p2 = (int((x+bw)*w), int((y+bh)*h))
    cv2.rectangle(frame, p1, p2, color, 2)
    if label:
        cv2.putText(frame, label, (p1[0], max(0,p1[1]-8)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

def main():
    args = parse_args()
    client = SimpleUDPClient(args.ip, args.port)
    filt_state = {}

    cap = cv2.VideoCapture(args.camera, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
    if not cap.isOpened():
        raise SystemExit(f"Could not open camera index {args.camera}")

    mp_hands = mp.solutions.hands
    mp_face = mp.solutions.face_detection
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    # Initialize model per mode
    if args.mode == "hands":
        model = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            model_complexity=1,
            min_detection_confidence=args.min_det,
            min_tracking_confidence=args.min_trk,
        )
    elif args.mode == "head":
        model = mp_face.FaceDetection(
            model_selection=0,  # close-range
            min_detection_confidence=args.min_det
        )
    else:  # body
        model = mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            enable_segmentation=False,
            smooth_landmarks=True,
            min_detection_confidence=args.min_det,
            min_tracking_confidence=args.min_trk
        )

    last_visible = defaultdict(lambda: 0)

    try:
        while True:
            ok, frame = cap.read()
            if not ok: break
            if args.flip:
                frame = cv2.flip(frame, 1)

            h, w = frame.shape[:2]
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            if args.mode == "hands":
                results = model.process(rgb)
                visible = {"left":0, "right":0}
                if results.multi_hand_landmarks:
                    for hand_lms, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                        label = handedness.classification[0].label.lower()  # "left"/"right"
                        xs = [lm.x for lm in hand_lms.landmark]
                        ys = [lm.y for lm in hand_lms.landmark]
                        cx, cy = float(np.mean(xs)), float(np.mean(ys))
                        idx = hand_lms.landmark[8]
                        ix, iy, iz = float(idx.x), float(idx.y), float(idx.z)
                        xmn, xmx = float(np.min(xs)), float(np.max(xs))
                        ymn, ymx = float(np.min(ys)), float(np.max(ys))
                        bw, bh = (xmx - xmn), (ymx - ymn)
                        # EMA
                        cx, cy = ema_update(filt_state, f"{label}_pos", [cx,cy], args.smooth)
                        ix, iy, iz = ema_update(filt_state, f"{label}_tip", [ix,iy,iz], args.smooth)
                        xmn, ymn, bw, bh = ema_update(filt_state, f"{label}_bbox", [xmn,ymn,bw,bh], args.smooth)
                        # OSC
                        client.send_message(f"/hand/{label}/visible", 1)
                        client.send_message(f"/hand/{label}/pos", [clamp01(cx), clamp01(cy)])
                        client.send_message(f"/hand/{label}/index_tip", [clamp01(ix), clamp01(iy), float(iz)])
                        client.send_message(f"/hand/{label}/bbox", [clamp01(xmn), clamp01(ymn), clamp01(bw), clamp01(bh)])
                        visible[label] = 1
                        if args.draw:
                            draw_bbox(frame, [xmn, ymn, bw, bh], (0,255,0), f"{label}")
                            cv2.circle(frame, (int(cx*w), int(cy*h)), 6, (0,255,0), -1)
                # visibility down edges
                for label in ["left","right"]:
                    if visible[label] == 0 and last_visible[label] != 0:
                        client.send_message(f"/hand/{label}/visible", 0)
                last_visible.update(visible)

            elif args.mode == "head":
                results = model.process(rgb)
                if results.detections:
                    det = results.detections[0]
                    rbb = det.location_data.relative_bounding_box
                    x, y, wrel, hrel = float(rbb.xmin), float(rbb.ymin), float(rbb.width), float(rbb.height)
                    cx, cy = x + wrel*0.5, y + hrel*0.5
                    area = wrel*hrel
                    # EMA
                    cx, cy = ema_update(filt_state, "head_pos", [cx,cy], args.smooth)
                    x, y, wrel, hrel = ema_update(filt_state, "head_bbox", [x,y,wrel,hrel], args.smooth)
                    area = ema_update(filt_state, "head_area", [area], args.smooth)[0]
                    # OSC
                    client.send_message("/head/visible", 1)
                    client.send_message("/head/pos", [clamp01(cx), clamp01(cy)])
                    client.send_message("/head/size", float(area))
                    client.send_message("/head/bbox", [clamp01(x), clamp01(y), clamp01(wrel), clamp01(hrel)])
                    if args.draw:
                        draw_bbox(frame, [x,y,wrel,hrel], (0,255,0), "head")
                        cv2.circle(frame, (int(cx*w), int(cy*h)), 6, (0,255,0), -1)
                else:
                    client.send_message("/head/visible", 0)

            else:  # args.mode == "body"
                results = model.process(rgb)
                vis = 0
                if results.pose_landmarks:
                    # collect visible landmarks (visibility is per-landmark in [0..1])
                    pts = []
                    for lm in results.pose_landmarks.landmark:
                        if lm.visibility is None or lm.visibility >= 0.5:
                            pts.append((float(lm.x), float(lm.y)))
                    if len(pts) >= 4:
                        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
                        xmn, xmx = float(np.clip(np.min(xs), 0, 1)), float(np.clip(np.max(xs), 0, 1))
                        ymn, ymx = float(np.clip(np.min(ys), 0, 1)), float(np.clip(np.max(ys), 0, 1))
                        bw, bh = (xmx - xmn), (ymx - ymn)
                        cx, cy = xmn + 0.5*bw, ymn + 0.5*bh
                        area = bw * bh  # normalized bbox area ∈ [0..1]
                        # EMA
                        cx, cy = ema_update(filt_state, "body_pos", [cx,cy], args.smooth)
                        xmn, ymn, bw, bh = ema_update(filt_state, "body_bbox", [xmn,ymn,bw,bh], args.smooth)
                        area = ema_update(filt_state, "body_area", [area], args.smooth)[0]
                        # OSC
                        client.send_message("/body/visible", 1)
                        client.send_message("/body/pos", [clamp01(cx), clamp01(cy)])
                        client.send_message("/body/size", float(max(0.0, min(1.0, area))))
                        client.send_message("/body/bbox", [clamp01(xmn), clamp01(ymn), clamp01(bw), clamp01(bh)])
                        vis = 1
                        if args.draw:
                            draw_bbox(frame, [xmn, ymn, bw, bh], (0,255,0), "body")
                            cv2.circle(frame, (int(cx*w), int(cy*h)), 6, (0,255,0), -1)
                if not vis:
                    client.send_message("/body/visible", 0)

            if args.draw:
                cv2.imshow("OSC Tracker", frame)
                if cv2.waitKey(1) & 0xFF in (27, ord('q')):
                    break

    finally:
        if args.draw:
            try: cv2.destroyAllWindows()
            except: pass
        cap.release()
        # best-effort close for mediapipe solutions
        try:
            model.close()
        except Exception:
            pass

if __name__ == "__main__":
    main()


.. title: Using MediaPipe with PD
.. slug: mediapipe-pd
.. date: 2025-10-19 10:00:00
.. tags:
.. category: basics:interactive
.. priority: 3
.. link:
.. description:
.. type: text



In this section we will use MediaPipe in Python to control PD patches. More specifically, the computer vision part will detect our hands and sends their positions to synthesis parameters:

.. figure:: /images/basics/cv2pd_signal_flow.png
    :width: 90%
    :figwidth: 100%
    :align: center
 
    *Signal flow for the CV -> sound synthesis exercise.*

Make sure you have completed the `Python and MediaPipe Setup <https://ringbuffer.org/computer_music_basics/Interactive/mediapipe-setup/>`_ before starting with this exercise.


----

Run Camera Tracking
===================

Download the `Python script <https://ringbuffer.org/files/python/cmb/osc_tracker_2.py>`_ and run it, after activating your virtual environment.
You can get information on the program's arguments by typing:


.. code-block:: bash

      $ python3 osc_tracker_2.py --help


The output lists all possible arguments:

.. code-block:: python

   Camera tracker (hands/head/body) -> OSC

   options:
   -h, --help            show this help message and exit
   --mode {hands,head,body}
                           Select tracker: hands,head,body
   --camera CAMERA       v4l2 device index
   --width WIDTH         default=1280
   --height HEIGHT       default=720
   --ip IP               default = 127.0.0.1
   --port PORT           default=9000
   --flip                horizontal mirror
   --draw                show preview window
   --smooth SMOOTH       EMA smoothing [0..1], 0=off
   --min_det MIN_DET     min detection confidence
   --min_trk MIN_TRK     min tracking confidence (hands)





For this excercise, we want to use hand-tracking, with additional parameters for smoothing the tracking results and drawing the markers:


.. code-block:: bash

      $ python osc_tracker_2.py --mode hands --flip --smooth 0.5 --draw


The program will open a window to visualize the tracking in real time:

.. figure:: /images/basics/hand.png
    :width: 70%
    :figwidth: 100%
    :align: center
 
    *Hand-tracking result from Python.*


With the default parameters for address and port, the program will send the tracking data to:

- **Address: 127.0.0.1**
- **Port: 9000**

Any program on that machine (localhost) opening this port can receive and process the information.

----


Run the PD Synth
================

Download the `PD patch <https://ringbuffer.org/files/cmb/pd/hand_synth.pd>`_ and launch it with Pure Data (install, if necessary: `Getting Started with PD <https://ringbuffer.org/computer_music_basics/Puredata/getting-started-with-puredata/>`_).


.. figure:: /images/basics/pd_hand_synth.png
    :width: 70%
    :figwidth: 100%
    :align: center
 
    *OSC-controlled Synth in PD.*

The patch consist of two main sections:

- 1: OSC receiver and router
   - opens a UDP port
   - extracts the right hand data
   - sends position data (X,Y) internally
- 2: Synth
   - reveives position data (X,Y)
   - uses parameters for sound synthesis



.. admonition:: Exercise I

	Extend the PD patch to make the left hand data accessible.

.. admonition:: Exercise II

	Extend the PD patch to create more interesting sounds.




s.boot;

// get script's directory for relative paths
~root_DIR = thisProcess.nowExecutingPath.dirname++"/";

~buffer  = Buffer.read(s,~root_DIR++"../audio/sala_formanten.wav");

(
~sampler = {

	|rate= 0.1|

	var out = LoopBuf.ar(1,~buffer.bufnum, BufRateScale.kr(~buffer.bufnum) * rate, 1, 0,0,~buffer.numFrames);

	Out.ar(0, out);

}.play;

)

~sampler.set(\rate,0.01);
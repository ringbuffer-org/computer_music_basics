s.boot;

(

// create white noise node with gain control
~test = {arg gain=1; WhiteNoise.ar(gain)}.play;

// try to set the gain
~test.set(\gain, 0.1);

)


(
Routine({

	// create white noise node with gain control
	~test = {arg gain=1; WhiteNoise.ar(gain)}.play;

	// wait for the server to finish all asynchronous tasks
	s.sync;

	// try to set the gain
	~test.set(\gain, 0.1);

}).play
)
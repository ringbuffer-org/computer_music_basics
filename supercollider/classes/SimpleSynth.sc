SimpleSynth {

	//var test_BUS;
	var dur;

	// constructor
	*new { | p |
		^super.new.init(p)
	}

	// initialize method
	init { | p |
		dur    = 1;
	}

	// a function for setting a member variable
	duration
	{
		|d|
		dur=d;
	}

	// a function for playing a synth
	play
	{ | f |
		{
		// this creates a synth with an envelope and frees it on finishing
		SinOsc.ar(f*[1.1,1.3,1.45,1.7], 0, 1) * EnvGen.kr(Env.linen(0.05, dur, 0.25), doneAction: Done.freeSelf);
		}.play;
	}

}





// boot the server
s.boot;


// Play a Synth
(
{
		// calculate a sine wave with frequency and amplitude
		var x = 100 * SinOsc.ar(1000);

		// send the signal to the output bus '0'
		Out.ar(0, x);

}.play;

)

// free all nodes from the server
s.freeAll

// define a SynthDef and send it to the server
(

SynthDef(\sine_example,
	{
		// define arguments of the SynthDef
		|f = 100, a = 1|

		// calculate a sine wave with frequency and amplitude
		var x = a * SinOsc.ar(f);

		// send the signal to the output bus '0'
		Out.ar(0, x);

}).send(s);

)



// create a synth from the SynthDef
~my_synth = Synth(\sine_example, [\f, 1000, \a, 1]);

// create another synth from the SynthDef
~another_synth = Synth(\sine_example, [\f, 1100, \a, 1]);

// set a parameter
~my_synth.set(\f,900);

// free the nodes
~my_synth.free();
~another_synth.free();
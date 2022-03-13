s.boot;

// define simple arrays:
a = [0,1,2,3];
b = [0,1,2,"last_value"];

// access indices:
a[3];

// an array with 4 values:
c = Array.fill(4,{arg i; 10/(i+1) });


/////////////// BUSES


// an array of 16 buses, each with 4 channels:
~busArray = Array.fill(16,{Bus.control(s, 4)})

// scope the second bus in the array:
~busArray[1].scope

// set the third bus of the second bus in the array:
~busArray[1].setAt(2,0.5);


/////////////// Array of Nodes/UGens

// an array of 16 sine oscillators:
~busArray = Array.fill(16,{arg i;{SinOsc.ar(200*(i+1),0,0.2)}.play})


/////////////// Array of Synths

// a simple synthdef
(
SynthDef(\sine,
{|f = 100, a = 1|

   Out.ar(0, a * SinOsc.ar(f));

}).send(s);
)

~busArray = Array.fill(16,{arg i;Synth.new(\sine,[f:200*(i+1),a:0.2])})


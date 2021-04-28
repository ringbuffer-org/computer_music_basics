s.boot;

~aBus = Bus.audio(s,1);

~osc = {arg out=1; Out.ar(out,Saw.ar())}.play;

~osc.set(\out,~aBus.index);

// ~aBus.scope

~lpf = {arg in=0; Out.ar(0, LPF.ar(In.ar(in),100))}.play;

~lpf.set(\in,~aBus.index);

~lpf.moveAfter(~osc)



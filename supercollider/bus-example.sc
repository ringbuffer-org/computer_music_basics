s.boot;

~osc  = {arg freq=100; Out.ar(0,Saw.ar(freq))}.play;

~cBus = Bus.control(s,1);

~osc.map(\freq,~cBus.index);

~cBus.set(50);


  ~mBus = Bus.control(s,8);

  ~mBus.scope;

  ~osc.map(\freq,~mBus.index+3);

  ~mBus.setAt(0,150);
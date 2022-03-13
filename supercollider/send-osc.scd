s.boot;

(
~out_address  = NetAddr("127.0.0.1", 6666);
~cBus         = Bus.control(s,1);
)

(
~osc_routine = Routine({

	inf.do({

		// read value from bus
		var value      = ~cBus.getSynchronous(~nVbap);

		// send value
		~out_address.sendMsg('/oscillator/frequency', value);

		// wait
		0.05.wait;

	});
});
)

~osc_routine.play();

~cBus.set(300);

~cBus.set(700);

~osc_routine.stop();


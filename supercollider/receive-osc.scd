	~osc_receive = OSCFunc(

		{ arg msg, time, addr, recvPort;

		post('Revceived message to path: ');
		msg[0].postln;

		post('With value: ');
		msg[1].postln;

	}, '/test/message');



  OSCdef(\tester,
		{|msg, time, addr, recvPort|

		post('Revceived message to path: ');
		msg[0].postln;

		post('With value: ');
		msg[1].postln;

	},'/test/another', n);

 
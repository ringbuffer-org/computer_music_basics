.. title: Receiving OSC in SuperCollider
.. slug: receiving-osc-in-supercollider
.. date: 2021-04-10 10:40:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 7
.. link:
.. description:
.. type: text


By default, a running instance of sclang listens to incoming OSC messsages on the port **57120**.

OSCFunc
-------


For listening to a specific OSC message, an OSC function can be defined
with the matching path:

.. code-block:: supercollider

	~osc_receive = OSCFunc(

		{ arg msg, time, addr, recvPort;

       postln('Revceived message: '+msg[0].string' - '+msg[1].string);

	}, '/test/message');

----

OSCdef
------

OSCdef is slightly more flexible and allows to change definitions
on the fly, without deleting nodes:

.. code-block:: supercollider

  OSCdef(\tester,
		{|msg, time, addr, recvPort|
			var val;
			val = msg[1];
			val.postln;
	},'/test/another', n);

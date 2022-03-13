.. title: Receiving OSC in SuperCollider
.. slug: receiving-osc-in-supercollider
.. date: 2021-04-10 10:40:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 7
.. link:
.. description:
.. type: text




OSCFunc
-------

By default, a running instance of sclang listens to incoming OSC messsages on the port **57120**. For listening to a specific OSC message, an OSC function can be defined
with a specific path. SC will then evaluate the defined function when OSC messages are
received at the default port with the matching path:

.. code-block:: supercollider

		~osc_receive = OSCFunc(

		{ arg msg, time, addr, recvPort;

		post('Revceived message to path: ');
		msg[0].postln;

		post('With value: ');
		msg[1].postln;

		}, '/test/message');


----

OSCdef
------

OSCdef is slightly more flexible and allows to change definitions
on the fly, without deleting nodes:

.. code-block:: supercollider

		OSCdef(\tester,
			{|msg, time, addr, recvPort|

			post('Revceived message to path: ');
			msg[0].postln;

			post('With value: ');
			msg[1].postln;

		},'/test/another', n);



------

Exercises
=========

.. admonition:: Exercise I

		Use a SuperCollider OSC receiver with the first `PD example on sending OSC </Puredata/using-osc-in-pure-data/>`_ for sending OSC to change the value of control rate bus and monitor the bus with a scope. The `section on buses <SuperCollider/using-buses-in-supercollider/>`_ is helpful for this. Keep in mind to set the correct port (**57120**) and path in the PD patch.

.. admonition:: Exercise II

		Use a SuperCollider OSC receiver with the `PD example </Puredata/using-osc-in-pure-data/>`_ for controlling the subtractive synth in the `previous example </SuperCollider/combining-nodes-in-supercollider/>`_. This can be done with control rate buses or by a direct	``set()`` to the synth nodes.

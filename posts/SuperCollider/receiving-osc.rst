.. title: Receiving OSC in SuperCollider
.. slug: receiving-osc-in-supercollider
.. date: 2021-04-10 10:40:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 10
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


Exercise
========

.. admonition:: Send-received

	Use the example from the `Section on sending OSC </computer_music_basics/SuperCollider/sending-osc-from-supercollider/>`_ to send a message to the OSCFunc.



------


OSCdef
------

OSCdef is more flexible and allows to change definitions
on the fly, without deleting nodes (the OSCdef identifier does not have to match the OSC path - but it does in this example):

.. code-block:: supercollider

		OSCdef(\poster,

			{|msg, time, addr, recvPort|

			post('With value: ');
			msg[1].postln;

		},'/poster', n);





------

Exercises
=========

.. admonition:: Group Exercise I

	Send messages to specific peers. To do this, you need their IP address. Their OSC receiver path has to match the path your sender uses.


.. admonition:: Group Exercise II

	Use the SynthDef from the `Section on envelopes </computer_music_basics/SuperCollider/using-envelopes-in-supercollider/>`_ inside an OSCdef to let your peers trigger sounds on your SC server.



------

Opening Specific UDP Ports
--------------------------

For many applications it can be helpul to open a specific port for a puropse. Sometimes the server booting process can be interrupted by messages being sent to ''57120'' before booting is competed. An additional port can be opened like this:

.. code-block:: supercollider

	thisProcess.openUDPPort(6666);


A list of all open ports can be queried from the language:

.. code-block:: supercollider

	thisProcess.openPorts


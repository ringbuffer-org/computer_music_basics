.. title: Sending OSC from SuperCollider
.. slug: sending-osc-from-supercollider
.. date: 2021-04-10 10:40:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 8
.. link:
.. description:
.. type: text





For sending OSC from SuperCollider, a ``NetAddr`` object needs to be generated.
It needs an IP address and a port:

.. code-block:: supercollider

    ~out_address  = NetAddr("127.0.0.1", 6666);


-----

Sending Values Once
-------------------

This first example sends an OSC message once when the following line is evaluated.
The previously created NetAddr object can be used to send OSC messages with its ``sendMsg`` method:

.. code-block:: supercollider

    ~out_address.sendMsg('/test/message', 1);


----


Sending Values Continuously
---------------------------

Based on the previous example, a routine can be created which
continuously reads values from control rate buses to send
their instantaneous value via OSC.
The ``osc_routine`` runs an infinite loop with a short
wait interval to limit the send rate and the CPU load:

.. code-block:: supercollider

    ~cBus = Bus.control(s,1);

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


-----

Once created, the routine can be started and stopped with the
methods ``play()`` and ``stop()``. While running, bus values
can be changed to test the functionality:

.. code-block:: supercollider

    ~osc_routine.play();

    ~cBus.set(300);

    ~cBus.set(700);

    ~osc_routine.stop();


Exercise
--------

.. admonition:: Exercise

		Run the PD patch ``osc-receive.pd`` to receive values from SuperCollider via OSC and control the pitch.

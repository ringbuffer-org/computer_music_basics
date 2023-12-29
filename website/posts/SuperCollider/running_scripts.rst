.. title: Running Scripts from the Command Line
.. slug: supercollider-command-line
.. date: 2023-05-08 10:00:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 15
.. link:
.. description:
.. type: text

Executing Complete Scripts
--------------------------

All above examples were used in a live-coding scenario. The commands were executed in blocks or single lines, step after step.
For running a complete script, routines can help to keep the server synchronized.
In addition, the server needs to be booted before any server-side operations take place.
This can be done with different methods.

----

Wait for Boot
=============

``Server.waitForBoot`` boots a server and, when completed, runs the function passed to it as an argument:

 .. code-block:: supercollider

     s.waitForBoot({

     	// a sine oscillator node with one parameter
     	var x = {|freq=1000| Out.ar(0, SinOsc.ar(freq))}.play;

     });

----

Do when Booted
==============

``Server.doWhenBooted`` need the server to be started with an extra command:

.. code-block:: supercollider

    s.doWhenBooted({

    	// a sine oscillator node with one parameter
    	var x = {|freq=1000| Out.ar(0, SinOsc.ar(freq))}.play;

    });

    s.boot;


-----

Calling sclang from the Terminal
--------------------------------

Once a script is executable as a whole, it can be started using sclang in the command line.
When the above file is stored as ``sine_example.scd``, it can be started without launching the scide or
any other environment :

.. code-block:: bash

  $ sclang sine_example.scd

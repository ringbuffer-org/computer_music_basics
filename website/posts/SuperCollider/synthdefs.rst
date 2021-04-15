.. title: SynthDefs
.. slug: synthdefs
.. date: 2020-11-05 13:47:06 UTC
.. tags:
.. category: basics:supercollider
.. priority: 5
.. link:
.. description:
.. type: text


SynthDefs
---------

SynthDefs are templates for Synths, which are
sent to a server:

.. code-block:: supercollider

 // define a SynthDef and send it to the server
 (

 SynthDef(\sine_example,
 {
    // define arguments of the SynthDef
    |f = 100, a = 1|

    // calculate a sine wave with frequency and amplitude
    var x = a * SinOsc.ar(f);

    // send the signal to the output bus '0'
    Out.ar(0, x);

 }).send(s);

 )


Once a SynthDef has been sent to the server,
instances can be created:

.. code-block:: supercollider

    // create a synth from the SynthDef
    ~my_synth = Synth(\sine_example, [\f, 1000, \a, 1]);

    // create another synth from the SynthDef
    ~another_synth = Synth(\sine_example, [\f, 1100, \a, 1]);


Parameters of running synths can be changed,
using the associated variable on the client side:

.. code-block:: supercollider

    // set a parameter
    ~my_synth.set(\f,900);


Running synths with a client-side
variable can be removed from the server:

.. code-block:: supercollider

    // free the nodes
    ~my_synth.free();
    ~another_synth.free();

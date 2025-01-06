.. title: Using Envelopes
.. slug: using-envelopes-in-supercollider
.. date: 2021-05-02 10:40:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 7
.. link:
.. description:
.. type: text


The body of a basic electronic kick drum is a sine wave with an
exponential decrease in frequency over time. Depending on the
taste, this drop happens from about 200-300 Hz
to 30-60 Hz. This can be achieved with temporal envelopes.

Define Envelopes
================

Before using an envelope, it needs to be defined,
using the ``Env`` class. It is feature rich and well
documented insice the SC help files.
The following line creates an exponential envelope with
a single segment, defining an exponential drop.
It can be plotted using the envelope's ``plot`` method:

.. code-block:: supercollider

    ~env = Env([1, 0.1], [0.15], \exp);
    ~env.plot;


-----

.. figure:: /images/basics/sc-envelope.png
  :figwidth: 100%
  :width: 40%
  :align: center



---


Using an Envelope Generator
===========================

Envelopes can be passed to envelope generators.
The following example generates a control rate signal
with the exponential characteristics.
It will be sent to the control bus with the index 0 (``Out.kr(0,)``)
and the created node will be freed once the envelope is done,
defined by the done action.
The bus can be monitored to see the result:


.. code-block:: cpp

    s.scope(1,0,rate:'control')

    {Out.kr(0,EnvGen.kr(~env, doneAction: Done.freeSelf))}.play


-----

A "Kick" SynthDef
=================

The following SynthDef uses the envelope inside the node. No bus is needed for
The synth has two arguments - the gain and the pitch:


.. code-block:: supercollider


    (
    SynthDef(\kick,
    {
        |gain=1,pitch=100|

        var env = EnvGen.kr(~env, doneAction: Done.freeSelf);

        // send the signal to the output bus '0'
        Out.ar(0, gain*SinOsc.ar(env*pitch));
    };
    ).send(s)
    )



-----

Triggering it
=============


The SynthDef can now be used to create a node on the server. It receives two arguments for gain and pitch:



.. code-block:: supercollider

    Synth(\kick, [1,300])


Once the envelope is finished, the '''Done.freeSelf''' will remove the whole node from the server. When multiple envelopes are used within a node, the first one to finish will free the node, if set to '''doneAction: Done.freeSelf'''. Other doneActions can help prevent this ('''Done.none''').


-----

Exercise
========

.. admonition:: Exercise

    Add a second envelope for the gain to the SynthDef to create a kick without clicks.




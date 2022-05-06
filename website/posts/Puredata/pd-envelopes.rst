.. title: Envelopes in PD
.. slug: pd-envelopes
.. date: 2021-04-30 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 4
.. link:
.. description:
.. type: text


Temporal envelopes are an essential building block of sound synthesis algorithms.
They are introduced in the Control Section of the CMB content:

- http://ringbuffer.org/computer_music_basics/Control/envelopes-adsr/
- http://ringbuffer.org/computer_music_basics/Control/envelopes-exponential/


ADSR in PD
==========

The ADSR envelope is the most widely used temporal envelope.
The PD help files contain an example, which can serve as a starting point
for an ADSR object. It can also be downloaded here: `ADSR <https://raw.githubusercontent.com/anwaldt/computer-music-basics/main/puredata/adsr.pd>`_

.. admonition:: Task

		Open the example or download the patch and store the object in your working directory.

-----

Once stored, the object can be used in custom patches to control
arbitrary parameters. The following example controls the gain of a
sine wave oscillator with an ADSR envelope.
The ``adsr`` object has six inlets:

- 1: the trigger
- 2: the peak value
- 3: the attack time (ms)
- 4: the decay time (ms)
- 5: the sustain amount (0...100%)
- 6: the release time (ms)

The delay object emulates a ``555 ms`` key press. The only outlet is an
audio rate signal with the envelope:

.. figure:: /images/basics/pd-adsr.png
    :width: 800px
    :figwidth: 100%
    :align: center

.. admonition:: Exercise

		Add a second ADSR with individual parameters to control the pitch of the tone.

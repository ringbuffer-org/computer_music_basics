.. title: Envelopes in PD
.. slug: pd-envelopes
.. date: 2021-04-30 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 6
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
for an ADSR object.

.. admonition:: Task

		Open the example and store the object in your working directory.

-----

Once stored, the object can be used in custom patches to control
arbitrary parameters. The following example controls the gain of a
sine wave oscillator with an ADSR envelope.
The delay object emulates a ``555 ms`` key press.

.. figure:: /images/basics/pd-adsr.png
    :width: 800px
    :figwidth: 100%
    :align: center

.. admonition:: Exercise

		Add a second ADSR with individual parameters to control the pitch of the tone.

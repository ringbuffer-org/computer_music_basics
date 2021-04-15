.. title: Sampling & Aliasing with Overtones
.. slug: sampling-and-aliasing-with-overtones
.. date: 2020-04-28 16:16:05 UTC
.. tags:
.. category: basics:introduction
.. link:
.. description:
.. has_math: true
.. type: text
.. priority: 4






Aliasing for Signals with Overtones
===================================

For signals with overtones, undersampling cal lead to inharmonic aliases
long before  the fundamental itself exceeds the Nyquist frequency.
For a harmonic signal with a fundamental frequency :math:`f_0`, the alias
frequencies for all :math:`N` harmonics can be calculated:

:math:`f_m = \sum\limits_{n=1}^{N} \Big| n f_0 - f_s \Big\lfloor \frac{n f_0}{f_s} \Big\rfloor \Big|`

-----

Interactive Example
-------------------

For the following example, a sawtooth with 20 partials is used without band limitation.
At a pitch of about :math:`2000 Hz`, the aliases become audible.
For certain fundamental frequencies, all aliases will be located at
actual multiples of the fundamental, resulting in a correct synthesis
despite aliasing.
In most cases, the mirrored partials are inharmonic and distort the signal.

.. raw:: html
   :file: /media/anwaldt/ANWALDT_2TB/WORK/TEACHING/Computer_Music_Basics/webaudio/aliasing-square.html

-----


Anti-Aliasing Filters
=====================

In analog-to-digital conversion, simple anti-aliasing filters can be
used to band-limit the input and discard signal components above the
Nyquist frequency. In case of digital synthesis, however, this principle
can not be applied. When generating a square wave signal with an
infinite number of harmonics, aliasing happens instantaneously and can
not be removed, afterwards.




Band Limited Generators
=======================

In order to avoid the aliasing, band-limited signal generators are provided in most audio programming languages and environments.

.. title: Sampling & Aliasing
.. slug: sampling-and-aliasing
.. date: 2020-04-28 16:16:05 UTC
.. tags:
.. category: basics:introduction
.. link:
.. description:
.. has_math: true
.. type: text
.. priority: 3


Sampling
========

Impulse Train
-------------

The representation of signals through equidistant, quantized values is
the fundamental principle of digital sound processing and has an
influence on several aspects of sound synthesis. Mathematically, a
continuous signal :math:`x(t)` is sampled by a multiplication with an
impulse train :math:`\delta_T(t)` (also referred to as Dirac comb) of
infitite length:

:math:`x[n] = x(t) \delta_T (t) = \sum\limits_{n=-\infty}^{\infty} x(n T) \delta (t-nT)`

This impulse train can be expressed as a Fourier series:

:math:`\delta_T = \frac{1}{T} \left[1 +2 \cos(\omega_s t) 2 \cos(2 \omega_s t) + \cdots \right]`,
with :math:`\omega_s=\frac{2\pi}{T}`

:math:`\delta_T = \frac{1}{T} + \sum \left( \frac{2}{T} \cos(n \omega_s t) \right)`

Fourier Transform of the Impulse Train
--------------------------------------

The Fourier transform of a time-domain impulse train is a
frequency-domain impulse train:

:math:`\mathfrak{F}(\delta_T) = \mathfrak{F}(\sum C_k e^{j k \omega_0 t})`

:math:`\mathfrak{F}(\delta_T) = \sum\limits_{m = -\infty}^{\infty} \delta(T f)`

Fourier Transform of the Sampled Signal
---------------------------------------

The Fourier transform of the sampled signal is periodic:

:math:`X[i] = \frac{1}{T} + \sum\limits_{n=-\infty}^{\infty} X(\omega -n \omega_s)`

Aliasing
========

Since the spectrum of a sampled signal is periodic, it must be
band-limited, in order to avoid misinterpretations, known as aliasing.
Since the spectrum is periodic with :math:`\omega_s`, the maximum
frequency which can be represented - the Nyquist frequency - is:

:math:`f_N = \frac{f_s}{2}`

As soon as components of a digitally sampled signal exceed this
boundary, aliases occur. The following example can be used to set the
frequency of a sine wave beyond the Nyquist frequency, resulting in
aliasing and ambiguity, visualized in the time domain. The static
version of the following example shows the time-domain signal of a
:math:`900 \ \mathrm{Hz}` sinusoid at a sampling rate
:math:`f_s = 1000 \ \mathrm{Hz}`:





Aliasing Frequency for a Sinusoid
=================================

For pure sinusoids, aliasing results in a sinusoid at the mirror- or
folding frequency :math:`f_m`:

:math:`f_m = \Big| f - f_s \Big\lfloor \frac{f}{f_s} \Big\rfloor \Big|`

With :math:`\lfloor x \rfloor` as round to next integer.

At a sampling rate :math:`f_s = 1000 \ \mathrm{Hz}` and a Nyquist
frequency :math:`f_N = 500 \ \mathrm{Hz}`, a sinusoid with
:math:`f = 900 \ \mathrm{Hz}` will be interpreted as one with
:math:`f = 100 \ \mathrm{Hz}`:

.. parsed-literal::

    f_m = 100


The following example can be used interactively as a Jupyter notebook,
by changing the frequency of a sinusoid and listening to the aliased
output. When sweeping the range up to :math:`2500 \ \mathrm{Hz}`, the
resulting output will increase and decrease in frequency. In the static
version, a sinusoid of :math:`f = 900 \ \mathrm{Hz}` is used, resulting
in an audible output at :math:`f_m = 100 \ \mathrm{Hz}`:



Interactive Example
-------------------

.. raw:: html
   :file: /media/anwaldt/ANWALDT_2TB/WORK/TEACHING/Computer_Music_Basics/webaudio/aliasing-sine.html

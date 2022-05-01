.. title: Envelopes: Exponential
.. slug: envelopes-exponential
.. date: 2020-11-05 13:47:15 UTC
.. tags:
.. category: basics:control
.. priority: 6
.. link:
.. description:
.. type: text
.. has_math: true

For percussive, plucked or struck instrument sounds, the envelope needs to
model an exponential decay. This is very useful for string-like sounds but
most importantly for most electronic musicians, it is the very core of kick drum sounds.

In contrast to the ADSR envelope, the exponential one does not
contain a sustain portion for holding a sound. The only parameter is the decay rate,
allowing quick adjustment. Alternative to an actual exponential, a modified
reciprocal function can be used for easier implementation. The factor $d$ controls
the rate of the decay, respectively the decay time:

$$
e = \\frac{1}{(1+(d t))}
$$

----

The following example adds a short linear attack before the exponential decay.
This minimizes clicks which otherwise occur through the rapid step from $0$ to $1$:

.. raw:: html
   :file: ../Computer_Music_Basics/webaudio/exponential.html

.. title: Audio Buffers
.. slug: audio-buffers
.. date: 2021-04-14 16:00:00 UTC
.. tags:
.. category: basics:signals-and-systems
.. link:
.. description:
.. has_math: true
.. type: text
.. priority: 5


Most systems for digital signal processing and music programming process audio
in chunks, which are defined by a so called buffer size. These buffer sizes are
usually powers of 2, usually ranging from $16$ samples - which can be considered a small
buffer size - to $2048$ samples (and more). Most applications, like DAWs and hardware
interfaces allow the user to select this parameter.
Technically this means that a system collects (or buffers) single samples -
for example from an ADC (analog-digital-converter) -
until the buffer is filled. This compensates irregularities in the speed of execution
for single operations and ensures a jitter-free processing.

-----

Latency
-------

The choice of the buffer size $N$ is usually a trade-off
between processor load and system latency. Small buffers require faster processing whereas large
buffers keep the user waiting until a buffer has been filled.
In combination with the sampling rate $f_s$, the buffer-dependent latency can be calculated as follows:

$$
\\tau = \\frac{N}{f_s}
$$

Round trip latency usually considers both the input and output buffers, thus doubling the latency.
For a system running at $48\\ \\mathrm{kHz}$ with a buffer size of $128$ samples - a typical size
for a decent prosumer setup - this results in a round trip latency of $5.5\\ \\mathrm{ms}$.
This value is low enough to allow a perceptually satisfying interaction with the system.
When exceeding the $10\\ \\mathrm{ms}$ threshold it is likely that percussions and other
timing-critical instruments experience disrupting latency.

----

Buffers in Programming
----------------------

In higher level programming environments like PD, MAX, SuperCollider or Faust
(depending on the way it is used), users usually do not need to deal with the buffer size.
When programming in C or C++, most frameworks and APIs offer a processing routine which is
based on the buffer size. This accounts for solutions like JUCE or the
JACK API, but also when programming externals or extensions for the above mentioned higher level
environments. These processing routines, also referred to as callback, are called by an interrupt
once the the hardware is ready to process the next buffer.

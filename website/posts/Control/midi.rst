.. title: The MIDI Protocol
.. slug: the-midi-protocol
.. date: 2020-11-05 13:47:15 UTC
.. tags:
.. category: basics:control
.. priority: 0
.. link:
.. description:
.. type: text
.. has_math: true

The MIDI protocol was released in 1982 as a means
for connecting electronic musical instruments.
First synths to feature the new technology were the
Prophet-600 and the Jupiter-6.
Although limited in resolution from a recent point of view,
it is still a standard for conventional applications -
yet to be replaced by the newly released MIDI 2.0.
Besides rare mismatches and some limitations, MIDI devices
can be connected without complications.
Physically, MIDI has been introduced with the still widespread
5-pin connector, shown below. In recent devices, MIDI is usually
transmitted via USB.

.. raw:: html

   <div align="center">
   <a href="discount"><img width="150" src="/images/basics/midi-input.png" alt="MIDI jack  (5-pin DIN)."></a>
   <p><i>
   MIDI jack  (5-pin DIN).
   </i></p>
   </div>




|






----

Standard MIDI Messages
----------------------

MIDI transmits binary coded messages with a speed of
$31250\\  \\mathrm{kbit/s}$. Timing and latency are thus
not a problem when working with MIDI. However, the resolution of control
values can be a limiting factor.
Standard MIDI messages consist of three Bytes, namely one
status Byte (first bit green) and two data bytes (first bit red).
The first bit declares the Byte either a status Byte (1) or a
data Byte (0).

.. figure:: /images/basics/midi-message.png
    :width: 500

    *Standard MIDI message with three Bytes.*

----

Some of the most common messages are listed in the table below.
Since one bit is used as the status/data identifier,
7 bits are left for encoding.
This results in the typical MIDI resolution of :math:`2^7 = 128` values
for pitch, velocity or control changes.

.. code-block:: console

    Voice Message           Status Byte      Data Byte1          Data Byte2
    -------------           -----------   -----------------   -----------------
    Note off                      8x      Key number          Note Off velocity
    Note on                       9x      Key number          Note on velocity
    Polyphonic Key Pressure       Ax      Key number          Amount of pressure
    Control Change                Bx      Controller number   Controller value
    Program Change                Cx      Program number      None
    Channel Pressure              Dx      Pressure value      None
    Pitch Bend                    Ex      MSB                 LSB

----

Pitch Bend
----------

If you are stuck with MIDI for some reason but need a higher
resolution, the Pitch Bend parameter can help.
Each MIDI channel has one Pitch Bend, each with two combined
data Bytes, resulting in a resolution of :math:`128^2 = 16384` steps.

-----


System Exclusive
----------------

SysEx messages can be freely defined by manufacturers.
They are often used for dumping or loading settings and presets,
but can also be used for arbitrary control purposes.
SysEx messages can have any length and are not standardized.


-----

MIDI Note to Hertz
------------------

When working with MIDI, a conversion from MIDI pitch to Hertz is often necessary.
There are two simple formulas for doing that. They both refer to the MIDI pitch of 69, wich corresponds to a frequency of 440 Hz:

.. math::
  f[\mathrm{Hz}] = 2 \frac{\mathrm{MIDI}-69}{12} 440

.. math::
  \mathrm{MIDI} = 69 +12 \log_2 \left( \frac{f}{440 \mathrm{Hz}} \right)

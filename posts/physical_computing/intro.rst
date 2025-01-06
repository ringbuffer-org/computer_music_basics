.. title: Physical Computing in Music and Sound Art
.. slug: physical_computing_in_music
.. date: 2023-02-08
.. tags:
.. category: basics:interfaces
.. priority: 0
.. link:
.. description:
.. type: text


The term *physical computing* describes the use of micro-controller-based solutions for connecting
software processes to the physical world. Sensors for obtaining physical quantities and actuators for manipulating objects
open up manifold applications in sound art and music.
Due to the rise of low cost, easy to program development boards like the `Arduino <https://www.arduino.cc/>`_,
creative projects have easy access to these possibilities, giving rise to a variety of individual interfaces, controllers
and installation concepts.
Many projects presented at conferences like `NIME <https://www.nime.org/>`_ are based on such solutions.

The Arduino is the most popular and established platform. It will be used in the examples and
tutorials in this section.
Other examples in the following sections are based on
the `Teensy Board <https://www.pjrc.com/teensy/>`_  or the `ESP32 <https://www.espressif.com/en/products/devkits>`_ , which are programmed in the same way as the Arduino.


----

Sensor-Based Projects
=====================

BinBong
-------

The first version of the BinBong (von Coler et al, 2017) is a haptic musical interface,
using a MIDI over USB wired communication.
A Teensy board is used to capture the force applied to four valve-like
mechanics and the wooden top.
The goal of this research-oriented instrument is to investigate the expressive
means of force-based control in monophonic electronic musical instruments.

.. figure:: /images/basics/binbong1_front_view.jpg
  :figwidth: 45%
  :width: 44%
  :align: center
  :alt: Front view of the BinBong with valve mechanics and wooden top.

  Front view of the BinBong with valve mechanics and wooden top.

.. figure:: /images/basics/binbong1_rear_view.jpg
  :figwidth: 45%
  :width: 44%
  :align: center
  :alt: Rear view of the BinBong with Teensy and octave switches.

  Rear view of the BinBong with Teensy and octave switches.


-----

BinBong MKII
------------

Based on the findings of the BinBong, a second, wireless version was
designed, using a RedBear Duo board with integrated WiFi communication (Schmied, 2018).
It has been designed to control spatial sound synthesis (von Coler et al., 2020)
with an additional IMU and is used within user studies on mapping
and expressivity (von Coler, 2021).

.. figure:: /images/basics/bin_bong_mk2.jpg
  :figwidth: 100%
  :width: 25%
  :align: center
  :alt: BinBong MKII.

  BinBong MKII.

-----

GameTrak: The Gallows
---------------------

The GameTrak is a motion controller for the Playstation, launched in 2004.
Nowadays, it is obsolete as a gaming device and used devices are cheap.
The actual control unit is basically a joystick with a string attached,
allowing to measure displacement and lengthening via potentiometers:


.. figure:: /images/basics/gametrak.jpg
  :figwidth: 100%
  :width: 33%
  :align: center
  :alt: GameTrak sensor.

The GameTrak is easily hacked in many ways and has thus been used in many experimental
music projects and by laptop orchestras (Huberth & Nanou, 2016).
It can be easily integrated into projects using PD, SC and other environments,
while the potentiometers are very reliable.
The follwing short demo video shows a small version of The Gallows with
a simple PD sample synthesis patch:

.. raw:: html

    <center>
    <video width="49%" controls src="/files/videos/cmb/gallows_demo.mp4"></video>
    </center>

Visit the `Gallows Website <https://hvc.berlin/performance/the-gallows/>`_ for more
information and audio recordings or get the code: https://github.com/anwaldt/The_Gallows


-----

PS_Gloves
---------

The PS_Gloves are a project by Paul Schuladen, developed between 2018 and 2023
and now being finalized in his master's thesis.
They track posture and orientation of the hand, using two inertial measurement units (IMU)
and various capacitive sensors at the finger tips.
Within a final study, they are used to play physical models of string instruments.


.. figure:: /images/basics/ps_glove_1.jpeg
  :figwidth: 100%
  :width: 44%
  :align: center


-----

Actuator-Based Projects
=======================

Cybernetic-playing Guitar
-------------------------

Building a self-playing and tuning guitar in a student project in a 2011 class with Douglas Repetto at TU Berlin.
These videos show only the isolated attempts at plucking the strings with selenoids and tuning them with servo motors:

.. raw:: html

    <center>
    <video width="49%" controls src="/files/videos/cmb/pluck.mp4"></video>
    <video width="49%" controls src="/files/videos/cmb/tune.mp4"></video>
    </center>

-----

Ton-Technik & Pot-Shot
----------------------

In his installations `Ton-Technik  <https://www.bartetzki.de/de/tontechnik.html>`_ and
`Pot-Shot  <https://www.bartetzki.de/de/pot-shot.html>`_, Andre Bartetzki uses solenoids
to excite clay pots. An Arduino Mega is used in combination with SuperCollider to trigger the selenoids in specific patterns:


.. raw:: html

  <center>
  <iframe width="49%" height="400"
  src="https://www.youtube.com/embed/VaOFgwalFxE?start=148">
  </iframe>
  <iframe width="49%" height="400"
  src="https://www.youtube.com/embed/FoaMXX-Fz2E">
  </iframe>
  </center>


-----

References
----------

.. publication_list:: bibtex/interfaces.bib
	   :style: unsrt

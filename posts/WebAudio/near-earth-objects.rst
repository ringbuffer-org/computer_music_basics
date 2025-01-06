.. title: Asteroids - NeoWs
.. slug: asteroids-neows
.. date: 2022-07-17 22:00:00 UTC
.. tags:
.. category: basics:webaudio
.. link:
.. description:
.. type: text
.. has_math: true
.. data:
.. priority: 3


NeoWs
-----

At https://api.nasa.gov/, the NASA offers various APIs.
This example uses data from the 'Asteroids - NeoWs'  RESTful web service,
which contains data of near earth Asteroids.

-----

JSON Data Structure
-------------------

The JSON data is arraned as an array, featuring the data on
20 celestial bodies, accessible via index:

.. code-block::

  links	{…}
  page	{…}
  near_earth_objects
    0	{…}
    1	{…}
    2	{…}
    3	{…}
    4	{…}
    5	{…}
    6	{…}
    7	{…}
    8	{…}
    9	{…}
    10	{…}
    11	{…}
    12	{…}
    13	{…}
    14	{…}
    15	{…}
    16	{…}
    17	{…}
    18	{…}
    19	{…}


------

Harmonic Sonification
---------------------

Mapping
=======

All entries of the individual Asteroids can be used as
synthesis parameters in a sonification system with
Web Audio.
This example uses two parameters of the Asteroids within an additive synthesis paradigm:

.. code-block::

    orbital_period       = sine wave frequency
    absolute_magnitude_h = sine wave  amplitude

More info on the orbital parameters:

https://en.wikipedia.org/wiki/Orbital_period

https://en.wikipedia.org/wiki/Absolute_magnitude

-----

The Result
----------

.. raw:: html
   :file: ../Computer_Music_Basics/webaudio/nasa_api.html



-----

..
.. Code
.. ====
..
.. .. listing:: nasa_api.html html

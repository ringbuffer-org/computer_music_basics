.. title: Raspberry Pi
.. slug: raspberry-pi
.. date: 2020-11-05 11:47:15 UTC
.. tags:
.. category: basics:linuxaudio
.. priority: 2
.. link:
.. description:
.. type: text


The class `Sound Synthesis <https://www.ak.tu-berlin.de/menue/lehre/vergangene_semester/sommersemester_2019/sound_synthesis/>`_
at TU Berlin makes use of the Raspberry PI as a development and runtime system for sound synthesis in C++ `(von Coler, 2017) <https://www.researchgate.net/publication/330359720_Teaching_Sound_Synthesis_in_CC_on_the_Raspberry_Pi>`_.
Firtly, this is the cheapest way of setting up a computer pool with unified hard- and software.
In addition, the PIs can serve as standalone synthesizers and sonification tools.
All examples can be found in a dedicated `software repository <https://github.com/anwaldt/sound_synthesis_pi>`_.

The full development system is based on free,
open source software.
The examples are based on the JACK API  for audio input and output,
``RtAudio`` for MIDI,
as well as the ``liblo`` for OSC communication and ``libyaml-cpp``
for data and configuration files.

The advantage and disadvantage of this setup is that every element needs
to be implemented from scratch. In this way, synthesis algorithms can be
understood in detail and customized without limitations.
For quick solutions it makes sense to switch to a framework
with more basic elements.
The source code can also be used on any Linux system,
provided the necessary libraries are installed.

-----

The Gain Example
----------------

The gain example is the entry point for coding on the PI system:
https://github.com/anwaldt/sound_synthesis_pi

-----

References
----------

.. publication_list:: bibtex/jack.bib
	   :style: unsrt

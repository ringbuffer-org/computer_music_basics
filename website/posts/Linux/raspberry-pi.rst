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
at TU Berlin makes use of the Raspberry PI as a development and runtime system for sound synthesis in C++ (von Coler, 2017).
Firtly, this is the cheapest way of setting up a computer pool with unified hard- and software.
In addition, the PIs can serve as standalone synthesizers and sonification tools.
All examples can be found in a dedicated software repository:

https://gitlab.tubit.tu-berlin.de/henrikvoncoler/SoundSynthesis_PI

The full development system is based on free, 
open source software.
The examples are based on the JACK API  for audio input and output,
``RtAudio`` for MIDI, 
as well as the ``liblo`` for OSC communication and ``libyaml-cpp``
for data and configuration files.

The advantage and disadvantage of this setup is that every element needs
to be implemented from scratch. In this way, synthesis agorithms can be
understood in detail and customized limitlessly.
For quick solutions it makes sense to switch to a framework
with more basic elements.

The source code can also be used on any linux system,
provided the necessary libraries are installed.

The Gain Example
----------------

The gain example is the entry point for coding on the PI system:

https://gitlab.tubit.tu-berlin.de/henrikvoncoler/SoundSynthesis_PI/tree/master/examples/gain_example

References
----------

.. publication_list:: bibtex/jack.bib
	   :style: unsrt

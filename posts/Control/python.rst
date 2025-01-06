.. title: Using Python for Control
.. slug: using-python-for-control
.. date: 2020-11-05 13:47:15 UTC
.. tags:
.. category: basics:control
.. priority: 3
.. link:
.. description:
.. type: text



Python offers many useful tools for preparing data and  controlling synthesis processes.
Although it can also be used for actual digital signal processing, its versatility
makes it a great tool for auxuliary tasks.
Most notably, it can be used for flexible
processing and routing of OSC messages,
especially in the field of data sonification.

-----

Python & OSC
------------

A large variety of Python packages offers
the possibility of using OSC. They can be installed
using pip:

.. code-block:: console

 $ pip install python-osc
 $ pip install pythonosc

|

An example project for controlling a Faust-built
synthesizer with Python is featured in this
software repository:
https://github.com/anwaldt/py2faust_synth

-----

Python & JACK
-------------

The `JACK Audio Connection Kit Client for Python <https://github.com/spatialaudio/jackclient-python/>`_
by Matthias Geier connects Python processes to the JACK server.
This integration of Python in a JACK ecosystem
can be helpful not only for audio processing, but also for synchronization of processes.
Since the Python package also implements the JACK transport functions,
it can be used to couple Python threads to the timeline of audio projects.

 

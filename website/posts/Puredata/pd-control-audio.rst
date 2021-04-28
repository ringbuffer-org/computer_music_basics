.. title: Control Rate and Audio Rate
.. slug: control-rate-and-audio-rate
.. date: 2020-11-05 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 2
.. link:
.. description:
.. type: text

Like many other audio programming environments, PD makes a difference between control signals and audio signals. They run at different rates and can not be combined, unless converted. Audio operations require the DSP to be activated, whereas control rate signal work at any time. Objects define whether an outlet gets or outputs control or audio rate signals. Objects with audio inputs or outputs are usually named with a ``~``. Control rate connections are thinner than audio rate signals:


.. figure:: /images/basics/pd-rates.png
	    :width: 600

-----

Audio to Control
----------------

Converting audio signals to control rate signals can be achieved with the ``snapshot~`` object. This object needs to be triggered to grab a snapshot, which is done with a metronome object at 100 Hz in this example. The output is a level indicator for the LFO at 0.1 Hz.

.. figure:: /images/basics/pd-audio-to-control.png
	    :width: 400

-----

Control to Audio
----------------

Usually, control signals can be connected to audio inlets. In some cases it might be necessary to convert control signals to audio rate. This is done with the ``sig~`` object:

.. figure:: /images/basics/pd-control-to-audio.png
	    :width: 400
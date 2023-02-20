.. title: Max for Live: Live Object Model
.. slug: max4live_object_model
.. date: 2023-02-08
.. tags:
.. category: basics:interfaces
.. priority: 20
.. link:
.. description:
.. type: text

Max's Live Object Model makes it possible to exchange data between
Max for Live and any parameter of a Live session.
The model is best described in the
`Max Online Documentation  <https://docs.cycling74.com/max8/vignettes/live_object_model>`_.
and the
`Live API Overview <https://docs.cycling74.com/max8/vignettes/live_api_overview>`_

In the following examples, different Live parameters are controlled via
LFOs or direct input to demonstrate the capabilities.


----

The Live Object Model
=====================

Working with the Live Object Model involves four objects:

- The ``live.path`` object is used to select objects in the Live object hierarchy. It receives a message, pointing to the object which is to be accessed.

- ``live.object`` is used to get and set properties and children of objects and to call their functions.

- The ``live.observer`` object can subscribe to properties of objects and their children and gets regular updates on changes.

- With the ``live.parameter~`` object it is possible to control Live device parameters in real time.


----

Controlling the Live Set
========================

This first example allows to change the playback speed of the Live session in BPM.
The live object only needs the path to the Live set (``live_set``) and
can then process the ``set tempo $1`` message.

.. figure:: /images/basics/Max_For_Live/set_live_set_bpm.png
  :figwidth: 100%
  :width: 33%
  :align: center
  :alt: Setting the session tempo from Max for Live.

  Setting the session tempo from Max for Live.


-----

Triggering Clips
================

Each clip in Live's session view can be accessed with an individual path.

Once set with the ``goto ...`` message, the ``call fire`` message can trigger the sample.

.. figure:: /images/basics/Max_For_Live/live_clip_trigger.png
  :figwidth: 100%
  :width: 33%
  :align: center
  :alt: Launching the first clip of the second channel from Max for Live.

  Launching the first clip of the second channel from Max for Live.

This tutorial gives more insight on controlling all clip properties offered by Live: `Hack Live 11 Clip Launching <https://cdm.link/2021/06/get-started-with-max-for-live-and-hack-live-11-clip-launching-heres-how-videos/>`_

-----

Controlling Device Parameters
=============================


By controlling device parameters, any synth or effect inside a Live
project can be automated from Max For Live patches.
Although this is a very powerful feature, paths to the objects need to be tracked
down by the indices of the channel, the plugin and the parameter.



-----

Instrument Channels
-------------------


In this example, the Granulator II is used. It can be installed via
the `Ableton Website <https://www.ableton.com/en/packs/granulator-ii/>`_.
The first thing to do is find the right path for the device and parameter.


.. figure:: /images/basics/Max_For_Live/lfo_to_grain_pos.png
  :figwidth: 100%
  :width: 55%
  :align: center
  :alt: xxx.

  oköas .



----


Main Channel
------------

Main channel effects and plugins can be controlled in the same way as those in instrument channels,
omitting the channel index.

.. figure:: /images/basics/Max_For_Live/control_main_device_parameter.png
  :figwidth: 100%
  :width: 44%
  :align: center
  :alt: Patch for controlling the cutoff frequency of a filter in the main channel.

  Patch for controlling the cutoff frequency of a filter in the main channel.


-----

Exercise
========

.. admonition:: Exercise

		Combine the above patches with the Max for Live sensor examples to directly control Live parameters with the Arduino.

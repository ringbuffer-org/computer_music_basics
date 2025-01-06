.. title: Max for Live: A Short Introduction
.. slug: max4live_intro
.. date: 2023-02-08
.. tags:
.. category: basics:max4live
.. priority: 1
.. link:
.. description:
.. type: text


Max for Live makes max patches run as part of an Ableton Live session.
Depending on the nature of the patch, it can be inserted as a device in Audio or MIDI tracks
by drag and drop.
MIDI and audio outlets of the patch will be visible and usable inside Live like the
connection of any other component.
Over the years, many devices have been created by the community, some for free, some for sale: https://maxforlive.com/

The concept and its details are best described on `Ableton's Live page <https://www.ableton.com/en/live/max-for-live/>`_.
This short introduction should only cover the very basics for a quick start.

-----

Max Audio Effects
-----------------

Dragging the default Max Audio Effect into a track gives a basic patch
connecting audio inlets (``plugin~``) with audio outlets (``plugout~``).
Any processing can be inserted in between.


.. figure:: /images/basics/Max_For_Live/m4l_default_audio.png
  :figwidth: 100%
  :width: 25%
  :align: center
  :alt: The default Max Audio Effect.

  The default Max Audio Effect.


The following example uses the ``degrade~`` object inside a Max Audio Effect.


.. figure:: /images/basics/Max_For_Live/m4l_degrader.png
  :figwidth: 100%
  :width: 25%
  :align: center
  :alt: A degrader effect.

  A degrader effect inside Max for Live.


-----

Max Instruments
---------------

The default Max Instrument can be dragged into a MIDI channel. It gives
a patch with a ``midiin`` object to receive any incoming MIDI data and
the ``plugout~`` object to send audio into Live.
Unlike the default Audio Effect, this patch is not functional.

.. figure:: /images/basics/Max_For_Live/m4l_default_instrument.png
  :figwidth: 100%
  :width: 25%
  :align: center
  :alt: The default Max Instrument.

  The default Max Instrument.

Like the ``midiin`` object, other MIDI objects in Max can also be used inside Max For Live devices.
The following mini saw example shows how to control a patch with MIDI from Live, using  the ``notein``
and the ``ctlin`` objects.

.. figure:: /images/basics/Max_For_Live/m4l_midi_synth.png
  :figwidth: 100%
  :width: 25%
  :align: center
  :alt: A mini saw synthesizer.

  A mini saw synthesizer.

-----

Automation to Max for Live
--------------------------

The Inspector View
==================

Although controlling Max for Live with MIDI is a good solution for many applications,
Device Parameter Automation offers more flexibility and can also be used in audio channels.
Most parameters in a Max for Live patch can be activated for automation, by editing inside the number inspector:


.. figure:: /images/basics/Max_For_Live/number_inspector.png
  :figwidth: 100%
  :width: 55%
  :align: center
  :alt: The number inspector in Max for Live.

  The number inspector in Max for Live.


The following adjustments need to be made:

- Parameter Mode Enable: check
- Name (long/short): foo
- Type: match parameter
- Range: match parameter
- Modulation Mode: match parameter
- Parameter Visibility: Automated and Stored



Track Automation
================

After making the Max for Live parameters ready for automation, the general automation mode needs to be
enabled in the Arranger view (the tiny blue button above the audio track).
Afterwards, each tack shows the available automation parameters and they can be edited.


.. figure:: /images/basics/Max_For_Live/automation_mode.png
  :figwidth: 100%
  :width: 80%
  :align: center
  :alt: Automation in the arranger window.

  Automation in the arranger window.



Clip Automation
===============

The automation panel in the clip view gives access to all activated Max for Live parameters.
This kind of modulation is tightly linked to the audio material, which can be both helpful and complicated.

.. figure:: /images/basics/Max_For_Live/clip_automation.png
  :figwidth: 100%
  :width: 95%
  :align: center
  :alt: Clip automation.

  Clip automation.

Find more information on live parameters: https://docs.cycling74.com/max5/vignettes/core/live_parameters.html

------


Exercise
========

.. admonition:: Exercise I

		Create a MIDI instrument and generate a sequence with parameter changes.

.. admonition:: Exercise I

		Realize a short acousmatic composition with Max for Live audio effects and automated parameters.

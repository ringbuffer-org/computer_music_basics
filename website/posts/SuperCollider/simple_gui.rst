.. title: Simple GUI
.. slug: simple_gui
.. date: 2023-05-10 10:00:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 6
.. link:
.. description:
.. type: text


SuperCollider comes with a powerful unified Qt GUI framework to create functional user interfaces with little effort.
The comprehensive `SuperCollider GUI Introduction <https://doc.sccode.org/Guides/GUI-Introduction.html>`_ includes many details
on the use and customization of GUI elements.

This example focuses on the plain use of a vertical slider to control a parameter of a node:

.. code-block:: supercollider

  (

	// a sine oscillator node with one parameter
	var x = {|freq=100| Out.ar(0, SinOsc.ar(freq))}.play;

	// create a window with width and position
    var w = Window("Slider", Rect(128, 64, 800, 480));

	// add a slider
	var slider = Slider(w, Rect(400,200,60,200));

	// the callback function on slider move
	slider.action_({x.set(\freq, slider.value * 10000)});

	// "same effect as setting -visible to true"
	w.front;

  )



//defer()


Exercise
========

.. admonition:: Exercise

    Use the ``Slider2D`` class to control two parameters of a node (gain+frequency, 2xfrequency, ...).

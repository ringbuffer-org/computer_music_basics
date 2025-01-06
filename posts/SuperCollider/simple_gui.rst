.. title: Simple GUI
.. slug: simple_gui
.. date: 2023-05-10 10:00:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 11
.. link:
.. description:
.. type: text


SuperCollider comes with a simple Qt GUI framework to create functional user interfaces with little effort.
The comprehensive `SuperCollider GUI Introduction <https://doc.sccode.org/Guides/GUI-Introduction.html>`_ includes many details
on the use and customization of GUI elements.

This example usees a slider to control a parameter of a sine oscillator and a button to trigger a noise burst:

.. code-block:: supercollider

	(
	// a sine oscillator node with one parameter
	var x = {|freq=100| Out.ar(0, SinOsc.ar(freq))}.play;

	// create a window with width and position
	var w = Window("Slider", Rect(128, 64, 800, 480));

	// add a slider
	var button = Button(w, Rect(400,50,200,200));

	// add a slider
	var slider = Slider(w, Rect(10,300,1000,100));

	// the callback function on slider move
	slider.action_({x.set(\freq, pow(slider.value,4) * 10000)});

	button.mouseDownAction = {{Out.ar(0, EnvGen.ar(Env([1,0],[1],'lin'),doneAction:Done.freeSelf) * WhiteNoise.ar())}.play};
	// same as button.mouseDownAction_(...)

	w.fullScreen;
	// "same effect as setting -visible to true"
	w.front;

	)



Exercises
=========


.. admonition:: Exercise I

		Build a GUI with a button to send OSC messages to a peer.


.. admonition:: Exercise II

	Use the ``Slider2D`` class to control two parameters of a node (gain+frequency, 2xfrequency, ...).

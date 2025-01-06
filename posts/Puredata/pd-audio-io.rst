.. title: Audio Input & Output in PD
.. slug: pd-audio-io
.. date: 2022-04-30 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 1
.. link:
.. description:
.. type: text



All objects which have audio inputs or outputs are written with a tilde as last character of their name(~).
The two objects introduced in this minimal example get audio signals from the
audio interface (``adc~`` - for analog-digital-conversion),
respectively send them to the audio interface (``dac~``, for digital-analog-conversion):


.. figure:: /images/basics/pd-audio-io.png
	:figwidth: 100%
	:width: 400px
	:align: center

Both ``adc~`` and ``dac~`` have one creation argument - the index of the input our output, counting from **1**.
The above shown example gets the left and the right channel from the audio hardware and swaps them,
before sending them to the audio output.


.. warning::

	When started on a laptop without headphones, the patch might generate a loud feedback-loop.


-----

Activating DSP
--------------

PD patches will only process audio when DSP has been activated.
This can be done in the ``Media`` section of the top menu or with the shortcut ``Ctrl+/`` (``Cmd+/`` on Mac).
DSP can always be killed using the shortcut ``Ctrl+.`` (``Cmd+.`` on Mac).

-----

References
----------

.. publication_list:: bibtex/visual-programming.bib
	   :style: unsrt

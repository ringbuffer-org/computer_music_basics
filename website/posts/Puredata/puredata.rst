.. title: Getting Started with Puredata
.. slug: getting-started-with-puredata
.. date: 2020-11-05 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 1
.. link:
.. description:
.. type: text

About
-----

Puredate (PD) is the free and open source version of Max/MSP, also developed and maintained by Miller Puckette. PD is one of the best options for people new to computer music, due to the obvious signal flow. It is a very helpful for exploring the basics of
sound synthesis and programming but can also be used for advanced applications: https://puredata.info/community/member-downloads/patches. In addition, PD offers simple and flexible means for creating control and GUI software.
There are a lot of great tutorials and examples online.
This one features almost anything to know: `PD-Flossmanuals <http://write.flossmanuals.net/pure-data/>`_

-----

Installing Extensions
---------------------

The official standard version of Pure Data is referred to *Pd-vanilla*. It features  `Deken <https://github.com/pure-data/deken>`_, a framework to for installing externals from within Pure Data. Some of the examples in this section make use of such extensions. The GUI version of Deken is located in the menu under ``Help->Find Externals``. After downloading an extension to the default location of the operating system, the paths need to be added, manually in ``Edit->Preferences->Path``.
This site is very helpful when figuring out which extension a missing object belongs to:
http://write.flossmanuals.net/pure-data/audio-filters/

-----

The Sine Example
----------------

This very basic `sine.pd <https://raw.githubusercontent.com/anwaldt/computer-music-basics/main/puredata/sine.pd>`_ example creates a sine wave oscillator. Its frequency can be controlled with a horizontal slider. Ann additional toggle object allows to switch
the sine on and of, by means of multiplication. When used without arguments, the ``dac~`` object has two inlets,
which relate to the left and right channel of the audio interface. The additional message box with the ``bang``
can be used to activate the DSP. This is necessary for getting any sound and can also be done in the menu.


.. figure:: /images/basics/pd-sine.png
	    :width: 400


-----


References
----------

.. publication_list:: bibtex/visual-programming.bib
	   :style: unsrt

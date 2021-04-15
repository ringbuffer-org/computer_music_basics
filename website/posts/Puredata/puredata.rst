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
sound synthesis and programming but can also be used for advanced applications: https://puredata.info/community/member-downloads/patches In addition, PD offers simple and flexible means for creating control and GUI software.



Installing Extensions
---------------------

The official standard version of Pure Data is referred to *Pd-vanilla*. It features a `Deken <https://github.com/pure-data/deken>`_, a framework to for installing externals from within Pure Data. Some of the examples in this section make use of such extensions. The GUI version of Deken is located in the menu under ``Help->Find Externals``. After downloading an extension to the default location of the operating system, the paths need to be added, manually in ``Edit->Preferences->Path``.


The Sine Example
----------------

This first example creates a sine wave oscillator.
Its frequency can be controlled with a slider:

.. figure:: /images/basics/pd-sine.png
	    :width: 400



.. publication_list:: bibtex/visual-programming.bib
	   :style: unsrt

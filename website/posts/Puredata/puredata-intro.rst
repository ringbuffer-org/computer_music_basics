.. title: Getting Started with Puredata
.. slug: getting-started-with-puredata
.. date: 2020-11-05 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 0
.. link:
.. description:
.. type: text

About
-----

Puredate (PD) is the free and open source version of Max/MSP, also developed and maintained by
Miller Puckette. PD is one of the best options for people new to computer music,
due to the obvious signal flow. It is a very helpful for exploring the basics of
sound synthesis and programming but can also be used for advanced applications:
https://puredata.info/community/member-downloads/patches.

As a graphical programming environment, PD offers simple and flexible means for creating control
and GUI software. There are a lot of great tutorials and examples online.
This one features almost anything to know:  http://write.flossmanuals.net/pure-data/


-----

Versions & Download
===================

PD comes in different versions, including customized ones for specific applications (*Pd-L2Ork*) or *PurrData* with an
HTML5 GUI.
This tutorial relies on the plain version, referred to as *vanilla*. The latest build can be downloaded here for all
major operating systems: https://puredata.info/downloads/pure-data


-----

Help Files
==========

The help files shipped with the install of PD feature a plethora of examples on
programming principles and audio signal processing, both for beginners and advanced.
Many examples and parts of this tutorial are based on this library.
It is recommended to explore the contents of the help browser.


-----

Working with PD Files
=====================

PD patches are organized in files with the ``.pd`` extension. This first patch
is the well known *Hello World!* example, not using any audio processing:


.. figure:: /images/basics/pd-hello-world.png
	:figwidth: 100%
	:width: 400px
	:align: center


It introduces two concepts:

		- A message, containing the string *Hello World!*.
		- An object, namely ``print``, printing the string to the PD console in the main window.


Edit Mode / Performance Mode
----------------------------

PD can operate in two modes:

- The *Edit Mode* allows to change patches (add, move and connect objects).
- The *Performance Mode* is used to perform with the patches (change values, operate GUI elements).

The mode can be changed in the menu or via the shortcut ``Ctrl+E`` (``Cmd+E`` on Mac).
Only when in *Performance Mode*, the message object can be clicked and and the output is printed.


Text File Format
----------------

All PD patches are stored as text files, declaring objects and connections line by line.
This makes version control possible, although small changes
in object positions can result in many changes inside the text representation.
For the above example, the related text version of the PD file looks as follows:

.. code-block::

			#N canvas 899 583 450 300 12;
			#X obj 75 107 print;
			#X msg 75 29 Hello World!;
			#X connect 1 0 0 0;



-----


References
----------

.. publication_list:: bibtex/visual-programming.bib
	   :style: unsrt

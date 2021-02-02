.. title: Puredata
.. slug: puredata
.. date: 2020-11-05 13:46:52 UTC
.. tags: 
.. category: basics:languages
.. priority: 3
.. link: 
.. description: 
.. type: text

About
-----

Puredate (PD) is the free and open source version
of Max/MSP, also developed and maintained by Miller Puckette.
PD is one of the best options for people
new to computer music, due to the obvious signal flow.
It is a very helpful for exploring the basics of
sound synthesis and programming but can also be
used for advanced applications: https://puredata.info/community/member-downloads/patches
In addition, PD offers simple and flexible means
for creating control and GUI software.



The Sine Example
----------------

This first example creates a sine wave oscillator.
Its frequency can be controlled with a slider:

.. figure:: /images/basics/pd-sine.png
	    :width: 400


   
Working with OSC
----------------


Dependencies
============

OSC can be used in Puredata without further packages,
by means of the ojects ``netsend``, ``oscformat`` and ``oscparse``.
The following examples are based on additional 
externals, since this results in more compact patches.
For using them, install the external ``mrpeach`` with
the Deken tool inside Puredata: https://puredata.info/docs/Deken


Sending OSC
===========



This example sends data via osc between two
puredata patches on the same machine.
It uses the hostname ``localhost`` instead of an 
IP address.
The path  ``oscillator/frequency``
of the OSC message has been defined arbitrarily -
it has to match between client and receiver.
Before sending osc messages, the connect message
needs to be clicked.


.. figure:: /images/basics/pd-osc-send.png
	    :width: 400


Receiving OSC
=============

Before receiving osc messages, the ``udpreceive`` oject
needs to know which  port to listen on.
Messages are then unpacked and routed according
to their path.

.. figure:: /images/basics/pd-osc-receive.png
	    :width: 400



References
----------

.. publication_list:: bibtex/visual-programming.bib
	   :style: unsrt

		 

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


   
Working with OCS
----------------


Dependencies
============

OSC can be used in Puredata without further packages,
by means of the ojects ``netsend``, ``oscformat`` and ``oscparse``.
The following examples are based on additional 
externals, since this results in more compact patches.
For using them, install the external ``mrpeach`` with
the Deken tool inside Puredata: https://puredata.info/docs/Deken

SENDING OSC
===========



THIS EXAMPLE SENDS DATA VIA OSC BETWEEN TWO
PUREDATA PATCHES ON THE SAME MACHINE.
IT USES THE HOSTNAME ``LOCALHOST`` INSTEAD OF AN 
IP ADDRESS.
THE PATH  ``OSCILLATOR/FREQUENCY``
OF THE OSC MESSAGE HAS BEEN DEFINED ARBITRARILY -
IT HAS TO MATCH BETWEEN CLIENT AND RECEIVER.
BEFORE SENDING OSC MESSAGES, THE CONNECT MESSAGE
NEEDS TO BE CLICKED.


.. FIGURE:: /IMAGES/BASICS/PD-OSC-SEND.PNG
	    :WIDTH: 400


RECEIVING OSC
=============

BEFORE RECEIVING OSC MESSAGES, THE ``UDPRECEIVE`` OJECT
NEEDS TO KNOW WHICH  PORT TO LISTEN ON.
MESSAGES ARE THEN UNPACKED AND ROUTED ACCORDING
TO THEIR PATH.

.. FIGURE:: /IMAGES/BASICS/PD-OSC-RECEIVE.PNG
	    :WIDTH: 400



References
----------

.. publication_list:: bibtex/visual-programming.bib
	   :style: unsrt

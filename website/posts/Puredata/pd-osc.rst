.. title: Using OSC in Pure Data
.. slug: using-osc-in-pure-data
.. date: 2020-11-05 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 3
.. link:
.. description:
.. type: text

Vanilla Only
------------

The default version of PD is referred to as *Vanilla*.
OSC can be used in Puredata without further packages,
by means of the ojects ``netsend``, ``oscformat`` and ``oscparse``.

Sending OSC
===========

.. figure:: /images/basics/pd-osc-send-vanilla.png
	    :width: 400


Receiving OSC
=============

.. figure:: /images/basics/pd-osc-receive-vanilla.png
	    :width: 400


------


Using Externals
----------------


Dependencies
============


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

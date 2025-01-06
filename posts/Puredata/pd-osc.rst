.. title: Using OSC in Pure Data
.. slug: using-osc-in-pure-data
.. date: 2020-11-05 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 10
.. link:
.. description:
.. type: text

Vanilla Only
------------


Sending OSC
===========

The default version of PD is referred to as *Vanilla*.
OSC can be used in Puredata without further packages,
by means of the ojects ``netsend``, ``oscformat`` and ``oscparse``.
The patch `osc-send-vailla.pd <https://raw.githubusercontent.com/anwaldt/computer-music-basics/main/puredata/osc-send-vanilla.pd>`_
sends a message to port ``6666`` on the localhost (``127.0.0.1``). The message has the following structure and contains
one float argument:

.. code-block::

	/oscillator/frequency/ [float]


----


.. figure:: /images/basics/pd-osc-send-vanilla.png
	    :width: 400


----

Receiving OSC
=============


The corresponding receiver patch
`osc-receive-vanilla.pd <https://raw.githubusercontent.com/anwaldt/computer-music-basics/main/puredata/osc-receive-vanilla.pd>`_
listens on port ``6666``.
Using the ``route`` object, the message is unwrapped until
the single float argument can be processed by the number box:

.. figure:: /images/basics/pd-osc-receive-vanilla.png
	    :width: 400


------


.. admonition:: Exercise

    Send messages between the patches. If possible, use two computers	and change the address in the send patch.


Using Externals
----------------


Dependencies
============


Sending OSC
===========


The following example is based on additional externals.
For using them, install the external ``mrpeach`` with
the Deken tool inside Puredata: https://puredata.info/docs/Deken
The send patch uses the hostname ``localhost`` instead of an IP address.
The path  ``/oscillator/frequency``
of the OSC message has been defined arbitrarily -
it has to match between client and receiver.
Before sending OSC messages, the ``connect`` message
needs to be clicked.


.. figure:: /images/basics/pd-osc-send.png
	    :width: 400


-----

Receiving OSC
=============

Before receiving OSC messages, the ``udpreceive`` object
needs to know which  port to listen on.
Messages are then unpacked and routed according
to their path, using the ``routeOSC`` object.

.. figure:: /images/basics/pd-osc-receive.png
	    :width: 400

-----

.. admonition:: Exercise

		Use both patches for a remote controlled oscillator. If possible, use two computers	and change the address in the send patch.



------


References
----------

.. publication_list:: bibtex/visual-programming.bib
	   :style: unsrt

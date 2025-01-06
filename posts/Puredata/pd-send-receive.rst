.. title: Pure Data: Send-Receive & Throw-Catch
.. slug: puredata-send-receive
.. date: 2020-11-05 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 6
.. link:
.. description:
.. type: text


Send & Receive
--------------


Control Rate
============

Send and receive objects allow a *wireless* connection of both control and audio signals.
The objects are created with ``send`` and ``receive``  or short ``s`` and ``r`` for control rate signals and get one argument - a string labeling the connection.

Local Sends
~~~~~~~~~~~

Prepending a ``$0-`` to a send label turns it into a local connection. These are only valid inside a patch and its subpatches but not across different abstractions. The example ``send-receive-help.pd`` shows the difference between local
and global sends when used in both cases.
It relies on the additional abstraction ``send-receive.pd`` which needs to be in the same directory:


.. figure:: /images/basics/pd-send-receive.png
	:width: 600px
	:figwidth: 100%
	:align: center

*Send and receive of control signals with subpatch and abstraction.*

|

The inside of both the subpatch and the abstraction are identical:

.. figure:: /images/basics/pd-send-receive-sub.png
	:width: 400px
	:figwidth: 100%
	:align: center


*Inside of send-receive and the subpatch.*

-----

Audio Rate
==========

Audio send and receives follow the same rules as control ones.
They are created with an additional ``~``, as usual for audio objects.
The example ``send-receive-audio.pd`` shows the use of these buses:

.. figure:: /images/basics/pd-send-receive-audio.png
	:width: 500px
	:figwidth: 100%
	:align: center

*Send and receive of audio signals with subpatch and abstraction.*

-----

Throw & Catch
-------------

Throw and catch are bus extensions of the above introduced send-receive method, only for audio signals. Unlike with ``s~`` and ``r~``, it is possible to send multiple signals to one ``catch~``. This allows a flexible audio routing and grouping without a lot of lines. The example `throw-catch.pd <https://raw.githubusercontent.com/anwaldt/computer-music-basics/main/puredata/throw-catch.pd>`_ *throws* four sine waves to a common bus for a minimal additive synthesis:

.. figure:: /images/basics/pd-throw-catch.png
	:width: 400px
	:figwidth: 100%
	:align: center

*Using throw and catch to merge four signals.*

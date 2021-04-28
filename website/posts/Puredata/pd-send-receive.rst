.. title: Pure Data: Send-Receive & Throw-Catch
.. slug: puredata-send-receive
.. date: 2020-11-05 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 4
.. link:
.. description:
.. type: text


Send & Receive
--------------


Control Rate
============

Send and receive objects allow a *wireless* connection of both
control and audio signals. The objects are created with ``send`` and ``receive``  or short ``s`` and ``r`` for control rate signals and get one argument - a string labeling the connection.

**Local Sends**

Prepending a ``$0-`` to a send label turns it into a local connection. These are only valid inside a patch and its subpatches but not across different abstractions:


.. figure:: /images/basics/pd-send-receive.png
	    :width: 500

*Send and receive of control signals with subpatch and abstraction.*

|


.. figure:: /images/basics/pd-send-receive-sub.png
	    :width: 400


*Inside of send-receive and the subpatch.*

-----

Audio Rate
==========

Audio send and receives follow the same rules as control ones.
They are created with an additional ``~``, as usual for audio projects:

.. figure:: /images/basics/pd-send-receive.png
	    :width: 500

*Send and receive of audio signals with subpatch and abstraction.*

-----

Throw & Catch
-------------

Throw and catch are bus extensions of the above introduced send-receive method, only for audio signals. Unlike with ``s~`` and ``r~``, it is possible to send multiple signals to one ``catch~``. This allows a flexible audio routing and grouping without a lot of lines:

.. figure:: /images/basics/pd-throw-catch.png
	    :width: 400

*Using throw and catch to merge four signals.*

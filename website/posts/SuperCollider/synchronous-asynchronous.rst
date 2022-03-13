.. title: SuperCollider: Synchronous vs Asynchronous
.. slug: synchronous-vs-asynchronous
.. date: 2021-04-10 10:40:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 10
.. link:
.. description:
.. type: text

The Problem
===========


Most examples in this class can not be run as a complete script.
They need to be evaluated line by line or block wise.
One reason for this is the difference between
synchronous and asynchronous execution. This problem is in detail explained in the SC guides: https://doc.sccode.org/Guides/Sync-Async.html
This site just gives a shorter answer.

Issues usually arise, when a command has been sent to the server
and following command depends on the completion of that action.
Examples can be the creation of nodes or the loading and filling
of buffers.
Running this simple block at once will result in an error. It creates a node
and does not wait for completion before it uses the ``.set()`` method.
The result is a ``FAILURE IN SERVER /n_set Node 1000 not found``:

.. code-block:: supercollider

    (

    // create white noise node with gain control
    ~test = {arg gain=1; WhiteNoise.ar(gain)}.play;

    // try to set the gain
    ~test.set(\gain, 0.1);

    )


----

A Solution
==========

There are several ways of dealing with the above introduced problem.
One solution is to wrap the code block in a ``Routine``, which allows
to control the order of execution. In the case of asynchronous tasks,
the command ``s.sync`` can be used inside a routine. It waits for the
sever to finish all asynchronous tasks and the below example works
without errors:

.. code-block:: supercollider

    (
    Routine({

    	// create white noise node with gain control
    	~test = {arg gain=1; WhiteNoise.ar(gain)}.play;

    	// wait for the server to finish all asynchronous tasks
    	s.sync;

    	// try to set the gain
    	~test.set(\gain, 0.1);

    }).play
    )

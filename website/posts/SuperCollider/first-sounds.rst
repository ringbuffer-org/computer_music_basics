.. title: First Sounds with SuperCollider
.. slug: first-sounds-with-supercollider
.. date: 2020-11-05 13:47:06 UTC
.. tags:
.. category: basics:supercollider
.. priority: 1
.. link:
.. description:
.. type: text


Boot a Server
=============

Synthesis and processing happens inside an SC server. So the first thing to do when creating sound with SuperCollider is to boot a server. The ScIDE offers menu entries for doing that. However, using code for doing so increases the flexibility. In this first example we will boot the default server. It is per default associated with the global variable ``s``:

.. code-block:: supercollider

   // boot the server
   s.boot;

-----

A First Node
------------

In the SC server, sound is generated and processed inside synth nodes.
These nodes can later be manipulated, arranged and connected.
A simple node can be defined inside a function curly brackets:

.. code-block:: supercollider

 // play a sine wave
 (
 {
     // calculate a sine wave with frequency and amplitude
     var x = SinOsc.ar(1000);

     // send the signal to the output bus '0'
     Out.ar(0, x);

 }.play;

 )


UGens
=====

Inside the synth node, the UGen (Unit Generator) ``SinOsc`` is used. UGens are the binary building blocks
for signal processing on the server. Most UGens can be used with audio rate (``.ar``) or control rate (``.kr``).

-----

In the ScIDE, there are several ways to get information on the active nodes on the SC server. The node tree can be visualized in the server menu options or printed from sclang, by evaluating:

.. code-block:: supercollider

    s.queryAllNodes

After creating just the sine wave node, the server will show the following node state:

.. code-block:: supercollider

  NODE TREE Group 0
     1 group
        1001 temp__1

|

The GUI version of the node tree looks as follows. This representation is updated in real time, when left open:

.. figure:: /images/basics/sc-nodes-1.png
  :figwidth: 100%
  :width: 50%
  :align: center

.. note::

  The server itself does not know any variable names but   addresses all nodes by their ID. IDs are assigned in an ascending order. The sine wave node can be accessed with the ID ``1001``.

-----

Removing Nodes
==============


Any node can be removed from a server, provided its unique ID:

.. code-block:: supercollider

  s.sendMsg("/n_free",1003)


All active nodes can be removed from the server at once. This can be very handy when experiments get out of hand or a simple sine wave does not quit. It is done by pressing ``Shift + .`` or evaluating:

.. code-block:: supercollider

    // free all nodes from the server
    s.freeAll


Running SC Files
================

SuperCollider code is written in text files with the extensions ``.sc`` or ``.scd``. On Linux and Mac systems, a complete SC file can be executed in the terminal by calling the language with the file as argument:

 $ sclang sine-example.sc

The program will then run in the terminal and still launch the included GUI elements.

.. title: Combining Nodes in SuperCollider
.. slug: combining-nodes-in-supercollider
.. date: 2020-11-05 13:47:06 UTC
.. tags:
.. category: basics:supercollider
.. priority: 4
.. link:
.. description:
.. type: text



Creating and Connecting Nodes
-----------------------------

Audio buses can be used to connect synth nodes. In this example we will create two nodes -
one for generating a sound and one for processing it. First thing is an audio bus:

.. code-block:: supercollider

    ~aBus = Bus.audio(s,1);


|

The ``~osc`` node generates a sawtooth signal and the output is routed to the audio bus:

.. code-block:: supercollider

    ~osc = {arg out=1; Out.ar(out,Saw.ar())}.play;

    ~osc.set(\out,~aBus.index);


|

The second node is a simple filter. Its input is set to the index of the audio bus:

.. code-block:: supercollider

    ~lpf = {arg in=0; Out.ar(0, LPF.ar(In.ar(in),100))}.play;

    ~lpf.set(\in,~aBus.index);


.. warning::

    Although everything is connected, there is no sound at this point.
    SuperCollider can only process such chains if the nodes are arranged in the
    right order. The filter node can be moved after the oscillator node:

-----

Moving Nodes
------------

.. figure:: /images/basics/sc-order-1.png
    :width: 400

    *Node Tree before moving the processor node.*

|


The ``moveAfter()`` function is a quick way for moving a node directly after
a node specified as the argument. The target node can be either referred to by
its node index or by the related name in sclang:

.. code-block:: supercollider

    ~lpf.moveAfter(~osc)

|



.. figure:: /images/basics/sc-order-2.png
    :width: 400

    *Node Tree after moving the processor node.*

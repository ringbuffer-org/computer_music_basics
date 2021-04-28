.. title: Using Buses in SuperCollider
.. slug: using-buses-in-supercollider
.. date: 2020-11-05 13:47:06 UTC
.. tags:
.. category: basics:supercollider
.. priority: 6
.. link:
.. description:
.. type: text


Control Rate vs Audio Rate
==========================

SC works with two internal signal types or rates.
When something is used with the extension ``.ar``,
this refers to audio signals (audio rate),
whereas ``.kr`` uses the control rate.
For both rates, buses can be created.


-----



Creating  Buses
===============

An audio bus with a single channel is created on the default server ``s``
with the following command:

.. code-block:: supercollider

  ~aBus = Bus.audio(s,1);


|

A control bus with a single channel is created on the default server ``s``
with the following command:

.. code-block:: supercollider

  ~cBus = Bus.control(s,1);



------


Bus Indices
===========

The variable ``~aBus`` is the client-side representation of the Bus.
The server only knows it by its bus index. Bus indices are counted upwards
and can be queried with the following command:

.. code-block:: supercollider

  ~aBus.index
  ~cBus.index


-----

Monitoring Buses
----------------

Any bus can be monitored with the builtin scope with the following command.
The first argument defines the number of buses to be shown, the second
the index of the first buses:


.. code-block:: supercollider

    s.scope(1,~aBus.index,rate:'audio')


|

There is a short version, which has limitations and does not specify the bus type:

.. code-block:: supercollider

    ~aBus.scope()



----

Control Buses
=============


This simple sawtooth node will be used for showing how to use control buses.
It has one argument ``freq``, which affects the fundamental frequency
and uses the first hardware output:

.. code-block:: supercollider

  ~osc  = {arg freq=100; Out.ar(0,Saw.ar(freq))}.play;


----


Mapping a Control Bus
---------------------


The ``map()`` function of a node can connect a control bus,
identified by its index, with a node parameter:

.. code-block:: supercollider

  ~osc.map(\freq,~cBus.index);


----


Setting a Control Bus
---------------------

After mapping the bus, the synth stops its sound., since the
control bus is still set to the default value 0. This can be
visualized with the scope command.
A simple and quick way for changing the control bus to a
different value is the ``set()`` function of a node.
It can be used for all arguments of the node which are
internally used for control rates:

.. code-block:: supercollider

  ~cBus.set(50);

----

Multichannel Buses
==================

Both control and audio rate buses can be created as multi channel buses.
A scope will automatically show all channels. Individual channels can be
mapped with an offset in relation to the index of the first channel.
The ``setAt()`` function can be used for changing individual channel values:

.. code-block:: supercollider

  ~mBus = Bus.control(s,8);

  ~mBus.scope;

  ~osc.map(\freq,~mBus.index+3);

  ~mBus.setAt(3,150);

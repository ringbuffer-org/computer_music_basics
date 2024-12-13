.. title: Using Buses in SuperCollider
.. slug: using-buses-in-supercollider
.. date: 2020-11-05 13:47:06 UTC
.. tags:
.. category: basics:supercollider
.. priority: 3
.. link:
.. description:
.. type: text


Control Rate vs Audio Rate
==========================

Buses can be used to route and group signals for prjects with a more complex signal flow.
SC works with two internal signal types: audio and control. This concept is also used in other computer music environments, such as PD or Max/MSP.
Control signals work at a lower sampling rate and are used to *control* parameters, whereas audio signals carry what is *audible*. Audio- and control-rate signals can not be mixed arbitrarely but there are ways to convert them.

This duality affects various aspects in SC. Many ``UGens`` (like signal generators and oscillators) can be used in both rates.
With the extension ``.ar`` they produce or process audio signals (at audio rate).
When used with ``.kr`` they operate at control rate.



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

The variable ``~aBus`` is merely the the client-side representation of the Bus.
The server only knows buses by their bus index.
Bus indices are counted upwards (for every new bus created in the language)
and can be queried with the following command:

.. code-block:: supercollider

  ~aBus.index
  ~cBus.index


-----

Reserved Audio Buses
--------------------

The indices of user-defined audio buses start counting after all output
an input buses. The number of input and output buses can be defined before
booting a server. The default setting uses 2 input and 2 output buses.

.. list-table:: Audio buses
   :widths: 25 25
   :header-rows: 1
   :align: center

   * - Indices
     - Audio Buses
   * - 0...1
     - Outputs
   * - 2...3
     - Inputs
   * - 4
     - First user-defined bus


The number of input and output buses can be queried after boot:

.. code-block:: supercollider

  s.options.numOutputBusChannels;
  s.options.numInputBusChannels;


-----



Monitoring Buses
================

Any bus can be monitored with the builtin scope with the following command.
The first argument defines the number of buses to be shown, the second
the index of the first bus:


.. code-block:: supercollider

    s.scope(1,~aBus.index,rate:'audio')


|

There is also a short version, which does not specify the bus type but uses a client-side object:

.. code-block:: supercollider

    ~aBus.scope()

    ~cBus.scope()


The standard bus meter in SC only scales from -2 to +2 and is not efficient for monitoring higher values.


-----


Audio Buses
===========

Audio Output
------------

Audio output was already used in the very first examples for
`creating a sound in SC </computer_music_basics/SuperCollider/first-sounds/>`_.
The UGen ``Out`` can be used at audio rate to output an audio signal to any bus by its index. With a stereo interface, this is the short version for sending a sine-wave to the left output/speaker:

.. code-block:: supercollider

  {Out.ar(0, SinOsc.ar(1000))}.play;

And to the right output/speaker:

.. code-block:: supercollider

  {Out.ar(1, SinOsc.ar(1000))}.play;


------


Audio Input
-----------

With ``In.ar()`` we can get the signal of any audio bus into a node on the sever. This will become interesting for routing signals between nodes and will be explored in the following chapters.

Most early stage applications will make use of the inputs from the audio interface (for microphones and instruments).
The ``SoundIn`` - ``UGen`` makes it convenient to access the audio input buses directly.
It is aware of the number of harware inputs and outputs and allows accessing all inputs directly with the input-index.
This node simply passes the first input (usually 'left') to the first output (also 'left'):

.. code-block:: supercollider

  {Out.ar(0,SoundIn.ar(0))}.play


Note that this is equivalent to using the proper offset with a regular audio input (which is more complicated, but can be more versatile in some cases):

.. code-block:: supercollider

  { Out.ar(0,In.ar(s.options.numOutputBusChannels))}.play



-----


Control Buses
=============



Setting a Control Bus
---------------------

A simple and quick way for changing the control bus on the language side
is the ``.set()`` function of a bus:

.. code-block:: supercollider

  ~cBus.set(1);


The effect is visible when monitoring the bus.


-----


Reading Control Buses in Nodes
------------------------------


Control buses can be read inside a node just like audio buses, using ``In.kr()``.
This simple sawtooth ``SynthDef`` will be used for showing how to use control buses as arguments. The first argument defines the output bus index.
The second argument ``freq_bus`` (defaulted to ``0``) is used inside an ``In.kr()``, reading the bus' value into the variable ``freq``.


.. code-block:: supercollider

  SynthDef(\saw,
  {
    arg out_bus, freq_bus;

    var freq = In.kr(freq_bus);
    Out.ar(out_bus, Saw.ar(freq));
  }).add;



When creating a node from the ``SynthDef``, we pass a bus or a bus index as initiation argument:

.. code-block:: supercollider

  ~saw = Synth(\saw,[\out_bus, 0, \freq_bus, ~cBus]);



The pitch of the sawtooth is now linked to the value of ``~cBus``.



----


Mapping a Control Bus
---------------------


Another way to use bus values inside a node is mapping.
Any input arguement of a node can be mapped to a control bus after it has been created.
This node does the same thing as the ``SynthDef`` above:


.. code-block:: supercollider

  ~osc =
  {
    arg freq = 100;
    Out.ar(0,Saw.ar(freq))
  }.play;


The ``map()`` function of a node can connect a control bus,
identified by its index, with a node parameter:

.. code-block:: supercollider

  ~osc.map(\freq,~cBus);


----


Control Bus Output
------------------

``Out.kr()`` can be used to output control-rate signals to arbitrary buses, just as outputs are used in the audio domain.
The following node creates a sinewave LFO with a center frequency of 100 Hz, a
modulation depth of 20 Hz and an LFO frequency of 1 Hz.
The control bus ``~cBus`` is used as the first argument of the ``Out.kr()``:

.. code-block:: supercollider

  ~mod =
  {
    |
    freq   = 1,
    center = 100,
    depth  =  20
    |
    Out.kr(~cBus, depth+(shift*SinOsc.ar(freq)));
    }.play;


If we have one of the above sawtooth synths running and connected to the control bus. the modulation will be effective immediately. Since all LFO parameters are arguments, we can change them now by setting node parameters:


.. code-block:: supercollider

    ~mod.set(\freq,3)
    ~mod.set(\depth,50)



----


Multichannel Buses
==================

Both control and audio rate buses can be created as multi channel buses by using the second creation argument:


.. code-block:: supercollider

  ~mc_Bus = Bus.control(s,8);
  ~ma_Bus = Bus.audio(s,8);

A scope will automatically show all channels. Individual channels can be
used in ``UGens``, set and mapped with an offset in relation to the index of the first channel of the bus.

Using the ``\saw`` SynthDef from above, we can now use any bus from those multichannel buses:

.. code-block:: supercollider

  ~saw = Synth(\saw,[\out_bus, ~ma_Bus.index+4, \freq_bus, ~mc_Bus.index+5]);

We are now sending the audio output to an internal SC bus.
It is thus not audible, but can be checked with the scope:


.. code-block:: supercollider

  ~ma_Bus.scope


To change a single channel in a multichannel bus, use ``setAt()``.
The first argument defines the offest (channel index) - the second one the value:

.. code-block:: supercollider

  ~mc_Bus.setAt(5,1)


In a similar way, we can get all values from the multichannel bus:


.. code-block:: supercollider

  ~mc_Bus.getn(8)

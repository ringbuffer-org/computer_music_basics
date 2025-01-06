.. title: Using Arrays in SuperCollider
.. slug: using-arrays-in-supercollider
.. date: 2021-04-10 10:40:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 6
.. link:
.. description:
.. type: text



Simple Arrays
=============

In SC, arrays are collections of objects of any kind.
They can be defined and accessed using brackets:

.. code-block:: supercollider

  // define simple arrays:
  a = [0,1,2,3];
  b = [0,1,2,"last_value"];

  // access indices:
  a[3];


-----


Dynamic Creation
================

The array class offers numerous methods for creating
arrays, including ``fill()``:

.. code-block:: supercollider

  c = Array.fill(4,{arg i; 10/(i+1) });


-----


Arrays of Buses
===============

Especially in multichannel projects and larger mixing setups,
arrays of buses can be helpful. Make sure to boot the server to
actually use (scope) the buses:

.. code-block:: supercollider

    // an array of 16 buses, each with 4 channels:
    ~busArray = Array.fill(16,{Bus.control(s, 4)})

    // scope the second bus in the array:
    ~busArray[1].scope

    // set the third bus of the second bus in the array:
    ~busArray[1].setAt(2,0.5);


-----


Array of Nodes/UGens
====================

The same array approach can be used to generate multiple nodes,
for example sine waves at different frequencies and amplitudes:

.. code-block:: supercollider

    // an array of 16 sine oscillators:
    ~sineArray = Array.fill(16,{arg i;{SinOsc.ar(200*i)}.play})


------


Array of Synths
===============

The previous example can also be used with SynthDefs,
which is a good starting point for additive synthesis:

.. code-block:: supercollider

    // a simple synthdef
    (
    SynthDef(\sine,
    {|f = 100, a = 1|

       Out.ar(0, a * SinOsc.ar(f));

    }).send(s);
    )

    ~busArray = Array.fill(16,{arg i;Synth.new(\sine,[f:200*(i+1),a:0.2])})


.. warning::

    The second argument of *fill* has to be a function in curly brackets. If not, the array will contain multiple pointers to the same object (try)!

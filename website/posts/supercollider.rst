.. title: SuperCollider
.. slug: supercollider
.. date: 2020-11-05 13:47:06 UTC
.. tags: 
.. category: basics:languages
.. priority: 2
.. link: 
.. description: 
.. type: text


Supercollider (SC) is a server-client-based 
tool for sound synthesis and composition.
SC was started by James McCartney in 1996 and
is free software since 2002.
It can be used on Mac, Linux and Windows
systems and comes with a large collection
of community-developed extensions.
The client-server pronciple makes it a powerful
tool for distributed and embedded systems,
allowing the full remote control of synthesis processes
and live coding.

Getting Started
---------------

Binaries, source code and build or installation
instructions can be found at the SC github site.
If possible, it is recommended to build the latest
version from the repository:

https://supercollider.github.io/download


Code snippets in this example are taken from the
accompanying repository: 


sclang
======

``sclang`` is the SuperCollider language.
It represents the client side when working with
SC. It can  for example be started in a terminal by running:

 $ slang

The terminal will then change into ``sclang``  mode
and SC commands can be entered:

 sc3> 


SuperCollider code is written in text files with the
extensions ``.sc`` or ``.scd``.
On Linux and Mac systems, a complete SC file can
be executed in the terminal by calling the language
with the file as argument:

 $ slang sine-example.sc

The program will then run in the background or
launch the included GUI elements.


Global variables are either single letters (``s`` is preserved for the server)
or start with a tilde: ``~var_name``).
Local variables, used in functions, need to be defined explicitly:

 var var_name;

 
SC works with two internal signal types.
When something is used with the extension ``.ar``,
this refers to audio signals (audio rate),
whereas ``.kr`` uses the control rate.

ScIDE
=====

Working with SC in the terminal is rather inconvinient.
The SuperCollider IDE (ScIDE) is the environment for
live coding in ``sclang``, allowing the control of the
SuperCollider language.
When editing ``.sc`` files in the ScIDE, they can be
executed as a whole.
Moreover, single blocks, respectively
single lines can be evaluated, which is the
standard way of using SC, especially when exploring
the possibilities.


Server
======

Synthesis and processing happens inside an SC server.
A server can be booted from the 

.. code-block:: cpp

   // boot the server
   s.boot;


Synth
=====

Inside the SC server, sound is usually generated
and processed inside Synths.

.. code-block:: cpp

 // Play a Synth
 (
 {
     // calculate a sine wave with frequency and amplitude
     var x = 100 * SinOsc.ar(1000);

     // send the signal to the output bus '0'
     Out.ar(0, x);

 }.play;

 )

SynthDefs are templates for Synths, which are
sent to a server:

.. code-block:: cpp

 // define a SynthDef and send it to the server
 (

 SynthDef(\sine_example,
 {
    // define arguments of the SynthDef
    |f = 100, a = 1|

    // calculate a sine wave with frequency and amplitude
    var x = a * SinOsc.ar(f);

    // send the signal to the output bus '0'
    Out.ar(0, x);

 }).send(s);

 )



 

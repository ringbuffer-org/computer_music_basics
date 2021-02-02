.. title: OSC: Open Sound Control
.. slug: open-sound-control
.. date: 2020-11-05 13:47:15 UTC
.. tags: 
.. category: basics:protocols
.. priority: 1
.. link: 
.. description: 
.. type: text

Open Sound Control (OSC) is the de facto standard
for exchanging control data between audio applications
in distributed systems and on local setups with
multiple components:
http://opensoundcontrol.org/introduction-osc


All programming languages and tools for computer
music offer means for using OSC and specific
solutions exist for data sonification:
http://opensoundcontrol.org/mapping-nonmusical-data-sound



OSC is based on UDP/IP protocol in a client-server way.
A server needs to be started for listening to messages
sent from a client. 
A typical OSC message consists of a path and arguments:

 /synthesizer/volume/ 0.5

The path is a string with slash-separated substrings.
Parameters can be integers, floats and strings.
Unlike MIDI, OSC offers only the
transport protocol but does not define a standard for
musical parameters.
Hence, the paths used for a certain software is
completely arbitrary and can be defined by the developers.

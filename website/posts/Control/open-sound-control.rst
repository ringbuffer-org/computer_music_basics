.. title: OSC: Open Sound Control
.. slug: open-sound-control
.. date: 2020-11-05 13:47:15 UTC
.. tags:
.. category: basics:control
.. priority: 1
.. link:
.. description:
.. type: text

`Open Sound Control <http://opensoundcontrol.org/>`_ (OSC) is the standard
for exchanging control data between audio applications
in distributed systems and on local setups with
multiple components.
Almost any programming language and environment for
computer music offers means for using OSC, usually builtin.


OSC is based on the UDP/IP protocol in a client-server paradigm.
A server needs to be started for listening to incoming messages
sent from a client. For bidirectional communication,
each participant needs to implement both a server and a client.
Servers start listening on a freely chosen port,
whereas clients send their messages to an arbitrary IP address and port.


The ports 0 to 1023 are reserved for common TCP/IP applications and can thus not be used in most cases.

----

OSC Messages
------------

A typical OSC message consists of a path and
an arbitrary number of arguments.
The following message sends a single floating point
value, using the path ``/synthesizer/volume/``:

.. code-block:: console

 /synthesizer/volume/ 0.5


The path can be any string with slash-separated sub-strings,
as paths in an operating system.
OSC receivers can sort the messages according to the path.
Parameters can be integers, floats and strings.
Unlike MIDI, OSC offers only the transport protocol but does
not define a standard for musical parameters.
Hence, the paths used for a certain software are
completely arbitrary and can be defined by the developers.

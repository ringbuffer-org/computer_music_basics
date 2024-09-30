.. title: Using JACK Audio
.. slug: using-jack-audio
.. date: 2020-11-05 10:47:15 UTC
.. tags:
.. category: basics:linuxaudio
.. priority: 1
.. link:
.. description:
.. type: text


The `JACK API <https://jackaudio.org/>`_ implements
an audio server, allowing the connection of various software clients and
hardware interfaces.
In short, it turns the whole system into a digital audio workstation (DAW).
It is the the standard way of working on Linux (pro) audio systems,
but is also available for Mac and Windows.
JACK needs a back end to connect to the actual audio hardware.
On Linux systems, this is usually *ALSA* (Mac uses *Core Audio* and Windows *ASIO*).

----

Starting a JACK Server
----------------------

A JACK server can be started via various graphical tools,
such as `QjackCtl <https://qjackctl.sourceforge.io/>`_ or
`Carla <https://kx.studio/Applications:Carla>`_.
Many audio programs also boot a JACK server o their own,
if launched.
The recommended way of starting a JACK server in our case is the
terminal, using the command ``jackd``. It takes several arguments.
The following line starts a server (in the background) with the ALSA interface named
*PCH*, using a sample rate of 48kHz and a buffer size of 128 samples.

.. code-block:: console

	$ jackd -d alsa -d hw:Gen -r 48000 -p 128 &


The above example works for the 4th Gen. Scarlett 4i4 interface. TO use a different audio interface, follow the steps below.

----

Finding ALSA Devices
--------------------

One way of finding the ALSA name of your interface
is to type the following command:

.. code-block:: console

	$ aplay -l

|

The output shows all ALSA capable devices, their name
listed after the ``card x:``. PCH is usually the default
onboard sound card:

.. code-block:: console

	**** List of PLAYBACK Hardware Devices ****
	card 0: HDMI [HDA Intel HDMI], device 3: HDMI 0 [HDMI 0]
	  Subdevices: 1/1
	  Subdevice #0: subdevice #0
	card 0: HDMI [HDA Intel HDMI], device 7: HDMI 1 [HDMI 1]
	  Subdevices: 1/1
	  Subdevice #0: subdevice #0
	card 0: HDMI [HDA Intel HDMI], device 8: HDMI 2 [HDMI 2]
	  Subdevices: 1/1
	  Subdevice #0: subdevice #0
	card 0: HDMI [HDA Intel HDMI], device 9: HDMI 3 [HDMI 3]
	  Subdevices: 1/1
	  Subdevice #0: subdevice #0
	card 0: HDMI [HDA Intel HDMI], device 10: HDMI 4 [HDMI 4]
	  Subdevices: 1/1
	  Subdevice #0: subdevice #0
	card 1: PCH [HDA Intel PCH], device 0: CX20751/2 Analog [CX20751/2 Analog]
	  Subdevices: 1/1
	  Subdevice #0: subdevice #0


----




Disable Autoconnect
-------------------

With default sessings, jackd will automatically connect most new clients with the system inputs and outputs.
In some cases (like in JackTrip network systems with many clients and specific connections) this should not happen.
Adding the arguments '-a a' to the above jackd command (before the devices) will prevent all autoconnect request


.. code-block:: console

	jackd -a a -d alsa -d hw:Gen -r 48000 -p 128 &


----



Connecting JACK Clients
-----------------------

With autoconnect disabled, we can still use qjackct or any other GUI tool to connect Jack clients.
As almost everything, JACK connections can be modified from the terminal.
All available JACK ports can be listed with the following command:

.. code-block:: console

	$ jack_lsp

Two ports can be connected with the following command:


.. code-block:: console

	$ jack_connect client1:output client2:input

Disconnecting two ports is done as follows:

.. code-block:: console

	$ jack_disconnect client1:output client2:input

-----

If possible, a GUI-based tool, such as QjackCtl, can be
more handy for connecting clients. It can be started via
the a Desktop environment or from the command line:

.. code-block:: console

	$ qjackctl

|



.. figure:: /images/basics/qjackctl_connect.png
    :width: 400

    QjackCtl with hardware connections and two clients.

----

Storing/Restoring Connections
-----------------------------

Several tools allow to store and restore JACK connections.
Some of them work in a dynamic way, detecting spawned clients
and connecting them accordingly.
Others just allow a single operation for restoring connections.


aj-snapshot
===========

The command line tool
`aj-snapshot <https://github.com/sreimers/aj-snapshot>`_ is automatically
installed alongside JACK. It can store and restore both JACK
and ALSA connections, which can be handy when working with MIDI
and is the most feature-rich and robust solution.

Once all connections are set, they can be stored to in an XML
file, specified by a single argument:

.. code-block:: console

	aj-snapshot connections.snap


The above stored connections can be restored with the flag ``-r``.
An additional ``x`` deletes all prior connections, thus restoring the
original state in the file:

.. code-block:: console

		aj-snapshot -xr connections.snap

The tool can also be started as a demon, looking for new clients
and setting the related connections:

.. code-block:: console

	aj-snapshot -d connections.snap

|

.. note::

	In some spatial audio projects, hardware devices and
	clients can have many a large number of ports.
	aj-snapshot does not handle that well and takes
	an excessive amount of time for deleting existing connections.


----

jmess
=====

`jmess <https://github.com/jacktrip/jmess-jack>`_ is another command line tool,
storing and restoring only JACK connections.
It does not come with a demon mode but is a lot faster than aj-snapshot.

----

jack-matchmaker
===============

`jack matchmaker <https://pypi.org/project/jack-matchmaker/>`_ is a Python-based
command line tool for dynamically restoring previously saved JACK connections.

----

QjackCtl Patchbay
=================

The `QjackCtl Patchbay <https://www.rncbc.org/drupal/node/76>`_ offers a graphical
solution for storing JACK and ALSA connections.
Once activated, it patches new clients dynamically.

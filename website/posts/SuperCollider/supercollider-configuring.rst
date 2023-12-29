.. title: Configuring the Server
.. slug: supercollider-configuring
.. date: 2022-04-25 10:00:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 14
.. link:
.. description:
.. type: text

Many application scenarios require specific server configurations.
The default server options can be adjusted accordingly.

-----


Multi IO
--------

The number of audio inputs and outputs can be defined before booting the server.
Especially in multichannel applications - like in spatial audio - this is necessary:


.. code-block:: supercollider

  s.options.numInputBusChannels  = 16;
  s.options.numOutputBusChannels = 48;

  // boot with options
  s.boot;

  // show all IO channels
  ServerMeter(s);

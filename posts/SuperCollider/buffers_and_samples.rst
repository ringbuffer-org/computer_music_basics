.. title: SuperCollider: Buffers & Samples
.. slug: buffer_and_samples
.. date: 2024-09-22 18:00
.. tags:
.. category: basics:supercollider
.. priority: 11
.. link:
.. description:
.. type: text


Buffers are a tool to hold data arrays on the server and can be used for recording, loading and playing audio files (`SC Documentation on Buffers <https://doc.sccode.org/Classes/Buffer.html>`_).

SuperCollider comes with a couple of builtin audio samples, which are used in most of the SC helpfiles and examples.
The following snippets work with extra audio samples that can be downloaded here:
`http://ringbuffer.org/download/audio/MFB-522/ <http://ringbuffer.org/download/audio/MFB-522/>`_
They need to be located in the current SC working directory.

-----

Reading Mono Files
------------------

The following code creates a client-side object `b`, that points to a buffer on the default server `s` - and loads the wav-file `kick_1.wav` into the buffer:

.. code-block:: supercollider

    b = Buffer.read(s, 'kick_1.wav');

When the wav-file has been read, we can get information on the buffer and the sample inside. Like nodes and buses, buffers are known to the server only by their index - the buffer number. We can query this buffer's number:


.. code-block:: supercollider

    b.bufnum


There is more information we can get about the sample once it is loaded on the server:

.. code-block:: supercollider

    b.numChannels;
    b.sampleRate;
    b.numFrames;
    b.path;


------


Single Shot Sampler
-------------------


The sampled audio file in a buffer can be played with the `PlayBuf` UGen. Since the wav's sample rate and the sample rate of the SC server are not necessarily the same, we need to take care that the playback-rate is adjusted accordingly.
The buffer-to-server ration can be calculated in the language (`b.sampleRate/s.sampleRate`) or using a dedicated UGen:


.. code-block:: supercollider

    // PlayBuf args: numChannels, buffer (buffer number), rate
    x = {Out.ar(0, PlayBuf.ar(1, b, BufRateScale.kr(b))) }.play;


Note that the node remains on the server and needs to be freed with `x.free`.



-----

.. admonition:: Exercise


    Build a GUI with a button to fire a single shot sample.



.. title: Playing Samples in SuperCollider
.. slug: playing-samples-in-supercollider
.. date: 2021-05-02 10:40:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 9
.. link:
.. description:
.. type: text

The ``Buffer`` class manages samples in SuperCollider.
There are many ways to use samples, based on these buffers.
The following example loads a WAV file (find it in the download)
and creates a looping node. When running, the playback speed can be changed:


.. code-block:: supercollider

  s.boot;

  // get and enter the absolute path to a sample
  ~sample_path = "/some/directory/sala_formanten.wav";

  ~buffer  = Buffer.read(s,~sample_path);

  (
  ~sampler = {

  	|rate= 0.1|

  	var out = LoopBuf.ar(1,~buffer.bufnum, BufRateScale.kr(~buffer.bufnum) * rate, 1, 0,0,~buffer.numFrames);

  	Out.ar(0, out);

  }.play;

  )

  // set the play rate manually
  ~sampler.set(\rate,-0.1);


------

Exercise
========

.. admonition:: Exercise

		Combine the sample looper example with the control bus and mouse input example to create a synth for *scratching* sound files.

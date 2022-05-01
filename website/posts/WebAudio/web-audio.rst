.. title: Getting Started with Web Audio
.. slug: getting-started-with-web-audio
.. date: 2020-11-05 13:47:51 UTC
.. tags:
.. category: basics:webaudio
.. priority: 20
.. link:
.. description:
.. type: text
.. priority: 1

The `Web Audio API <https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API>`_
is a JavaScript based  API for sound synthesis and processing in web applications.
It is compatible to most browsers and can thus be used on almost any device.
This makes it a powerful tool in many areas. In the scope of this introduction it is
introduced as a means for data sonification with web-based data APIs and for
interactive sound examples.
Read the `W3C Candidate Recommendation <https://www.w3.org/TR/webaudio/>`_ for an in-depth documentation.


-----

The Sine Example
----------------


The following Web Audio example features a simple
sine wave oscillator with frequency control and a mute
button:

.. raw:: html
   :file: ../Computer_Music_Basics/webaudio/sine_example/sine_example.html


------

Code
====

Building Web Audio projects involves three components:

- HTML for control elements and website layout
- CSS for website appearance
- JavaScript for audio processing


Since HTML is kept minimal, the code is compact but
the GUI is very basic.


.. listing:: ../Computer_Music_Basics/webaudio/sine_example/sine_example.html html


-----

Links and More Examples
-----------------------

https://github.com/mdn/webaudio-examples

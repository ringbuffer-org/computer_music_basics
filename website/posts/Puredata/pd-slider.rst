.. title: Sliders in PD
.. slug: pd-sliders
.. date: 2022-04-28
.. tags:
.. category: basics:puredata
.. priority: 4
.. link:
.. description:
.. type: text


This very basic `sine.pd <https://raw.githubusercontent.com/anwaldt/computer-music-basics/main/puredata/sine.pd>`_ example creates a sine wave oscillator.
Its frequency can be controlled with a horizontal slider. Ann additional toggle object allows to switch
the sine on and of, by means of multiplication. When used without arguments, the ``dac~`` object has two inlets,
which relate to the left and right channel of the audio interface. The additional message box with the ``bang``
can be used to activate the DSP. This is necessary for getting any sound and can also be done in the menu.


.. figure:: /images/basics/pd-sine.png
    :width: 40%
    :figwidth: 100%
    :align: center


-----


References
----------

.. publication_list:: bibtex/visual-programming.bib
	   :style: unsrt

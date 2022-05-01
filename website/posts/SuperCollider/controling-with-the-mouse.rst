.. title: Controlling SC with the Mouse
.. slug: controlling-sc-with-the-mouse
.. date: 2020-11-05 13:47:06 UTC
.. tags:
.. category: basics:supercollider
.. priority: 6
.. link:
.. description:Exercise
.. type: text


A quick way of control is often needed
when testing and designing synthesis and processing algorithms
in SuperCollider. One quick way is to map the mouse position to
control rate buses. Combined with a touch display, this can even
be an interesting means for expressive control.
This example first creates a control bus with two channels.
The node ``~mouse`` uses the ``MouseX`` and ``MouseY`` UGens to
influence the two channels of this bus:

.. code-block:: supercollider

  // mouse xy controll with busses
  ~mouse_BUS = Bus.control(s,2);

  ~mouse   = {
    Out.kr(~mouse_BUS.index,   MouseX.kr(0,1));
    Out.kr(~mouse_BUS.index+1, MouseY.kr(0,1));
  }.play;


------

Exercise
========

.. admonition:: Exercise

		Use the mouse example with the previous `sawtooth-filter example </computer_music_basics/SuperCollider/combining-nodes-in-supercollider/>`_ to control pitch and filter characteristics.

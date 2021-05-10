.. title: Patches and Subpatches in Pure Data
.. slug: patches-and-subpatches-in-pure-data
.. date: 2020-11-05 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 3
.. link:
.. description:
.. type: text


Arguments
---------

The following examples are based on patches and additional files, called
abstractions. To make them work, all involved patches need to be located
in the same direction (by cloning the complete repository).
Arguments are passed to objects after the name, separated by a white space.
The patch ``arguments-help.pd`` shows this by creating an ``arguments`` object:

.. figure:: /images/basics/pd-arguments-1.png
	:width: 400


Inside an abstraction, individual arguments can be accessed with the ``$`` operator and
their index. The ``loadbang`` is executed on the object's creation, thus printing both
arguments on start. This is helpful for setting initial values in patches,
as shown in ``arguments-help``. Once created, it will print the arguments to the
main Pd window:

.. figure:: /images/basics/pd-arguments-2.png
	:width: 500



-----


Subpatches
----------

Subpatches can be very helpful for creating cleaner patches
without addtional abstractions and files.
To create a subpatch, use the object ``pd`` with an optional
string argument for naming the subpatch. They can be used like abstractions
but do not require an additional file.

----



Graph-on-Parent
===============

When toggling *Graph-on-Parent* in an object's properties, it can expose
GUI elements to its parent patch. This is a good way of cleaning your patch and
showing only what is needed in a performance situation. It works for both abstractions
and subpatches.
The example ``patches.pd`` makes use of this to create a filter subpatch with controls.
The left hand audio input of the suppatch is a fixed frequency sawtooth.
The right hand control input sets the Q of the filter.

.. figure:: /images/basics/pd-patches-1.png
	:width: 400

On the inside, the ``moog~`` object is used. It is not part of PD vanilla and can be installed
with the *flatspace ggee* extensions from Deken. The red rectangle marks the area visual in the
parent patch. All GUI components inside this area will be visible:


.. figure:: /images/basics/pd-patches-2.png
	:width: 400

-----

Inlets and Outlets
------------------

The patch has two inlets - one in audio rate (``inlet~``) and one in control rate -
and two outlets, also with audio rate (``outlet~``) and control rate.
For inlets and outlets, their horizontal order determines their order in the
object when patched from the parent. Changing them can mess up the complete patching.

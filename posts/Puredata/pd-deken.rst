.. title: Pure Data: Installing Externals with Deken
.. slug: installing-externals-with-deken
.. date: 2020-11-05 13:46:52 UTC
.. tags:
.. category: basics:puredata
.. priority: 5
.. link:
.. description:
.. type: text

The basic install of PD is referred to as *Vanilla*.
Although many things are possible with this plain version,
some additional libraries are very helpful and there is a handful which can be considered standard.


Find and Install Extensions
===========================

PD comes with *Deken*, a builtin tool for installing external libraries.
Deken can be opened from the menu of the PD GUI. On Linux installs it is located under
``Help->Find Externals``.
Deken lets you search for externals by name. The best match is usually found at the top of the results.
``cyclone`` is an example for a library with many useful objects:


.. figure:: /images/basics/pd-deken-1.png
	    :width: 400


----

Deken lets you select where to install externals in its *Preferences* menu.
Everything will be located in the specified directory afterwards.

-----

Add Libraries to Search Paths
=============================

Once installed, it may be necessary to add the individual libraries to the search paths.
This is done in an extra step. On Linux installs, this can be found under ``Edit->Preferences->Path``:

.. figure:: /images/basics/pd-deken-2.png
	    :width: 300

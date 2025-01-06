.. title: Extensions & Plugins for SuperCollider
.. slug: supercollider-extensions
.. date: 2022-04-25 10:00:00 UTC
.. tags:
.. category: basics:supercollider
.. priority: 16
.. link:
.. description:
.. type: text


sc3-plugins
===========

The sc3-plugins are a collection of unit generators (UGen),
developed by the SC community.
For using the full potential of SuperCollider, it is recommended to
install them alongside every SC install:

https://github.com/supercollider/sc3-plugins

The sc3-plugins also contain the SC-HOA UGens, which are needed for working
with binaural and Ambisonics in SC.



-----

Extensions
==========

Extra classes are organized in so called Quarks:

https://github.com/supercollider-quarks/quarks

Some addons for SuperCollider require plugins AND extensions.
Quarks can be added via code. This example shows how to install the
SC-HOA quarks (https://github.com/florian-grond/SC-HOA):

.. code-block:: supercollider

  Quarks.install("SC-HOA")

  // SuperCollider will automatically install the Quarks here:
  Quarks.folder; // execute to see the directory


Another way is to use the Quarks GUI:

.. code-block:: supercollider

  Quarks.gui



.. warning::

    The sclang needs to be restarted after installing Quarks and extensions.
    When doing so, the class library gets recompiled and newly installed classes or unit
    generators are available.

----

After restarting sclang (recompiling the class library), you can check whether a Quark (SC-HOA)
has been installed properly by checking for related help files, which will be installed:

.. code-block:: supercollider

  HOAmbiPanner.help

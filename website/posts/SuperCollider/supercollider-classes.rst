.. title: Create Classes in SuperCollider
.. slug: create-classes-in-supercollider
.. date: 2021-04-10 10:40:00 UTC
.. tags:
.. category: basics:supercollider-development
.. priority: 9
.. link:
.. description:
.. type: text
.. priority: 1


At its core, SuperCollider works in a strictly object oriented way.
Although SynthDefs already allow to work with multiple instances of a
definition, actual classes can help in many ways.
This includes the typical OOP paradigms, such as member variables and methods
for quick access to properties and actions.

----


Where to put SC Classes
-----------------------

While SynthDefs can be sent to a server during run time,
classes are compiled when booting the interpreter or recompiling
the class library.
SuperCollider classes are defined in ``.sc`` files with a specific structure.
For compiling a class when booting the interpreter, it needs to be located in
a directory which is scanned by SC. For this reason, an installation of SC
creates a directory for user-defined content. Inside ``sclang``, this directory can
be shown with the following command:

.. code-block:: SuperCollider

  Platform.userExtensionDir

On Linux systems, this is usually:

.. code-block:: SuperCollider

  /home/someusername/.local/share/SuperCollider/Extensions

For more information, read the `SC documentation on extensions <https://doc.sccode.org/Guides/UsingExtensions.html>`_.

-----

Structure of SC Classes
-----------------------

The following explanations are based on the example 
A class is defined inside brackets, with the class name:

.. code-block:: SuperCollider

  SimpleSynth
  {
    ...
  }


Creating Help Files
-------------------

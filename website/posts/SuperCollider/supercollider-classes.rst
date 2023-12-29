.. title: Create Classes in SuperCollider
.. slug: create-classes-in-supercollider
.. date: 2021-04-10 10:40:00 UTC
.. tags:
.. category: basics:supercollider-development
.. priority: 11
.. link:
.. description:
.. type: text
.. priority: 1


At its core, SuperCollider works in a strictly object oriented way.
Although SynthDefs already allow to work with multiple instances of a
definition, actual classes can help in many ways.
This includes the typical OOP paradigms, such as member variables and methods
for quick access to properties and actions.

While SynthDefs can be sent to a server during run time,
classes are compiled when booting the interpreter or recompiling
the class library. Some possible errors in class definitions are
detected and reported by the compiler.

This is just a brief overview, introducing the basic principles.
Read the  `SC documentation on writing classes <https://doc.sccode.org/Guides/WritingClasses.html>`_
for a detailed explanation.

----


Where to put SC Classes
-----------------------

SuperCollider classes are defined in ``.sc`` files with a specific structure.
For compiling a class when booting the interpreter, it needs to be located in
a directory which is scanned by SC. For this reason, an installation of SC
creates a directory for user-defined content. Inside ``sclang``, this directory can
be shown with the following command:

.. code-block:: supercollider

  Platform.userExtensionDir

On Linux systems, this is usually:

.. code-block:: console

  /home/someusername/.local/share/SuperCollider/Extensions

For more information, read the `SC documentation on extensions <https://doc.sccode.org/Guides/UsingExtensions.html>`_.

-----

Structure of SC Classes
-----------------------

The following explanations are based on the `example in the repository <https://github.com/anwaldt/computer-music-basics/blob/master/supercollider/classes/SimpleSynth.sc>`_.
A class is defined inside brackets, with the class name:

.. code-block:: supercollider

  SimpleSynth
  {
    ...
  }

----

Member Variables
================

Member variables are declared in the standard way for local variables.
They can be accessed anywhere inside the class.

.. code-block:: supercollider

  var dur;


----

Constructor and Init
====================

The constructor calls the ``init()`` function in the
following way for initializing values and other tasks on
object creations:

.. code-block:: supercollider

	// constructor
	*new { | p |
		^super.new.init(p)
	}

	// initialize method
	init { | p |
		dur    = 1;
	}


----


Member Functions
================

Member functions are defined as follows, using either the ``|...|`` or the ``arg ...;``
syntax for defining their arguments:

.. code-block:: supercollider

  play
  	{ | f |
      ...
    }

-----


Creating Help Files
-------------------

In SC, help files are integrated into the SCIde for quick access.
Help files for classes are also created during compilation.
They need to be placed in a directory relative to the ``.sc`` file
with the extension ``.schelp``:

.. code-block:: console

    HelpSource/Classes/SimpleSynth.schelp

Read the
`SC documentation on help files <http://doc.sccode.org/Guides/WritingHelp.html>`_
for more information.

.. title: Getting Started with SuperCollider
.. slug: getting-started-with-supercollider
.. date: 2020-11-05 13:47:06 UTC
.. tags:
.. category: basics:supercollider
.. priority: 0
.. link:
.. description:
.. type: text


Supercollider (SC) is a server-client-based tool for sound synthesis and composition.
SC was started by James McCartney in 1996 and is free software since 2002.
It can be used on Mac, Linux and Windows systems and comes with a large collection
of community-developed extensions.
The client-server principle aims at live coding and makes it a powerful
tool for distributed and embedded systems,
allowing the full remote control of synthesis processes.

There are many ways of approaching SuperCollider, depending on the
intended use case. Some tutorials focus on sequencing, others on live coding
or sound design.
This introduction aims at programming remotely controlled synthesis and processing
servers, which involves signal routing and OSC capabilities.

-----

Getting SC
----------

Binaries, source code and build or installation
instructions can be found at the SC GitHub site.
If possible, it is recommended to build the latest
version from the repository:

https://supercollider.github.io/download

SuperCollider comes with a large bundle of help files and code examples
but first steps are usually not easy.
There are a lot of very helpful additional resources,
providing step by step introductions.

- `The SuperCollider tutorial <https://composerprogrammer.com/teaching/supercollider/sctutorial/tutorial.html>`_

- `The SuperCollider Book  <https://mitpress.mit.edu/books/supercollider-book>`_


Code snippets in this example are taken from the
accompanying repository:  `SC Example <https://gitlab.tubit.tu-berlin.de/henrikvoncoler/computer-music-basics/blob/master/supercollider/sine-example.sc>`_.
You can simple copy and paste them into your editor.

-----

SC Trinity
----------

SuperCollider is based on a client-server paradigm.
The server is running the actual audio processing,
whereas clients are used to control the server processes
via OSC messages.
Multiple clients can connect to a running server.
The dedicated ScIDE allows convenient features for
live coding and project management:


.. figure:: /images/basics/supercollider-components.png
    :width: 400
    :align: center

    Server, client and ScIDE.

----

sclang
======

``sclang`` is the SuperCollider language.
It represents the client side when working with
SC. It can for example be started in a terminal by running:

.. code-block:: console

 $ sclang


|

Just as with other interpreted languages, such as
Python, the terminal will then change into ``sclang``  mode.
At this point, the class library is complied,
making all SC classes executable.
Afterwards, SC commands can be entered:

.. code-block:: console

 sc3>  postln("Hello World!")


-----

ScIDE
=====

Working with SC in the terminal is rather inconvenient.
The SuperCollider IDE (ScIDE) is the environment for
live coding in ``sclang``, allowing the control of the
SuperCollider language:

.. thumbnail:: /images/basics/scide.png

  *ScIDE*


|

When booting the ScIDE, it automatically launches sclang
and is then ready to interpret.
Files opened in the IDE can be executed as a whole.
Moreover, single blocks, respectively
single lines can be evaluated, which is especially
handy in live coding, when exploring possibilities or prototyping.
In addition, the IDE features tools for monitoring various
server properties.

----

Some Language Details
---------------------

Variable Names
==============

Global variables are either single letters - ``s`` is preserved for the
default server - or start with a tilde: ``~varname``).
Local variables, used in functions, need to be defined explicitly:

.. code-block:: supercollider

 var foo;

----

Evaluating Selections
=====================

- Individual sections of code can be evaluated by selecting
  them and pressing ``Control + Enter``.

- Single lines of code can be evaluated by placing the cursor and
  pressing ``Shift + Enter``

-----

Parentheses
===========

Parentheses can help structuring SC code for live programming.
Placing the cursor inside a region between parentheses and
pressing ``Control + Enter`` evaluates the code inside the parentheses.

.. code-block:: supercollider

  (
	post('Hello ');
	postln('World!');
  )

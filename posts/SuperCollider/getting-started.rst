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

https://supercollider.github.io/downloads

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
  :figwidth: 100%
  :width: 60%
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

.. figure:: /images/basics/scide.png
  :figwidth: 100%
  :width: 60%
  :align: center

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



Parentheses
===========

Parentheses can help structuring SC code for live programming.
Placing the cursor inside a region between parentheses and
pressing ``Control + Enter`` evaluates the code inside the parentheses.
This way of coding is not suited for scripts which are executed as one.

.. code-block:: supercollider

  (
	post('Hello ');
	postln('World!');
  )


------


Variable Names
==============

Global variables are either single letters - ``s`` is preserved for the
default server - or start with a tilde: ``~varname``). They can be declared
and used anywhere in a language instance.
The first letter of tilde variables must be lowercase.
Local variables, used in functions or code blocks, need to be defined explicitly:

.. code-block:: supercollider

  // single-letter-global variable:
  x = 1.0;

  // tilde-global variables:
  ~aValue = 1.1;

  // local variable:
  var foo;


Declare First
~~~~~~~~~~~~~

All declarations of local variables must happen in the beginning of a function or block.
The following example throws an error:

.. code-block:: supercollider

  (
  var xValue = 1.0;

  xValue.postln;

  var yValue = 2.1;
  )


----

Evaluating Selections
=====================

Some of the examples in the SC section of this class are in the repository,
whereas other only exist as snippets on these pages.
In general, all these examples can be explored by copy-pasting the
code blocks from the pages into the ScIDE.
They can then be evaluated in blocks or line-wise
but can not be executed as complete files.
This is caused by the problem of synchronous vs asynchronous processes,
which is explained later: `Synchronous vs Asynchronous </SuperCollider/synchronous-vs-asynchronous/>`_

These features help to run code in the ScIDE subsequently:


- Individual sections of code can be evaluated by selecting
  them and pressing ``Control + Enter``.

- Single lines of code can be evaluated by placing the cursor and
  pressing ``Shift + Enter``


-----

Functions
=========


Functions in SC are defined inside curly brackets.
Arguments can are declared in the very beginning.
Once created, a function is used by calling the ``.value()`` method:

.. code-block:: supercollider

    (
    ~poster = {

    	arg a,b;

    	var y = a+b;

    	y.postln;

    };
    )

    ~poster.value(1,1);


Arguments can also be defined inside pipes:

.. code-block:: supercollider

    ~poster = {

    	|a,b|

    	a.postln;

    };

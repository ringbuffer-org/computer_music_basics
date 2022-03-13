.. title: Working with Groups
.. slug: working-in-groups
.. date: 2020-11-05 13:47:06 UTC
.. tags:
.. category: basics:supercollider
.. priority: 5
.. link:
.. description:
.. type: text


Creating Groups
---------------

Groups - or group nodes - can be a very useful concept
for keeping track of the signal flow.
Without any further actions, all nodes are placed in the default
Group ``1``. Additional groups can be arranged regarding the
order of execution.
A new group can be added from ``sclang`` as follows:

.. code-block:: supercollider

    ~g1 = Group.new();


------

Relative Group Positions
------------------------

As with nodes, further groups can be added in relation
to existing groups. The following action makes sure that a new group
will be placed *after* the previously defined group:

.. code-block:: supercollider

  ~g2 = Group.after(~g1);


-----

Nested Groups
-------------

Groups can contain other groups, allowing a hierarchical
structure of nodes:

.. code-block:: supercollider

  ~g3 = Group.head(~g2);


-----

More on Groups
--------------


The group object allows many more actions. They are listed in the
`SC documentation on groups <http://doc.sccode.org/Classes/Group.html>`_.
After adding another group ``before`` the third one

.. code-block:: supercollider

  ~g4 = Group.before(~g3);


|

the server node structure looks as follows:


.. figure:: /images/basics/sc-group-nodes.png
	    :width: 400


The server does not know the
groups by their variable names in ``sclang``. Hence they are numerated.
Node indices - or IDs -  of groups can be assessed from the language:


.. code-block:: supercollider

  ~g1.nodeID;
  ~g2.nodeID;
  ~g3.nodeID;
  ~g4.nodeID;

-----


Exercise
========

.. admonition:: Exercise

		Use groups to sort the nodes from the example in the section on `Combining Nodes </SuperCollider/combining-nodes-in-supercollider/>`_

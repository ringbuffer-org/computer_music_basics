.. title: A Brief History
.. slug: a-brief-history
.. date: 2020-11-05 13:47:15 UTC
.. tags:
.. category: basics:introduction
.. priority: 1
.. link:
.. description:
.. type: text
.. priority: 2


Beginnings of Computer Music
----------------------------

First experiments on digital sound creation took place 1951 in  Australia, on the  `CSIRAC <https://cis.unimelb.edu.au/about/csirac/music/music.html>`_ computer system.


Besides from these experiments, digital sound synthesis dates back to the first experiments of Max Mathews at Bell Labs
in the mid 1950s. Mathews created the MUSIC I
programming language for generating musical
sounds through synthesis of a single triangular  waveform on an IBM 704.
*The Silver Scale*, realized by psychologist Newman Guttman in 1957, is one of the first ever digitally synthesized piece of music (Roads, 1980).

.. youtube:: PM64-lqYyZ8
	  :width: 500

----


MUSIC and its versions (I, II, III, ...)
are direct or indirect ancestors to most
recent languages for sound processing.
Mathews defined the building blocks for digital sound synthesis and processing in these frameworks (Mathews, 1969, p. 48).
This concept of *unit generators* is still used today.
Although the first experiments sound amusing
from today's perspective, he already anticipated the
potential of the computer as a musical instrument:

    *“There are no theoretical limitations to the performance of the computer as a source of musical sounds, in contrast to the performance of ordinary instruments.”* (Mathews, 1963)



Mathews created the first digital musical
pieces himself, but in order to fully explore the musical
potential, he was joined by composers, artists and other
researchers, such as Newman Guttman, James Tenney
and Jean Claude Risset.
Risset  contributed to the development of electronic music
by exploring the possibilities of spectral analysis-resynthesis (1:20)
and psychoacoustic phenomena like the Shepard tone (4:43):


.. youtube:: RcX0ubvoZUA
	  :width: 500

------

Later, the Bell Labs were visited
by many renowned composers of various styles genres, including
John Cage, Edgard Varèse and Laurie Spiegel (Park, 2009).
The work at Bell Labs will be in focus again in the
`section on additive synthesis </Additive_Spectral/spectral-history/>`_.

-----

A Pedigree
==========

The synthesis experiments at Bell Labs are the origin of most music programming languages and methods for digital sound synthesis.
On different branches, techniques developed from that seed (Bilbao, 2009):


.. figure:: /images/basics/bilbao_history.png
	    :width: 800

-----

The following family tree focuses on the tools used in this class and is thus without any claim to completeness:

.. figure:: /images/basics/computer_music_pedegree.png
	    :width: 800

-----

Chowning & CCRMA
----------------

The foundation for many further developments was
laid when John Chowning brought the software MUSIC VI
to Stanford from a visit at Bell Labs in the 1060s.
After migrating it to a *PDP-6* computer,
Chowning worked on his groundbreaking digital compositions,
such as *Turenas (1972)*, using the frequency modulation synthesis (FM) and spatial techniques. Although in particular known for discovering the FM synthesis, these works are far more than mere studies of technical means:

.. youtube:: kSbTOB5ft5c
	  :width: 500


-----

Puckette & IRCAM
----------------


Most of the active music programming environments, such as Puredata, Max/MSP, SuperCollider or CSound, are descendants of the MUSIC languages. Graphical programming languages like Max/MSP
and Puredata were actually born as patching and mapping environments.
Their common ancestor, the Patcher (Puckette, 1986; Puckette, 1988), developed by Miller Puckette at IRCAM in the 1980s,
was a graphical environment for connecting MAX real-time processes and for controlling MIDI instruments.

The new means of programming and the increase in computational power allowed *musique mixte* with digital signal processing means. *Pluton* (1988-89) by Philippe Manoury is one of the first pieces to use MAX for processing piano sounds in real time (6:00-8:30):

.. youtube:: W9xjcOrl-kk
	  :width: 500

-----

Links
-----

`120 Years of Electronic Music <http://120years.net/>`_ is a very thorough site on history and development of electronic musical instruments.

A talk by  Paul Davis (Jack, Ardour) on the development of open source audio:

.. youtube:: dk2AMwc4e2k
	  :width: 500



-----

References
----------

.. publication_list:: bibtex/synthesis_overview.bib
	   :style: unsrt

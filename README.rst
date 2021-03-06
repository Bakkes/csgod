csgod
=====

csgod monitors an instance of Counter-Strike: Global Offensive and hooks onto in-game events. Handlers can be easily written and hooked onto the provided events.

Features
--------

- Monitors a CS:GO process for events e.g. match start, player connect, map change.
- Allows registration of handlers for these events.
- ...more to come

Notes
-----

Modifies the valve.rc file. One command is appended (along with a safely removable comment) but can be moved to any valid place within the file.

Installation
------------

A `binary distribution`_ is available.

Execution from source requires Python 3 and `Python for Windows Extensions`_.

.. _binary distribution: http://magp.io/projects/csgod/home.html
.. _Python for Windows Extensions: http://sourceforge.net/projects/pywin32/


Documentation
-------------

View the `documentation on my site`_.

.. _documentation on my site: http://magp.io/projects/csgod/documentation/home.html
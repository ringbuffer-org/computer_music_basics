.. title: Python and MediaPipe Setup
.. slug: mediapipe-setup
.. date: 2025-10-19 10:00:00
.. tags:
.. category: basics:interactive
.. priority: 2
.. link: basics:interactive:mediapipe-setup
.. description:
.. type: text




This page helps you set up `Python <https://www.python.org/>`_ with `MediaPipe <https://chuoling.github.io/mediapipe/>`_ and `OSC capacities <https://pypi.org/project/python-osc/>`_ for interactive systems based on computer vision.
Together, these components allow a wide range of applications.
A proper setup is necessary to avoid conflicts.

----


Python Version
==============

MediaPipe works with **Python versions 3.8–3.12**.
To get the installed Python version, type the following into your terminal:

.. code-block:: bash

   $ python3 --version


The output will provide the installed version (e.g. **Python 3.12.3**)


Getting the Right Python Version
--------------------------------

If your Python is too old (<3.8) or too new (≥3.13), install or switch to a compatible version.
**Recommended versions:** 3.10 - 3.12 (stable and widely supported).
The following sections show the steps for the most common operating systems.

**Windows**
~~~~~~~~~~~

1. Uninstall older versions if needed from *Add or Remove Programs*.
2. Download the 64-bit installer from:
   https://www.python.org/downloads/windows/
3. During installation:
   - Tick *Add Python to PATH*
   - Under *Customize installation*, ensure *pip* and *venv* are selected.
4. Open a new PowerShell or Command Prompt and verify:


   .. code-block:: bash

      $ python --version

**macOS**
~~~~~~~~~

Option 1 – Use the official universal installer:

.. code-block:: bash

   open https://www.python.org/downloads/macos/

After installation, confirm:

.. code-block:: bash

   $ python3 --version

Option 2 – Use Homebrew (if installed):

.. code-block:: bash

      $ brew install python@3.11
      $ brew link python@3.11 --force --overwrite

**Linux**
~~~~~~~~~

On most systems you can install a supported version via package manager.

- **Ubuntu / Debian:**

.. code-block:: bash

     $ sudo apt update
     $ sudo apt install python3.12 python3.12-venv python3.12-distutils


Then explicitly use that version:

.. code-block:: bash

     $ python3.12 --version

- **Fedora:**

.. code-block:: bash

     $ sudo dnf install python3.11

- **Arch / Manjaro:**

.. code-block:: bash

     $ sudo pacman -S python


After installation, confirm the version again:

.. code-block:: bash

   $ python3 --version

-----


Check for pip
=============

pip is Python's package installer - we need it to install dependencies.
Make sure pip is available on your system:

.. code-block:: bash

      $ python3 -m ensurepip --default-pip


-----


Virtual Environment and Dependencies
====================================

We are using virtual environments to make sure we are using only the packages and versions we need for a specific project.
This avoids confusions with different installs.

First, verify that pip is available, by typing the following in the terminal:

.. code-block:: bash

   $ python3 -m venv --help

Create and activate a virtual environment - this step is the same for all operating systems:

.. code-block:: bash

   $ python3 -m venv cv2pd


To activate te venv on macOS/Linux, enter:

.. code-block:: bash

      $ source cv2pd/bin/activate

For Windows (PowerShell) type:

.. code-block:: powershell

      cv2pd\Scripts\activate   


You will see that your venv is activated when the terminal shows ``(cv2pd)``.


-----


Install Packages with pip
==========================

.. code-block:: bash

   $ pip install mediapipe opencv-python python-osc numpy

You can verify the install by typing:


.. code-block:: bash

   $ python -m pip list

You should see: opencv-python, numpy, python-osc




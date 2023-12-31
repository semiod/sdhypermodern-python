The Hypermodern Python Project
==============================
.. toctree::
   :hidden:
   :maxdepth: 1

   license
   reference
   
The example project for the
`sdHypermodern Python `_
article series.
The command-line interface prints random facts to your console,
using the `Wikipedia API <https://en.wikipedia.org/api/rest_v1/#/>`_.


Installation
------------

To install the Hypermodern Python project,
run this command in your terminal:

.. code-block:: console

   $ pip install sdhypermodern-python


Usage
-----

Hypermodern Python's usage looks like:

.. code-block:: console

   $ sdhypermodern-python [OPTIONS]

.. option:: -l <language>, --language <language>

   The Wikipedia language edition,
   as identified by its subdomain on
   `wikipedia.org <https://www.wikipedia.org/>`_.
   By default, the English Wikipedia is selected.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.
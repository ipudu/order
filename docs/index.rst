.. toctree::
  :maxdepth: 2
  :hidden:
  
  tutorials/tutorial.rst
  api/modules.rst

Order
=================================

.. image:: https://img.shields.io/travis/ipudu/order.svg
    :target: https://travis-ci.org/ipudu/order

.. image:: https://img.shields.io/pypi/v/iorder.svg
    :target: https://pypi.python.org/pypi/iorder

.. image:: https://img.shields.io/pypi/l/iorder.svg
    :target: https://pypi.python.org/pypi/iorder

.. image:: https://img.shields.io/pypi/pyversions/iorder.svg
    :target: https://pypi.python.org/pypi/iorder

.. image:: https://readthedocs.org/projects/order/badge/?version=latest
    :target: http://order.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://zenodo.org/badge/96138460.svg
   :target: https://zenodo.org/badge/latestdoi/96138460

Getting started
---------------

Installation:
~~~~~~~~~~~~~

.. code-block:: console

    $ pip install iorder



Usage:
~~~~~~

.. code-block:: console

    usage: order [-h] [-t TASK] [-c CENTER] [-b BINS] [-f FREQUENCY] [-p PLOT]
            [input]

    Order: A tool to characterize the local structure of liquid water by 
    geometric order parameters

    positional arguments:
    input                 XYZ trajectory of system

    optional arguments:
    -h, --help            show this help message and exit
    -t TASK, --task TASK  type of task: oto,tto,avc (default: oto)
    -c CENTER, --center CENTER
                            type of center atom (default: O)
    -b BINS, --bins BINS  number of bins for the parameter (default: 100)
    -f FREQUENCY, --frequency FREQUENCY
                            compute the parameter every n frame(s) (default: 1)
    -p PLOT, --plot PLOT  turn on / off of plotting (default: on)

Feature Support
---------------

**Order** is ready to calculate several geometric order parameters:

- Orientational Tetrahedral Order
- Translational Tetrahedral Order
- Local Structure Index (**under working**)
- Asphericity of the Voronoi Cell
- Water-Water Angular Distribution Function (**under working**)

Contributing
------------

Contributions to this library are always welcome and highly appreciated.

License
-------

MIT - See the LICENSE_ for more information.

.. _LICENSE: https://github.com/ipudu/order/blob/master/LICENSE
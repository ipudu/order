Order
========================

.. image:: https://img.shields.io/travis/ipudu/order.svg
    :target: https://travis-ci.org/ipudu/order

A tool to characterize the local structure of liquid water by geometric order parameters.

Installation
------------

::

    pip install order

or

::

    git clone https://github.com/ipudu/order
    cd order
    python setup.py install

Usage
-----

::

    usage: order [-h] [-t TASK] [-c CENTER] [-b BINS] [-f FREQUENCY] [-p PLOT]
                [input]

    Order: A tool to characterize the local structure of liquid water by geometric
    order parameters

    positional arguments:
    input                 XYZ trajectory of system

    optional arguments:
    -h, --help            show this help message and exit
    -t TASK, --task TASK  type of task: oto,tto,lsi (default: oto)
    -c CENTER, --center CENTER
                            type of center atom (default: O)
    -b BINS, --bins BINS  number of bins for the parameter (default: 100)
    -f FREQUENCY, --frequency FREQUENCY
                            compute the parameter every n frame(s) (default: 1)
    -p PLOT, --plot PLOT  turn on / off of plotting (default: on)

Author
------

-  Pu Du (`pudu.io <https://pudu.io>`_)
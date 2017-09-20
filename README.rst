.. image:: https://raw.githubusercontent.com/ipudu/order/master/docs/_static/images/order_small.png
    :target: http://order.readthedocs.io/
    :align: center

========================

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

A tool to characterize the local structure of liquid water by geometric order parameters.

Getting started
---------------

Installation:

.. code-block:: console

    $ pip install iorder

or

.. code-block:: console

    $ git clone https://github.com/ipudu/order
    $ cd order
    $ python setup.py install

Running:

.. code-block:: console
    
    # calculate bar parmeter for center atom of O
    $ order foo.xyz -t bar -c 'O' -f 100 -b 100

Feature Support
---------------

**Order** is ready to calculate several geometric order parameters:

- Orientational Tetrahedral Order
- Translational Tetrahedral Order
- Asphericity of the Voronoi Cell
- and more

Documentation
-------------

The documentation of Order is available at http://order.readthedocs.io/.

Contributing
------------

Contributions to this library are always welcome and highly appreciated.

License
-------

MIT - See the LICENSE_ for more information.

.. _LICENSE: https://github.com/ipudu/order/blob/master/LICENSE
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

Running:
~~~~~~~~

.. code-block:: console

    # calculate bar parmeter for center atom of O
    $ order foo.xyz -t bar -c 'O' -f 100 -b 100

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

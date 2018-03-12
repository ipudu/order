###############################################################################
# -*- coding: utf-8 -*-
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT License
###############################################################################


from __future__ import print_function, division
import os
import six
from six.moves import range

import numpy as np
from progress.bar import ChargingBar
from .util import pbc
from . import oto


class StructureFactor():
    """Structure Factor"""
    pass
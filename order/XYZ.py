###############################################################################
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT MIT License
###############################################################################

from __future__ import print_function, division
import six


import numpy as np


class XYZLoader(object):

    def __init__(self, filename):
        self.filename = filename
        self.n_atoms = self.n_atoms()
        self.n_frames = 0
    
    def close(self):
    """close XYZ file"""
        pass
    
    def n_atoms(self):
    """number of atoms in each frame"""
        with open(self.filename, 'r') as f:
            n = f.readline()
        return int(n)

    def __del__(self):
        self.close()
    
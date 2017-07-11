###############################################################################
# -*- coding: utf-8 -*-
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT License
###############################################################################

from __future__ import division, print_function
from six.moves import range

import numpy as np
from scipy.spatial import ConvexHull

class VoronoiCell(object):
    """asphericity of the Voronoi cell"""
    def __init__(self):
        pass
    
    def compute_vc(self, points):
        """compute the Voronoi cell"""
        #total area of all planes
        S = 0.0

        #total volume of Voronoi polyhedron
        V = 0.0

        #compute S and V
        S = ConvexHull(points).area
        V = ConvexHull(points).volumes

        #voronoi cell
        eta = S ** 3 / (36 * np.pi * V ** 2)

        return eta
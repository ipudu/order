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
from scipy.spatial import Voronoi
from progress.bar import ChargingBar
from .util import pbc
from . import oto

class VoronoiCell(oto.Orientational):
    """asphericity of the Voronoi cell"""
    def __init__(self, filename, center, bins=100):
        super(VoronoiCell, self).__init__(filename, center, bins)

    def wrap_box(self, c_coord, coords, L):
        """wrap the simulation box"""
        new_coords = np.zeros([self.traj.n_atoms,3], dtype=np.float)
        for i in range(self.traj.n_atoms):
            dx, dy, dz = coords[i] - c_coord

            #periodic boundary conditions
            dx, dy, dz = pbc(dx, dy, dz, L)
            new_coords[i] = np.array([dx, dy, dz])
        
        return new_coords

    def polyhedron(self, coords, j, L):
        """find the polyhedron for center molecule"""
        vor = Voronoi(coords)
        #get the vertices
        points = [vor.vertices[x] for x in vor.regions[vor.point_region[j]] if x != -1]
        return points

    def compute_vc(self, points):
        """compute the Voronoi cell"""
        #compute S and V
        S = ConvexHull(points).area
        V = ConvexHull(points).volume

        #voronoi cell
        eta = S ** 3 / (36 * np.pi * V ** 2)

        return eta

    def asphericity(self, freq = 1):
        """compute asphericity of the Voronoi cell"""
        #progress bar
        frames = int(self.traj.n_frames / freq)
        bar = ChargingBar('Processing', max=frames, 
        suffix='%(percent).1f%% - %(eta)ds')

        for i in range(0, self.traj.n_frames, freq):
            for j in range(self.traj.n_atoms):
                if self.traj.atom_names[i][j] == self.center:
                    #center coordinate
                    c = self.traj.coords[i][j]
                    
                    #coordinates
                    cs = self.traj.coords[i]
                    
                    #box_size
                    L = self.traj.box_size[i]

                    #new coordinates after wrapping
                    nc = self.wrap_box(c, cs, L)
                    points = self.polyhedron(nc, j, L)
                    e = self.compute_vc(points)
                    self.raw.append(e)
            bar.next()
        bar.finish()
        

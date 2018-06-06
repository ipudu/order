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
import yaml


class WillardChandler(object):
    """
    Identifies the dividing surface using the Willard-Chandler method
    """
    def __init__(self, reader, inputfile):
        self.coords = reader.coords
        self.n_frames = reader.n_frames
        self.box, self.box_info = self.get_box()
        with open(inputfile, 'r') as f:
            self.input = yaml.load(f)


    def get_box(self):
        box = []
        box_info = []
        for i in range(self.n_frames):
            xlo = self.coords[i][:,0].min()
            xhi = self.coords[i][:,0].max()
            ylo = self.coords[i][:,1].min()
            yhi = self.coords[i][:,1].max()
            zlo = self.coords[i][:,2].min()
            zhi = self.coords[i][:,2].max()
            box.append([xhi - xlo, yhi - ylo, zhi - zlo])∂
            box_info.append([xlo, xhi, ylo, yhi, zlo, zhi])
        return np.array(box), np.array(box_info)

    def density(self, r_coord, i_coord, box, xi):
        n, _ = r_coord.shape
        rc = np.zeros([n, 3])
        rc = r_coord[i] - i_coord
        xi_2 = xi ** 2
        
        #periodic boundary conditions
        for j in range(3):
            rc[:,j] -= box[j] * np.round(rc[:,j] / box[j])

        r_2 = (rc ** 2).sum(axis=1)

        rho = (2 * np.pi * xi_2) ** (-1.5) * np.exp( - r_2 / xi_2)
    
        return rho

    def grid(box, mesh):
        """
        generate an homogenous grid of a box
        """
        x_len = box[1] - box[0]
        y_len = box[3] - box[2]
        z_len = box[5] - box[4]
        box_len = [x_len, y_len, z_len]
        ngrid = np.array([np.ceil(l / mesh) for l in box_len])
        spacing = box / ngrid
        


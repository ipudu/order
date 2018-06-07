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

        self.xi_2 = self.input['xi']
        self.c = self.input['c']
        self.mask = self.input['mask']


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
            box.append([xhi - xlo, yhi - ylo, zhi - zlo])
            box_info.append([xlo, xhi, ylo, yhi, zlo, zhi])
        return np.array(box), np.array(box_info)

    def single_density(self, r_coord, i_coord, box):
        """density field of single atom in a frame"""
        n, _ = r_coord.shape
        rc = np.zeros([n, 3])

        #periodic boundary conditions
        rc = r_coord - i_coord
        for j in range(3):
            rc[:,j] -= box[j] * np.round(rc[:,j] / box[j])

        r_2 = (rc ** 2).sum(axis=1)
        rho = np.exp( - r_2 / self.xi_2)

        return rho.reshape(n, 1)
    
    def single_frame_density(self, r_coord, coords, box):
        """density field of a single frame"""
        n, _ = r_coord.shape
        rho = np.zeros([n, 1])
        
        for i in self.mask:
            i_coord = coords[i]
            rho += self.single_density(r_coord, i_coord, box)

        return rho

    
    def all_density(self, coords, box, box_info):
        """density field of all frame"""

        rho = []

        for i in range(self.n_frames):
            #generate r_coord
            r_coord = self.grid(box[i], box_info[i])
            
            tmp = self.single_frame_density(r_coord, coords[i], box[i])
            tmp *= (2 * np.pi * self.xi_2) ** (-1.5)

            rho.append(tmp)
        
        return rho

    def grid(self, box, box_info, mesh=1):
        """generate an homogenous grid of a box"""
        
        ngrid = np.array([int(np.ceil(l / mesh)) for l in box])
        #spacing = box / ngrid

        xyz = []

        xlo = [box_info[0], box_info[2], box_info[4]]
        for i in range(3):
            xyz.append(np.linspace(xlo[i], box[i] - box[i] / ngrid[i], ngrid[i]))
        
        x, y, z = np.meshgrid(xyz[2], xyz[1], xyz[0], indexing='ij')

        grid = np.append(x.reshape(-1, 1), y.reshape(-1, 1), axis=1)
        grid = np.append(grid, z.reshape(-1, 1), axis=1)
    
        return grid
    

    def generate_interface(self):

        rho  = self.all_density(self.coords, self.box, self.box_info)
        np.save('rho.npy', rho)

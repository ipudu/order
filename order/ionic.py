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
import os

from scipy import stats
import numpy as np
import yaml

from progress.bar import ChargingBar

class IonicConductivity(object):
    """ Ionic Conductivity"""
    def __init__(self, reader, inputfile):
        with open(inputfile, 'r') as f:
            self.input = yaml.load(f)

        self.reader = reader
        self.E = float(self.input['efield'])
        self.mask = self.input['mask']
        self.delta_t = self.input['delta_t']

        d = self.input['direction']
        #direction
        if d == 'X' or d == 'x':
            self.d = 0
        elif d == 'Y' or d == 'y':
            self.d = 1
        else:
            self.d = 2
       
        base = os.path.basename(reader.filename)
        self.fprefix = os.path.splitext(base)[0]
  
    def crossing_ion(self, atom_names, n_frames, n_atoms, 
                        box, mask, coords):
        """
        method 1
        Jordi Faraudo, Carles Calero and Marcel Aguilella-Arzo
        Ionic Partition and Transport in Multi-Ionic Channels: 
        A Molecular Dynamics Simulation Study of the OmpF Bacterial Porin
        https://doi.org/10.1016/j.bpj.2010.07.058
        """

        pass         

    def total_intensity(self, atom_names, n_frames, n_atoms, 
                        box, mask, coords, delta_t):
        """
        method 2
        Jordi Faraudo, Carles Calero and Marcel Aguilella-Arzo
        Ionic Partition and Transport in Multi-Ionic Channels: 
        A Molecular Dynamics Simulation Study of the OmpF Bacterial Porin
        https://doi.org/10.1016/j.bpj.2010.07.058
        """

        I  = np.zeros(n_frames-1)

        #progress bar
        bar = ChargingBar('Processing', max=n_frames-1, 
                           suffix='%(percent).1f%% - %(eta)ds')

        for i in range(n_frames-1):
            tmp = 0
            mid = coords[i][:, self.d].max() + coords[i][:, self.d].min()
            mid *= 0.5

            for j in range(n_atoms):

                atom  = atom_names[i][j]
                atom  = atom[0]

                if atom in mask:
                    if np.abs(coords[i][j][self.d] - mid) <= box[i][self.d] / 4.:
                        #print(coords[i+1][j][self.d] - coords[i][j][self.d])
                        tmp += mask[atom] * (coords[i+1][j][self.d] - 
                                            coords[i][j][self.d])
            
            #I[i] = 1. / (delta_t * box[i][self.d])
            I[i] = 1. / (box[i][self.d] / 2.)
            I[i] *= tmp
            
            if i !=0:
               I[i] += I[i-1]

            bar.next()

        bar.finish()
        return I

    def intensity_across_a_fixed_plane(self, atom_names, n_frames, n_atoms,
                                       box, mask, coords):
        """
        method 3
        Jordi Faraudo, Carles Calero and Marcel Aguilella-Arzo
        Ionic Partition and Transport in Multi-Ionic Channels: 
        A Molecular Dynamics Simulation Study of the OmpF Bacterial Porin
        https://doi.org/10.1016/j.bpj.2010.07.058
        """

        Q  = np.zeros(n_frames)
        
        #progress bar
        bar = ChargingBar('Processing', max=n_frames-1, 
                           suffix='%(percent).1f%% - %(eta)ds')

        for i in range(1, n_frames):
            if 'select plane' in self.input:
                mid = self.input['select plane']
            else:
                mid = coords[i][:, self.d].max() + coords[i][:, self.d].min()
                mid *= 0.5

            tmp = 0
            
            quarter = coords[i][:, self.d].max() + coords[i][:, self.d].min()
            quarter *= 0.25
            
            for j in range(n_atoms):
                
                atom  = atom_names[i][j]
                atom  = atom[0]

                if atom in mask:
                    if coords[i][j][self.d] > mid and coords[i][j][self.d] < mid + quarter:
                        if coords[i-1][j][self.d] < mid and coords[i-1][j][self.d] > mid - quarter:
                            tmp += mask[atom]

                    if coords[i][j][self.d] < mid and coords[i][j][self.d] > mid - quarter:
                        if coords[i-1][j][self.d] > mid and coords[i-1][j][self.d] < mid + quarter:
                            tmp -= mask[atom]
                Q[i] = tmp + Q[i-1]
            bar.next()
        bar.finish()

        return Q

    def calculate_conductivity(self):
        """ calculate the ionic conductivity """

        self.sigma = np.zeros(3)
        atom_names = self.reader.atom_names
        n_frames = self.reader.n_frames
        n_atoms = self.reader.n_atoms
        box = self.reader.box_size
        mask = self.mask
        coords = self.reader.coords
        delta_t = self.delta_t

        t = np.arange(float(n_frames)) * self.delta_t

        # calculate the area
        # area unit: Angstrom ^ 2
        area = np.zeros(n_frames-1)
        for i in range(n_frames-1):
            tmp = 1.
            for j in range(3):
                if j != self.d:
                    tmp *= box[i][j]
            area[i] = tmp

        average_area = np.average(area)

        # method 2 ########################################################

        self.I = self.total_intensity(atom_names, n_frames, n_atoms, 
                                 box, mask, coords, delta_t)

        t_ = t[:-1]
        slope, _, _, _, _ = stats.linregress(t_, self.I)
        #slope = np.average(self.I)
        
        # calculate the conductivity        
        # Q =  I * t
        # I unit: A
        # J unit: A / m ^2
        
        J = 1.602176e13 * slope / average_area

        self.sigma[1] = J / self.E
        
        # method 3 ########################################################
        self.Q = self.intensity_across_a_fixed_plane(atom_names, n_frames, 
                                                n_atoms, box, 
                                                mask, coords)

        slope, _, _, _, _ = stats.linregress(t,self.Q)

        # calculate the conductivity        
        # Q =  I * t
        # I unit: A
        # J unit: A / m ^2
        J = 1.602176e13 * slope / average_area

        # sigma unit: S / m
        self.sigma[2]  = J / self.E
        ##################################################################
        self.print_result()

    def print_result(self):
        """ 
        print the ioinc conductivities calculated from
        different methods.
        """
        print('\nResult:\n')
        print('                        Method:\tIonic Conductivity (S/m)')
        print('               total_intensity\t{:.3f}'.format(self.sigma[1]))
        print('intensity_across_a_fixed_plane\t{:.3f}\n'.format(self.sigma[2]))
 
    def out_put(self, taskname='ionic'):
        """output raw data and distribution"""
        
        #method 2 output
        raw_data_1 = self.fprefix + '_' + taskname + '_ti.dat'
        with open(raw_data_1, 'w') as f:
            f.write('#' + taskname + ' generated by Order: A Python Tool\n')
            f.write('#raw data:\n')
            f.write('#conductivity:{} (S/m)\n'.format(self.sigma[1]))
            f.write('#t Q\n')

            n = len(self.I)
            t = np.arange(float(n))
            t *= self.delta_t
            
            for i in range(n):
                f.write('{} {}\n'.format(t[i], self.I[i]))        

        #method 3 output
        raw_data_2 = self.fprefix + '_' + taskname + '_iaafp.dat'
        with open(raw_data_2, 'w') as f:
            f.write('#' + taskname + ' generated by Order: A Python Tool\n')
            f.write('#raw data:\n')
            f.write('#conductivity:{} (S/m)\n'.format(self.sigma[2]))
            f.write('#t Q\n')

            n = len(self.Q)
            t = np.arange(float(n))
            t *= self.delta_t
            
            for i in range(n):
                f.write('{} {}\n'.format(t[i], self.Q[i]))
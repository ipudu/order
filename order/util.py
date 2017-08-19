###############################################################################
# -*- coding: utf-8 -*-
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT License
###############################################################################

import numpy as np


def output_welcome():
    """print welcome information"""
    order = """                
                ,-----.           ,--.               
                '  .-.  ',--.--. ,-|  | ,---. ,--.--. 
                |  | |  ||  .--'' .-. || .-. :|  .--' 
                '  '-'  '|  |   \ `-' |\   --.|  |    
                `-----' `--'    `---'  `----'`--'    
                                                    
    """
    print(order)
    print('-' * 70)
    print('\nOrder: A tool to characterize the local structure of liquid water')
    print('       by geometric order parameters\n')

def output_system_info(filename, n_atoms, n_frames):
    """print system information"""
    print('System information:\n')
    print('        XYZ trajectory file name:\t{:s}'.format(filename))
    print('  Number of particles in the box:\t{:d}'.format(n_atoms))
    print('       Total number of snapshots:\t{:d}\n'.format(n_frames))

def output_task(name, freq, bins, center):
    """print task information"""
    print('\nTask information:\n')
    if name is 'oto':
        print('                  Parameter name:\tOritentational tetrahedral order')
    if name is 'tto':
        print('                  Parameter name:\tTranslational tetrahedral order')
    if name is 'avc':
        print('                  Parameter name:\tAsphericity of the Voronoi cell')
    if name is 'msd':
        print('                  Parameter name:\tMean square displacement')
    print('                       Frequency:\tevery {:d} frame(s)'.format(freq))
    print('                  Number of bins:\t{:d}'.format(bins))
    if name is not 'msd':
        print('                     Center atom:\t{:s}\n'.format(center))

def output_end(t_start, t_end):
    """print total running time"""
    print('\n' + '-' * 70)
    print ('\nTotal elapsed time = {:.2f} seconds.'.format(t_end - t_start))
    art = """
                           .
                          ":"
                        ___:____     |"\/"|
                      ,'        `.    \  /
                      |  O        \___/  |
                    ~^~^~^~^~^~^~^~^~^~^~^~^~
           """
    print(art)   

def pbc(dx, dy, dz, L):
    """periodic boundary conditions"""
    hL = [ x / 2 for x in L]
    if dx > hL[0]:
        dx -= L[0]
    if dx < -hL[0]:
        dx += L[0]
    if dy > hL[1]:
        dy -= L[1]
    if dy < -hL[1]:
        dy += L[1]
    if dz > hL[2]:
        dz -= L[2]
    if dz < -hL[2]:
        dz += L[2]
    return dx, dy, dz


def cos_angle(v1, v2):
    """compute the cos angle of two giving vectors"""
    #cos_phi = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
    return  np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

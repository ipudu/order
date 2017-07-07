###############################################################################
# -*- coding: utf-8 -*-
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT MIT License
###############################################################################

from __future__ import division
import numpy as np


def welcome():
    order = """                
    ,-----.           ,--.               
    '  .-.  ',--.--. ,-|  | ,---. ,--.--. 
    |  | |  ||  .--'' .-. || .-. :|  .--' 
    '  '-'  '|  |   \ `-' |\   --.|  |    
    `-----' `--'    `---'  `----'`--'    
                                                    
    """
    print(order)
    print('=================================================================')
    print('Order: A tool to characterize the local structure of liquid water')
    print('       by geometric order parameters\n')


def output_end(t_start, t_end):
    print('-' * 70)
    print ('Total looping time = {:.2f} seconds.'.format(t_end - t_start))
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
    return  np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
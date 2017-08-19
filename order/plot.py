###############################################################################
# -*- coding: utf-8 -*-
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT License
###############################################################################

import os
import matplotlib.pyplot as plt
import numpy as np


class plot(object):
    """plotting"""
    def __init__(self, filename, taskname):
        base = os.path.basename(filename)
        self.fprefix = os.path.splitext(base)[0]
        self.taskname = taskname
        self.data = np.loadtxt(self.fprefix+'_'+self.taskname+'.dat')
        self.plot_distribution()
    
    def plot_distribution(self):
        """plot distribution"""

        #plot setting
        #plt.rcParams['font.family'] = 'serif'
        #plt.rcParams['font.serif'] = 'Ubuntu'
        #plt.rcParams['font.monospace'] = 'Ubuntu Mono'
        plt.rcParams['font.size'] = 10
        plt.rcParams['axes.labelsize'] = 10
        #plt.rcParams['axes.labelweight'] = 'bold'
        plt.rcParams['xtick.labelsize'] = 8
        plt.rcParams['ytick.labelsize'] = 8
        plt.rcParams['legend.fontsize'] = 10
        plt.rcParams['figure.titlesize'] = 12

        #clean last plot
        plt.clf()

        if self.taskname == 'oto':
            plt.xlabel("Q")
            plt.ylabel(r"$P(Q)  (arb. unit)$")

        if self.taskname == 'tto':
            plt.xlabel("Sk")
            plt.ylabel(r"$P(Sk)  (arb. unit)$")
         
        if self.taskname == 'avc':
            plt.xlabel("Asphericity")
            plt.ylabel(r"$P(Asphericity)  (arb. unit)$")
        
        if self.taskname == 'msd':
            plt.xlabel('t')
            plt.ylabel('<r^2>')

        x = self.data[:,0]
        y = self.data[:,1]

        plt.plot(x,y,linewidth=2.0)
        
        figure = self.fprefix + '_' + self.taskname.upper() + '.pdf'
        plt.savefig(figure, bbox_inches="tight")
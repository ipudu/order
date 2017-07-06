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
        self.xyzfile = open(self.filename, 'r')
        self.n_atoms = self.n_atoms()
        self.n_frames = self.n_frames()
        self.box_size = self.box_size()
        self.atom_names = np.empty([self.n_frames, self.n_atoms, 1], dtype='|S2')
        self.atom_coords = np.empty([self.n_frames, self.n_atoms, 3], dtype=np.float)
        self.read_all_frames()
    
    def close(self):
        """close XYZ file if it was open"""
        if self.xyzfile is None:
            return
        self.xyzfile()
        self.xyzfile = None

      def __del__(self):
        self.close()
        
    def n_atoms(self):
        """number of atoms in each frame"""
        with open(self.filename, 'r') as f:
            n = f.readline()
        return int(n)
    
    def n_frames(self):
        """number of frames in XYZ trajectory"""
        try:
            return self.read_n_frames()
        except IOError:
            return 0

    def read_next_frame(self, frame):
        """read a frame of XYZ trajectory"""
        f = self.xyzfile
        try:
            f.readline()
            f.readline()
            for i in range(self.n_atoms):
                line = f.readline().split()
                self.atom_names[frame][i] = line[0]
                self.atom_coords[frame][i] = \
                np.array(map(float, lineInfo[1:4]), dtype=np.float)
        
        except (ValueError, IndexError) as err:
            raise EOFError(err)

    def read_n_frames(self):
        """get the starting position of each frame"""
        lines_per_frame = self.n_atoms + 2
        counter = 0
        offset = []
        
        with open(self.filename, 'r') as f:
            line = True
            while line:
                if not counter % lines_per_frame:
                    offset.append(f.tell())
                line = f.readline()
                counter += 1
        
        n_frames = int(counter / lines_per_frame)
        self.offsets = offsets
        return n_frames

    def read_all_frames(self):
        """read all frames of XYZ trajectory"""
        for frame in range(self.n_frames):
            self.xyzfile.seek(self.offsets[frame])
            self.read_next_frame(frame)

    


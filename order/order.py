###############################################################################
# -*- coding: utf-8 -*-
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT License
###############################################################################

from __future__ import print_function
import argparse
import time
from . import XYZ, oto, tto, avc, msd, lsi, plot, util

def get_parser():
    parser = argparse.ArgumentParser(description='Order: A tool to characterize the \
                                                  local structure of liquid water \
                                                  by geometric order parameters')
    parser.add_argument('input', type=str, nargs='?',help='XYZ trajectory of system')
    parser.add_argument('-t','--task', default='oto', type=str,
                        help=' type of task: oto,tto,avc (default: oto)')
    parser.add_argument('-c','--center', default='O', type=str,
                        help=' type of center atom  (default: O)')
    parser.add_argument('-b','--bins', default=100, type=int,
                        help=' number of bins for the parameter (default: 100)')
    parser.add_argument('-f','--frequency', default=1, type=int,
                        help=' compute the parameter every n frame(s) (default: 1)')                        
    parser.add_argument('-p','--plot', default='on', type=str,
                        help='turn on / off of plotting (default: on)')
    return parser

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if not args['input']:
        parser.print_help()
        return
    if args['task']:
        t_start = time.clock()
        util.output_welcome()
        
        reader = XYZ.XYZLoader(args['input'])
        
        util.output_system_info(reader.filename, reader.n_atoms, reader.n_frames)

        if 'oto' in args['task']:
            util.output_task('oto', args['frequency'], args['bins'], args['center'])
            tasker = oto.Orientational(reader, args['center'], args['bins'])
            tasker.orientational_param(args['frequency'])
            tasker.out_put()
        
        if 'tto' in args['task']:
            util.output_task('tto', args['frequency'], args['bins'], args['center'])
            tasker = tto.Translational(reader, args['center'], args['bins'])
            tasker.translational_param(args['frequency'])
            tasker.out_put('TTO', 'Sk')

        if 'avc' in args['task']:
            util.output_task('avc', args['frequency'], args['bins'], args['center'])
            tasker = avc.VoronoiCell(reader, args['center'], args['bins'])
            tasker.asphericity(args['frequency'])
            tasker.out_put('AVC', 'Eta')

        if 'msd' in args['task']:
            util.output_task('msd', args['frequency'], args['bins'], args['center'])
            tasker = msd.meanSquareD(reader, args['center'], args['bins'])
            #TODO:
            tasker.mean_square_displacement(1000, args['frequency'])
            tasker.out_put('MSD')

    if args['plot'] == 'on':
        for t in args['task'].split(','):
            ploter = plot.plot(args['input'], t)

    t_end = time.clock()
    util.output_end(t_start, t_end)
if __name__ == '__main__':
    command_line_runner()
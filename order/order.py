###############################################################################
# -*- coding: utf-8 -*-
# Order: A tool to characterize the local structure of liquid water 
#        by geometric order parameters
# 
# Authors: Pu Du
# 
# Released under the MIT License
###############################################################################

import argparse
#from order import XYZ, oto, tto, lsi, plot, util

def get_parser():
    parser = argparse.ArgumentParser(description='Order: A tool to characterize the \
                                                  local structure of liquid water \
                                                  by geometric order parameters')
    parser.add_argument('input', type=str, nargs='?',help='XYZ trajectory of system')
    parser.add_argument('-t','--task', default='oto', type=str,
                        help=' type of task: oto,tto,lsi (default: oto)')
    parser.add_argument('-c','--center', default='O', type=str,
                        help=' type of center atom  (default: O)')
    parser.add_argument('-b','--bins', default=100, type=int,
                        help=' number of bins for the parameter (default: 100)')
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
        util.output_welcome()
        
        reader = XYZLoader(args['input'])
        
        util.output_system_info(reader.filename, reader.n_atoms, reader.n_frames)

        if 'oto' in args['task']:
            tasker = (reader, args['center'], args['bins'])
            tasker.orientational_param()
            tasker.out_put()

    if args['plot'] is 'on':
        pass
    
    #util.output_end()
if __name__ == '__main__':
    command_line_runner()
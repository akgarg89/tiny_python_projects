#!/usr/bin/env python3
"""
Author: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 07-27-2020
Purpose: HOWLER
"""

import argparse
import os
import sys


# ----------------------------------------------------------
def get_args():
    """Get the arguments"""
    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        help='Input string or file',
                        type=str,
                        metavar='txt')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        type=str,
                        help='Output filename',
                        default='')

    args = parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# ----------------------------------------------------------
def main():
    """The main executable code"""
    args = get_args()
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout
    out_fh.write(args.text.upper()+'\n')
    out_fh.close()


# ----------------------------------------------------------
if __name__ == '__main__':
    main()

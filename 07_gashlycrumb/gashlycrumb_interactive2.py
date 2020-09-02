#!/usr/bin/env python3
"""
Name: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 2020-07-29
Purpose: Gashlycrumb
"""

import argparse
import sys
from pprint import pprint as pp


# --------------------------------------------------------
def get_args():
    """Get command line arguments"""
    parser=argparse.ArgumentParser(
                description='Gashlycrumb',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        help='Input File',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')

    return parser.parse_args()


# ---------------------------------------------------------
def main():
    """The main Function"""
    args=get_args()
    dict={line[0].lower(): line.rstrip() for line in args.file}
    #pp(dict)

    while True:
        letter = input('Please provide a letter [! to quit]: ')
        if letter == '!':
            print('Bye')
            break
        print(dict.get(letter, f'I do not know "{letter}".'))


# ---------------------------------------------------------
if __name__ == '__main__':
    main()

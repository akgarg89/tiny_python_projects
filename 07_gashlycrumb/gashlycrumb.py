#!/usr/bin/env python3
"""
Name: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 2020-07-29
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------------
def get_args():
    """Get command line arguments"""
    parser=argparse.ArgumentParser(
                description='Gashlycrumb',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        help='Letter(s)',
                        nargs='+')
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
    dict={}

    for line in args.file:
        #print(line[0].lower())
        dict[line[0].lower()] = line.rstrip()
    #print(dict)

    for letter in args.letter:
        if letter.lower() in dict:
            print(dict[letter.lower()])
        else:
            print(f'I do not know "{letter}".')


# ---------------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Name: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 2020/07/28
Purpose: Emulate wc (word count)
"""


import argparse
import os
import sys


# -------------------------------------------------------
def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(
                description='Emulate wc (word count)',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('rt'),
                        default=[sys.stdin])

    return parser.parse_args()


# ---------------------------------------------------------
def main():
    """The main function"""
    args = get_args()
    total_lines =0
    total_words=0
    total_bytes=0


    for fh in args.file:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in fh:
            num_lines+=1
            num_bytes+=len(line)
            #if line!='\n':
                #print(len(line))
            num_words+=len(line.split())
        total_lines+=num_lines
        total_words+=num_words
        total_bytes+=num_bytes
        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')
    if len(args.file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')


# ---------------------------------------------------------
if __name__ == '__main__':
    main()

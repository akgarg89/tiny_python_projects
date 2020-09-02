#!/usr/bin/env python3
"""
Name: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 2020-01-30
Purpose: Apples and Banana
"""


import argparse
import os
import sys


# --------------------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(
                description='Apples and bananas',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        type=str,
                        metavar='text',
                        help='Input text or file')
    parser.add_argument('-v',
                        '--vowel',
                        metavar='vowel',
                        type=str,
                        default='a',
                        help='The vowel to substitute',
                        choices=['a','e','i','o','u'])

    args=parser.parse_args()
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# ----------------------------------------------------------------
def main():
    args=get_args()
    vowels='aeiouAEIOU'
    dict={}
    for v in vowels:
        if v.islower():
            #print(v)
            dict[v] = args.vowel
        else:
            dict[v] = args.vowel.upper()

    print(f'{args.text.translate(str.maketrans(dict))}')



# ----------------------------------------------------------------
if __name__ == '__main__':
    main()

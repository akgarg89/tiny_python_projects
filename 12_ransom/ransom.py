#!/usr/bin/env python3
"""
Name: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 8/5/2020
Purpose: Ransom Note
"""


import argparse
import os
import random


# ----------------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(
                        description='Ransom Note',
                        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')
    parser.add_argument('-s',
                        '--seed',
                        metavar='int',
                        help='Random seed',
                        type=int,
                        default=None)

    args=parser.parse_args()
    if os.path.isfile(args.text):
        args.text=open(args.text).read().rstrip()

    return args


# -------------------------------------------------------------
def main():
    args=get_args()
    random.seed(args.seed)
    print(''.join(map(choose, args.text)))


# -------------------------------------------------------------
def choose(char):
    return char.upper() if random.choice([0,1]) else char.lower()


# -------------------------------------------------------------
def test_choose():
    state=random.getstate()
    random.seed(1)
    assert choose('a') == 'a'
    assert choose('b') == 'b'
    assert choose('c') == 'C'
    assert choose('d') == 'd'
    random.setstate(state)


# -------------------------------------------------------------
if __name__ == '__main__':
    main()

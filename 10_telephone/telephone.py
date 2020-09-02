#!/usr/bin/env python3
"""
Name: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 2020-01-30
Purpose:
"""


import argparse
import os
import random
import string


# -------------------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(
                    description = 'Telephone',
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file',
                        type=str)
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        help='Random seed',
                        type=int,
                        default=None)
    parser.add_argument('-m',
                        '--mutations',
                        metavar='mutations',
                        help='Percent mutations',
                        default=0.1,
                        type=float)

    args = parser.parse_args()
    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text=open(args.text).read().rstrip()

    return args


# -----------------------------------------------------------------
def main():
    args=get_args()
    random.seed(args.seed)
    num_mutations=round(len(args.text)*args.mutations)
    alpha = string.ascii_letters + string.punctuation
    #res = ''.join(sorted(test_string))
    alpha=''.join(sorted(alpha))
    print(f'You said: "{args.text}"')
    #if num_mutations!=0:
    indexes=random.sample(range(len(args.text)), num_mutations)
    for i in indexes:
        args.text=args.text[:i]+random.choice(alpha.replace(args.text[i],''))+args.text[i+1:]
    print(f'I heard : "{args.text}"')


# -----------------------------------------------------------------
if __name__ == '__main__':
    main()

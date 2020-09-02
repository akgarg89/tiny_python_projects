#!/usr/bin/env python3
"""
Author : jarvis <jarvis@localhost>
Date   : 2020-07-26
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        default=False,
                        action='store_true')
    parser.add_argument('-n',
                        '--no_oxford_comma',
                        help='No Oxford Comma',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items_arg = args.items
    sorted_arg = args.sorted

    if sorted_arg:
        items_arg.sort()

    if len(items_arg) == 1:
        print(f'You are bringing {items_arg[0]}.')
    elif len(items_arg) == 2:
        print(f'You are bringing {items_arg[0]} and {items_arg[1]}.')
    else:
        if not(args.no_oxford_comma):
            items_arg[-1]='and '+items_arg[-1]
            print(f'You are bringing {", ".join(items_arg)}.')
        else:
            items_arg[-1]=items_arg[-2]+' and '+items_arg[-1]
            items_arg.pop(-2)
            print(f'You are bringing {", ".join(items_arg)}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : jarvis <jarvis@localhost>
Date   : 2020-07-27
Purpose: Jump the Five
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input Text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_arg = args.text

    jumper = {'1':'9',
                '2':'8',
                '3':'7',
                '4':'6',
                '5':'0',
                '6':'4',
                '7':'3',
                '8':'2',
                '9':'1',
                '0':'5'}

    encoded_message =''
    for char in text_arg:
        encoded_message+=jumper.get(char, char)

    print(f'{encoded_message}')


# --------------------------------------------------
if __name__ == '__main__':
    main()

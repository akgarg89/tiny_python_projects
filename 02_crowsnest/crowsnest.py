#!/usr/bin/env python3
"""
Author : jarvis <jarvis@localhost>
Date   : 2020-07-26
Purpose: Crow's Nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')
    parser.add_argument('--starboard',
                        #metavar='starboard',
                        help='TRUE if on right side',
                        default=False,
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    starboard = args.starboard
    article = 'an' if word[0].lower() in 'aeiou' else 'a'

    if starboard:
        print(f'Ahoy, Captain, {article} {word} off the starboard bow!')
    else:
        print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Name: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 2020-01-30
Purpose: Bottles of beer song
"""


import argparse


# ------------------------------------------------------------
def get_args():
    """Parse the command line arguments"""
    parser=argparse.ArgumentParser(
                    description='Bottles of beer song',
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                    '--num',
                    metavar='number',
                    type=int,
                    help='How many bottles',
                    default=10)
    args = parser.parse_args()
    if args.num<=0:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# -------------------------------------------------------------
def main():
    """Main Shit here"""
    args = get_args()
    #print(args.num)
    print('\n\n'.join(map(verse, range(args.num, 0, -1))))


# -------------------------------------------------------------
def verse(bottle):
    """Sing a verse"""
    next_bottle = bottle-1
    s1 = 's' if bottle >1 else ''
    s2 = '' if next_bottle==1 else 's'
    s3 = 'No more' if next_bottle==0 else next_bottle

    return '\n'.join([
        f'{bottle} bottle{s1} of beer on the wall,', f'{bottle} bottle{s1} of beer,',
        'Take one down, pass it around,',
        f'{s3} bottle{s2} of beer on the wall!'
        ])


# --------------------------------------------------------------
def test_verse():
    """Test Verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
        ])
    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
        ])
    eight_bottles = verse(8)
    assert eight_bottles == '\n'.join([
        '8 bottles of beer on the wall,', '8 bottles of beer,',
        'Take one down, pass it around,', '7 bottles of beer on the wall!'
        ])


# ----------------------------------------------------------------
if __name__ == '__main__':
    main()

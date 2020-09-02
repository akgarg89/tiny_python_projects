#!/usr/bin/env python
"""
Name: Achal Kumar Garg <achalkumargarg89>
Date: 2020/08/05
Purpose: Twelve Days of Christmas
"""


import argparse
import sys


# --------------------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(
                    description='Twelve Days of Christmas',
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        metavar='days',
                        type=int,
                        default=12,
                        help='Number of days to sing')
    parser.add_argument('-o',
                        '--outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        help='Outfile',
                        default=sys.stdout)
    args=parser.parse_args()
    if args.num > 12 or args.num < 1:
        parser.error(f'--num "{args.num}" must be between 1 and 12')
    return args


# ----------------------------------------------------------------
def main():
    args = get_args()
    verses = map(verse,range(1,args.num + 1))
    args.outfile.write('\n\n'.join(verses)+'\n')


def verse(day):
    """Create a verse"""
    ordinal={1:'first', 2:'second', 3:'third', 4:'fourth', 5:'fifth', 6: 'sixth',
            7:'seventh', 8:'eighth', 9:'ninth', 10:'tenth', 11:'eleventh', 12:'twelfth'}
    gifts = [' partridge in a pear tree.', 'Two turtle doves,', 'Three French hens,',
            'Four calling birds,', 'Five gold rings,', 'Six geese a laying,',
            'Seven swans a swimming,', 'Eight maids a milking,', 'Nine ladies dancing,',
            'Ten lords a leaping,', 'Eleven pipers piping,', 'Twelve drummers drumming,']

    str_1 = f'On the {ordinal[day]} day of Christmas,'
    str_2 = 'My true love gave to me,'
    verses = [str_1,str_2]
    if day == 1:
        last_verse = 'A'
    else:
        last_verse = 'And a'
    for i in range(day,0,-1):
        if i == 1:
            verses.append(last_verse+gifts[i-1])
        else:
            verses.append(gifts[i-1])

    paras = '\n'.join(verses)
    return paras


# ----------------------------------------------------------------
def test_verse():
    """Test Verse"""
    assert verse(1) == '\n'.join([
                'On the first day of Christmas,', 'My true love gave to me,',
                'A partridge in a pear tree.'
                ])
    assert verse(2) == '\n'.join([
                'On the second day of Christmas,', 'My true love gave to me,',
                'Two turtle doves,', 'And a partridge in a pear tree.'
                ])



# ----------------------------------------------------------------
if __name__ == '__main__':
    main()

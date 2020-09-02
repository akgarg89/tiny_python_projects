#!/usr/bin/env python3
"""
Name: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 8/25/2020
Purpose: Separate id and name
"""


import re
import pandas as pd
import argparse


# --------------------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(
                    description='Separate ID and column',
                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c',
                        '--col',
                        metavar='column_name',
                        type=str,
                        default='(PRIMARY MCAT ID - PRIMARY MCAT NAME)',
                        help='Column to be splitted')
    parser.add_argument('-i',
                        '--inputfile',
                        metavar='FILE',
                        type=str,
                        help='Input excel location file',
                        default='./id_name.xlsx')
    parser.add_argument('-s',
                        '--sheet',
                        metavar='sheet_name',
                        type=str,
                        default='id_name',
                        help='Sheet name in excel file')
    parser.add_argument('-o',
                        '--outfile',
                        metavar='output_file',
                        type=str,
                        default='./id_name_separated.xlsx',
                        help='Outfile file location with file name')
    return parser.parse_args()


# ----------------------------------------------------------------
def main():
    args = get_args()
    df = pd.read_excel(args.inputfile, sheet_name=args.sheet)
    # print(df.head())
    # (12965-Acid Proof Bricks)
    col=args.col
    id_key = r'\(([\d]+)'
    # id = re.findall(id_key, df[col][1])[0]
    # print(id)
    df['id'] = df.apply(lambda row: re.findall(id_key, row[col])[0], axis=1)
    # print(df.head())
    name_key = r'\([\d]+\-(.*)\)'
    name = re.findall(name_key, df[col][1])[0]
    # print(name)
    df['name'] = df.apply(lambda row: re.findall(name_key, row[col])[0], axis=1)
    # print(df.head())
    df.to_excel(args.outfile, sheet_name=args.sheet, index = False)




# ----------------------------------------------------------------
if __name__ == '__main__':
    main()

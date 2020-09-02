#!/usr/bin/env python3
"""
Name: Achal Kumar Garg <achalkumargarg89@gmail.com>
Date: 2020-01-30
Purpose: Abuse
"""


import argparse
import random


# ---------------------------------------------------------
def get_args():
    parser = argparse.ArgumentParser(
                description = 'Heap abuse',
                formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        metavar='adjectives',
                        type=int,
                        default=2,
                        help='Number of adjectives')
    parser.add_argument('-n',
                        '--number',
                        metavar='insults',
                        type=int,
                        default=3,
                        help='Number of insults')
    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        default=None,
                        type=int,
                        help='Random seed')
    args = parser.parse_args()
    if args.number<=0:
        parser.error(f'--number "{args.number}" must be > 0')
    if args.adjectives<=0:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    return args


# ------------------------------------------------------------
def main():
    args=get_args()
    random.seed(args.seed)
    adjectives = """bankrupt base caterwauling corrupt
                    cullionly detestable dishonest false
                    filthsome filthy foolish foul gross
                    heedless indistinguishable infected
                    insatiate irksome lascivious lecherous
                    loathsome lubbery old peevish rascaly
                    rotten ruinous scurilous scurvy slanderous
                    sodden-witted thin-faced toad-spotted
                    unmannered vile wall-eyed""".split()
    nouns = """Judas Satan ape ass barbermonger beggar block
            boy braggart butt carbuncle coward coxcomb cur dandy
            degenerate fiend fishmonger fool gull harpy jack
            jolthead knave liar lunatic maw milksop minion ratcatcher
            recreant rogue scold slave swine traitor varlet villain worm""".split()
    #print(len(nouns))
    #print(len(adjectives))
    for i in range(args.number):
        adj = random.sample(adjectives,args.adjectives)
        noun = random.choice(nouns)
        print(f'You {", ".join(adj)} {noun}!')



# ------------------------------------------------------------
if __name__ == '__main__':
    main()

#!usr/bin/env/python

# File:           main.py
# Author:         Alex Thompson
# Github:         palex88
# Date Created:   2018-02-12
# Date Modified:  2018-02-12
# Python Version: 3.6

import time
import progressbar
import whois
from argparse import ArgumentParser
from pprint import pprint


def progress(num):
    bar = progressbar.ProgressBar()
    for i in bar(range(num)):
        time.sleep(.05)


def run():
    ap = ArgumentParser()
    ap.add_argument('-v', '--verbose', default=False, action='store_true', help='increase verbosity')
    ap.add_argument('-n', '--number', type=int, default=1, help='print up to this number')
    ap.add_argument('-na', '--name', help='Your name')
    ap.add_argument('-ps', '--progress', help='see a progress bar for the number')
    ap.add_argument('-w', '--who', help='look up a domain')
    args = ap.parse_args()

    if args.verbose:
        for arg in vars(args):
            print(arg, getattr(args, arg))

    if args.number:
        for x in range(args.number):
            print(x)

    if args.name:
        name = (args.name or 'there')
        print("Hello ", name, "!")

    if args.progress:
        num = (args.progress or 100)
        progress(num)

    if args.who:
        domain = whois.query(args.who)
        pprint(domain.__dict__)


if __name__ == '__main__':
    run()

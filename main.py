#!usr/bin/env/python

# File:           main.py
# Author:         Alex Thompson
# Github:         palex88
# Date Created:   2018-02-12
# Date Modified:  2018-02-13
# Python Version: 3.6

import os
import time
from argparse import ArgumentParser
from pprint import pprint
from glob import glob

import progressbar
import whois


def run():
    ap = ArgumentParser()
    ap.add_argument('-v', '--verbose', default=False, action='store_true', help='increase verbosity')
    ap.add_argument('-n', '--number', type=int, default=1, help='print up to this number')
    ap.add_argument('-na', '--name', help='Your name')
    ap.add_argument('-ps', '--progress', help='see a progress bar for the number')
    ap.add_argument('-w', '--who', help='look up a domain')
    ap.add_argument('-f', '--file', help='create a new file txt file, do not specify file type')
    ap.add_argument('-l', '--list', default=False, action='store_true', help='list all txt files')
    ap.add_argument('-df', '--delete', help='delete a txt file, specify a file type')
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
        bar = progressbar.ProgressBar()
        for i in bar(range(num)):
            time.sleep(.05)

    if args.who:
        domain = whois.query(args.who)
        pprint(domain.__dict__)

    if args.file:
        file = args.file
        with open(file + '.txt', 'w') as f:
            pass

    if args.list:
        print(glob('*.txt'))

    if args.delete:
        file = args.delete
        if os.path.isfile(file + '.txt'):
            if file.endswith('.txt'):
                os.remove(file)
            else:
                print('you can only delete txt files')
        else:
            print('that file does not exist')


if __name__ == '__main__':
    run()

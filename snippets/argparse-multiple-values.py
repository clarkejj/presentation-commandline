#!/usr/bin/env python2

import sys
from argparse import ArgumentParser
ap = ArgumentParser()

ap.add_argument('-t','--to', metavar="EMAIL", action="append")

args = ap.parse_args()

if not args.to:
    sys.exit("missing --to values")

print "Sending email to: ", ', '.join(args.to)


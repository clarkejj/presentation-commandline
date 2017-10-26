#!/usr/bin/env python2

from argparse import ArgumentParser
ap = ArgumentParser()
ap.add_argument('filename', nargs="+")

args = ap.parse_args()

for f in args.filename:
    print "processing",f 

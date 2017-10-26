#!/usr/bin/env python2

from argparse import ArgumentParser,RawDescriptionHelpFormatter

__version__ = 0.1

version_info="""Frobnicator  - version %s
Copyright (C) 2017 Assaf Gordon <assafgordon@gmail.com>
License: MIT
""" % (__version__)

ap = ArgumentParser(
     description="My Frobnicator",
     formatter_class=RawDescriptionHelpFormatter,
     version=version_info)

ap.add_argument('-m','--max-age', type=int, metavar="AGE",
                help="Maximum patient age (samples of older patients will be ignored)")

ap.add_argument('-n','--experiment-name',
		metavar="NAME", default="NO-NAME",
                help="Experiment name, used in the title of the output report" \
                     " (default: '%(default)s')")

ap.add_argument('--model',choices=["knight2001","zhang2014","lechner09"],
                default="knight2001",
                help="Statistical model to use for gene estimation" \
                     " (default: %(default)s)")

ap.add_argument('-q', '--quiet', action="store_true",
                help="supress informational messages")
ap.add_argument('filename') #help,metavar omitted for brevity
args = ap.parse_args()
if not args.quiet:
    print "Requested file:",args.filename
    if args.max_age:
       print "Ignoring samples of patients older than",args.max_age,"years"
    else:
       print "All patient samples included"
    print "Experiment name:",args.experiment_name

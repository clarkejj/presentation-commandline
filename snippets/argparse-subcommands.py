#!/usr/bin/env python2

from argparse import ArgumentParser

ap = ArgumentParser()

sp = ap.add_subparsers(help='sub-command help')

parser_commit = sp.add_parser('commit', help='commit help')
parser_commit.add_argument('-m','--message')
parser_commit.set_defaults(action="commit")

parser_clone = sp.add_parser('clone', help='clone help')
parser_clone.add_argument('-q','--quiet', action="store_true",default=False)
parser_clone.add_argument("repository")
parser_clone.set_defaults(action="clone")

args = ap.parse_args()

if args.action == "commit":
    print "commiting files, message: ", args.message

elif args.action == "clone":
    if not args.quiet:
        print "cloning repository ", args.repository

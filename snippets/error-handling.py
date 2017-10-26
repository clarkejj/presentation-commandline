#!/usr/bin/env python2

from collections import defaultdict
import sys
from argparse import ArgumentParser,RawDescriptionHelpFormatter

sums = defaultdict(int)

def parse_command_line():
    ap = ArgumentParser(
            description="Input Validation Example",
            formatter_class=RawDescriptionHelpFormatter,
            epilog="""

This program reads a tab-separated file with two fields: ID<tab>VALUE
and sums up the values for each ID.

Example:

    $ cat input.txt
    user1    5
    user2    7
    user1    1
    user2    10

    $ %(prog)s input.txt
    user1    6
    user2    17

Given invalid input files, this program should print informative
and helpful error messages.

""")

    ap.add_argument('filename',help="Input file to process (format: ID<tab>VALUE")

    args = ap.parse_args()
    return args




class MyError(RuntimeError):
    """Base class for exceptions in this module."""
    pass


def process_fields(fields):
    if len(fields)!=2:
        raise MyError("expecting 2 fields, found %d field(s)" % len(fields))

    (user,value) = fields
    try:
        value = int(value)
    except ValueError:
        raise MyError("invalid integer value '%s' in field 2" % (value))

    sums[user] += value




def process_file(filename):
    try:
        f = open(filename,'r')

        for linenum,line in enumerate(f):
            try:
                flds = line.strip().split()
                process_fields(flds)
            except MyError as e:
                # add the filename and propagate further
                raise MyError("input error in '%s' line %d: %s" \
                              % (filename, linenum+1, str(e)))

    except IOError as e:
        raise MyError("failed to read file '%s': %s" % (filename, str(e)))



def print_results():
    for user,value in sums.iteritems():
        print user, "=", value




def main():
    args = parse_command_line()
    process_file(args.filename)
    print_results()





if __name__ == "__main__":
    try:
        main()
    except MyError as e:
        # Prepend program name
        msg = sys.argv[0] + ":" + str(e)
        sys.exit(msg)

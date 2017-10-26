#!/usr/bin/env python2

from argparse import ArgumentParser,RawDescriptionHelpFormatter

ap = ArgumentParser(
    description="Candidate Gene Detection for IK4 project",
    formatter_class=RawDescriptionHelpFormatter,
    epilog="""

This program reads a CSV file with two fields (gene name, patient ID) and prints
the output of possible candidate genes matching the IK4 project criteria.

Example CSV files available at https://example.com/IK4/samples
To learn more about the IK4 project visit https://examples.com/IK4/
Send questions and bug reports to joe@example.com

Usage example:
    $ wget https://example.com/IK4/samples/1.csv
    $ %(prog)s 1.csv > out.txt
""")

ap.add_argument('filename',    # = python variable name
                help="Input CSV file. Expected fields: gene name, sample name",
                metavar="CSV"  # = help screen variable name
		);
args = ap.parse_args()  # Parse the command line
print "Requested file:",args.filename

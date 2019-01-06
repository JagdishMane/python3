#!/usr/bin/env python3.6


import argparse

""" build the parser """
""" Usage
 reverse_file_argparse.py --limit # filename
 reverse_file_argparse.py -l # filename
 """
parser = argparse.ArgumentParser(description='Read a file in reverse')
parser.add_argument('filename', help='the file to read')
parser.add_argument('--limit', '-l', type= int, help='Enter the number of line to read')
parser.add_argument('--version', '-v', action='version', version='%(prog)s 1.0')

args = parser.parse_args()

#print(args)

""" Parse the arguments """

with open(args.filename) as f:
    lines = f.readlines()
    lines.reverse()

    if args.limit:
        lines = lines[:args.limit]

    for line in lines:
        print(line.strip()[::-1])

""" read the file ,  reverse the contents """

#!/usr/bin/env python3

import argparse #argparse standard library for parsing command line arguments
# documentation for argparse:
# https://docs.python.org/3/library/argparse.html?highlight=argparse#module-argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')

args = parser.parse_args()
print(args)

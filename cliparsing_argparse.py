#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('filename', help='the file to read')

args = parser.parse_args()
print(args)

#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser() #build Parser Object; no options needed to pass in currently
parser.add_argument('filename', help="Name of file to read") #call method add_argument to provide arguments to input
args = parser.parse_args()
print(args)

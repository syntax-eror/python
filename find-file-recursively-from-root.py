#!/usr/bin/env python3
import os

path = os.path.abspath(os.sep)

for dirpath, dirs, files in os.walk(path):
    for filename in files:
        fname = os.path.join(dirpath,filename)
        if fname.endswith('.txt'):
            print(fname)

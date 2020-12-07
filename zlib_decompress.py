#!/usr/bin/env python3
#simple script to decompress zlib files
#stolen from awesome SANS instructor Jason Wright, sorry/thanks Jason!

import sys
from zlib import *

indata=open(sys.argv[1], "rb").read()
outdata=decompress(indata)
with open(sys.argv[1] + ".out", "wb") as f:
    f.write(outdata)
    f.close()

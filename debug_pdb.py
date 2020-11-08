#!/usr/bin/env python3

#debugging with pdb

import pdb

def map(func, values):
    output_values = []
    index = 0
    while index < len(values):
        pdb.set_trace() #enter breakpoint for pdb debugger
        output_values = func(values[index])
        index += 1
    return output_values

def add_one(val):
    return val + 1

print(map(add_one, list(range(10))))

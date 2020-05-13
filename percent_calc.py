#!/usr/bin/env python3

#get percentage 1 num (x) is of other num (y)
#

def get_percent(y, z):
    y = y*100
    x = y/z
    return(x)

y = input("Enter first number:")
z = input("Enter second number:")

percent = get_percent(y, z)
print(percent)

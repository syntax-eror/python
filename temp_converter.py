#!/usr/bin/env python3

#F to C = (T(°F) - 32) / 1.8
#C to F = T(°C) × 1.8 + 32

def convert_to_celcius(ftemp):
    return (ftemp - 32) / 1.8

def convert_to_fahrenheit(ctemp):
    return (ctemp * 1.8) + 32

ctemp = float(input("Enter temperature to convert in Celsius: "))
ftemp = float(input("Enter temperature to convert in Fahrenheit: "))

ctof = convert_to_fahrenheit(ctemp)
ftoc = convert_to_celcius(ftemp)

print(ctemp, "in Fahrenheit is", ctof)
print(ftemp, "in Celsius is", ftoc)

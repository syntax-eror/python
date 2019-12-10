#!/usr/bin/env python3

#C to F = T(°C) × 1.8 + 32
#F to C = (T(°F) - 32) / 1.8

def convert_to_celcius(ftemp):
    return (ftemp - 32) / 1.8

def convert_to_fahrenheit(ctemp):
    return (ctemp * 1.8) + 32

ctemp = input("Enter temperature to convert in Celsius:")
ftemp = input("Enter temperature to convert in Fahrenheit:")

converted_ctemp = convert_to_celcius(ftemp)
converted_ftemp = convert_to_fahrenheit(ctemp)

print(ftemp, "in Celsius is", converted_ctemp)
print(ctemp, "in Fah is", converted_ftemp)

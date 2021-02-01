#!/usr/bin/env python3

def convert_mph_to_kmh(speed_in_mph):
    speed_in_kmh = speed_in_mph * .6213712
    return speed_in_kmh

def convert_kmh_to_mph(speed_in_kmh):
    speed_in_mph = speed_in_kmh * 1.609344
    return speed_in_mph

try:
    speed_in_mph = float(input("Enter speed in mph(0 if unknown): "))
    speed_in_kmh = float(input("Enter speed in kmh(0 if unknown): "))
    converted_speed_kmh = convert_mph_to_kmh(speed_in_mph)
    converted_speed_mph = convert_kmh_to_mph(speed_in_kmh)
    print(speed_in_mph, "mph(s) =", round(converted_speed_kmh, 2), "in kmh")
    print(speed_in_kmh, "kmh(s) =", round(converted_speed_mph, 2), "in mph")
except:
    print("Enter a valid numerical speed")
    

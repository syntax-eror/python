#!/usr/bin/env python3

def convert_lb_to_kg(weight_in_lb):
    weight_in_kg = weigh_in_lb * .45359237
    return weight_in_kg
    
def convert_kg_to_lb(weight_in_kg):
    weight_in_lb = weight_in_kg * 2.2046226218488
    return weight_in_lb
    
try:
    weight_in_lb = float(input("Enter weight in lbs(0 if unknown):"))
    weight_in_kg = float(input("Enter weight in kg(0 if unknown):"))
    converted_weight_kg = convert_lb_to_kg(weight_in_lb)
    converted_weight_lb = cconvert_kg_to_lb(weight_in_kg)
    print(weight_in_lb, "lb(s) =", round(converted_weight_kg, 2), "in kg")
    print(weight_in_kg, "kg(s) =", round(converted_weight_lb, 2), "in lb")
except:
    print("Enter a valid numerical weight")
    

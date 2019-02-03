#!/usr/env/python3

#define functions using the format:
#def function_name(variable_to_pass_in):
    #indent code blocks here
    
#importing functions:
#to import specific module from function
from time import localtime, mktime, sleep, strftime
#import module sleep from time

def print_name(name):
    print("Name passed to function is", name)
    
#when this function is called, you will pass an argument to it which it will accept as the name variable:

print_name("Name goes here")

#can also pass in a variable predefined:
name = "This is a predefined variable name"
print_name(name)

#functions and returning variables

def add_two_numbers(num):
    return num + 2

result = add_two_numbers(2) #stores returned value in result variable, but doesn't output
print(result)

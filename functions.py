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

def takeargsandreturn(arg1, arg2):
    print("These are the two arguments that are passed in when function is called:", arg1, arg2)
    newarg = arg1 + arg2
    print("This is a new argument combined from the two passed in and stored as newarg within local scope of function:", newarg)
    print("Returning newarg variable", newarg, " to where it was called")
    return newarg

takeargsandreturn(1, 2)
newargfromfun = takeargsandreturn(1, 2)
print(newargsfromfun)

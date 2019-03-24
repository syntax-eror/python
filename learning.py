#!/usr/bin/python3.6

#variables can use single or double quotes
var1 = "String1"
var2 = 'String2'
var3 = "string3"
int1 = 1

#print function - provide value as argument
print('This is a manually printed string')
print(var1)
print(var2, int1)

#len function returns length
var1_len = len(var1)
print(var1_len)
print(len(var1)) #pass len directly to var1

#methods
print(var1.upper())
#uses method to print var1 string as uppercase

#concat strings
print(var1 + var3)

#repeat
print('A' * 10)

#MORE FUNCTIONS
#str turns non-strings into strings
print(str(var2))

#format method
print('I {} stuff.'.format('eat'))
print('{} {} {}'.format('I', 'like', 'stuff'))
#by default, it prints format args as 0-3

print('This {0} {1}. {0} {1}'.format('a', 'test'))

print('This is going to print {0} '.format(var1, var2))

#providing formatting options to print function
#you can specify width using {#:width}
#below makes a arugment print at least 10 characters wide

print('{0:10} | {1:10}'.format('Variable', 'Quantity'))
print('{0:10} | {1:10}'.format(var1, int1))
print('{0:10} | {1:10}'.format(var3, int2))

#NUMBERS
#math can be done on the fly
#floats will always be decimal

float1 = 4
print(float1)

print(1 + 1)
print(2 * 2)
print(2 ** 16)
print(16 / 2)

#booleans
#true or false
#comparison operators;
# == equal to
# > greater than
# >= or equal to
# < less than
# <=
# != not equal

#boolean operators
# and
# or
# not

print(1 == 2)
print(1 == 1 or 1 == 2)

#tuples - immutable
tuple1 = (2, 3)

#dictionaries - key/value pairs
dictionary1 = {'Key1':2, 'Key2':'SecondKey'}
dictionary1['Key1'] #outputs 2, references value associated with Key1
#dicts are mutable
dictionary1['Key3'] = 'Third Key' #adds third key value pair
#remove keys with del
del dictionary1['Key3']
dictionary1.pop('Key3') #pops Key3, outputs and removes from dict

dictionary1.keys()
dictionary1.values()
dictionary1.items()

#can create dict using lists of tuples
dictionary2 = dict([('Key1', 'Value1'), ('Key2', 'Value2')])

#dict using lists of keys
dictofkeys = ({'key1':1, 'key2':'keyvalue2'})

dictofkeys.keys() #print the keys in the dictionary
dictofkeys.values() #print the values stored

#conditionals
1 in [1, 2, 3]
1 not in [1, 2, 3]


#looping
#while loop
#while True:
    #print('loopin')  #infinite loop
    
count = 1
while count <= 4:
    print('count is currently', count)
    count += 1
    
count = 0
while count < 10:
    if count % 2 == 0: #if count modulo 2, if count is divisible by 2
        count += 1
        continue #specifies for program to go back to top of while loop, otherwise it will just loop within if
    #print(f"We're counting odd numbers: {count}") #string interpolation, doesn't seem to work with my verison of python3
    print("We're counting odd numbers:", count)
        count += 1
        
count = 0
while count < 10:
    if count % 2 == 0: #if count modulo 2, if count is divisible by 2
        break
    print("Counting odd numbers:", count)
    count += 1
    
#for loops
list1 = ['item1', 'item2', 'item3', 'item4']

for item in list1: #item is set up as a temporary variable
    print(item)
    
   
#booleans
name = ""  #name is empty string which evalutes to False as boolean
not name  #this will print true since "name" is false

if not name:
    print("No name given")
else:
    print(name)
    


 

#INITIALIZOR
# _init_ - this is an initializer, sets up objects with values passed when created
# example of creating a class and then calling functions of it:
class bike:
    def __init__ (self, color, frame_material):
        self.color = color
        self.frame_material = frame_material
        
    def brake(self):
        print("Braking!")

red_bike = bike('Red', 'Carbon fiber')
blue_bike = bike('Blue', 'Steel')

print(red_bike.color) #this will print "Red", it calls color object of bike class





# break, continue, and pass are options for loops
condition1 = 10
while condition1 > 0:
    condition1 = condition1 - 1
    if condition1 == 8:
        continue
    elif condition1 == 2:
        break
    else:
        print(condition1)

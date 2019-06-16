#!/usr/bin/python3

#2018-11-04
#last updated 2019-06-15
#Python learning script to give a brother some lööps
#todo list:
#    X-figure out how to do ascii chars - DONE, just use the Alt + keycodes
#        ö - Alt + 0246
#    X-ask for more lööps - DONE, nested if conditional
#    O-error checking for user entering anything other than a number during askForLoops
#    X-move everything into functions for möre streamlined cöde 

from time import sleep #import sleep function from module time - add delay to output

#first function, ask for lööps and print a cat
def askForLoops():
    print()
    sleep(.25)
    print('Bröther may i have some lööps')
    sleep(.25)
    printCatte()

def receiveBoop():
    sleep(.50)
    print('Righteous bröther but what i really need is lööps')
    printCatte()
	
def printCatte():
    sleep(.25)
    print()
    print('    ^  ^       ')
    print('   (O  O)      ')
    print('  { /  \ }     ')
    print(' {I      I}    ')
    print(' {V      V}    ')
    print('  (||  ||)     ')
    print('   ^^  ^^      ')
    print()
    sleep(.25)
	
def receiveLoop():
    sleep(.25)
    print()
    print('Thank you bröther')
    printCatte()
    print()
    sleep(.5)
    print('Would you care to donate another lööp to the cause')
    printCatte()
	
def mainCode(boopsGiven, catteBeg, loopsGiven):
    intuserInput = None
    while loopsGiven < 1 or catteBeg == 1: # as long as you dont give a brother some lööps they're gonna keep asking
        usrInput = input('1 - Give lööp, 2 - Give bööp: ')
        try:
            usrInput = int(usrInput) # remember input is stored as a string, gotta convert it to compare integers
        except:
            print('Gotta use a number bröther')

        if intusrInput == 1:
            loopsGiven += 1  # increment number of l00ps given by one
            receiveLoop()
            usrBeg = str.upper(input('Y/N: '))
            if usrBeg == 'Y':
                catteBeg = 1
                print()
            elif usrBeg == 'N':
                catteBeg = 0
                print()
            else:
                print('Y or N bröther')
                printCatte()
                catteBeg = 1
        elif intusrInput == 2:
            boopsGiven += 1
            receiveBoop()

        else:  #defaults to else catch-all if something else is entered
            sleep(.25)
            print()
            print('bröther why')
            printCatte()
            print()
        print(boopsGiven, catteBeg, loopsGiven)
    return (boopsGiven, catteBeg, loopsGiven)

boopsGiven = 0 # initialize number of boops to 0
catteBeg = 1 # catte starts off begging for loops
loopsGiven = 0 # catte starts off having no lööps, v sad

askForLoops()
(boopsGiven, catteBeg, loopsGiven) = mainCode(boopsGiven, catteBeg, loopsGiven)

if boopsGiven < 1:
    print ('You did not bööp a bröther at all, not even once')
elif boopsGiven == 1:
    print ('You only gave a bröther one bööp')
else:
    print ('{} Bööps were received)'.format(boopsGiven))

if loopsGiven == 1:
    print ('You only hööked a bröther up with one Lööp, do you want him to ŝtārve')
else:
    print ('You gave a bröther {} Lööps, you are a trüe bröther'.format(loopsGiven))

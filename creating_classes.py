#!/usr/bin/env python3
# simple class as example

class Bike:
    """"
    This is a docstring which describes the class
    This class Bike models a bike with engine and tires
    """

    def __init__(self, engine, tires): #methods are functions that are inside classes
        #__ double under - dunder
        """
        Docstring describing the method
        """
        self.engine = engine
        self.tires = tires
        #define the data that will make up the class
        #pass - use pass if you do not implement method currently

    def description(self):
        print(f"A bike with an {self.engine} engine, and {self.tires} tires")

    def wheel_circumference(self):
        if len(self.tires) > 0:
            return self.tires[0].circumference()
        else:
            return 0

#if you run this it will let you create a new object with Bike attribute:
kawi = Bike('636', ['frontwheel', 'rearwheel'])
kawi
kawi.engine
kawi.tires

#!/usr/bin/env python

import sys
import os
import math

def calculateFuelByMass(mass):
    return math.floor(mass / 3) - 2

inputFile = "puzzle1_input.txt"
# inputFile = "puzzle1_example.txt"
totalFuelRequirement = 0

if not os.path.isfile(inputFile):
    print("Input File {} does not exist. Exiting...".format(inputFile))
    sys.exit()

with open(inputFile) as inFile:
    for line in inFile:
        moduleFuel = 0
        line = line.strip('\n')
        moduleMass = int(line)
        moduleFuel = calculateFuelByMass(moduleMass)
        totalFuelRequirement += moduleFuel
        
        while moduleFuel > 0:
            newFuel = calculateFuelByMass(moduleFuel)
            if (newFuel > 0):
                totalFuelRequirement += newFuel
                moduleFuel = newFuel
            else:
                break

print("Total fuel required is {}".format(totalFuelRequirement))



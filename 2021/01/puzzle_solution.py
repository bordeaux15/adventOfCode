#!/usr/bin/env python

import sys
import os
import math

relPath = "2021/01/"
# inputFile = relPath + "sample.txt"
inputFile = relPath + "input.txt"

if not os.path.isfile(inputFile):
    print("Input File {} does not exist. Exiting...".format(inputFile))
    sys.exit()

depths = []
increasedSingle = 0
increasedWindow = 0
sumPrevious = 0
sumCurrent = 0


with open(inputFile) as inFile:
    for line in inFile:
        depths.append((int (line)))

for i in range(len(depths) - 1):
    if (depths[i+1] > depths[i]):
        increasedSingle += 1

print("Increasing values: {}".format(increasedSingle)) 

for i in range(len(depths) - 2):
    sumCurrent = depths[i+2]+depths[i+1]+depths[i]
    if (i != 0):
        if (sumCurrent > sumPrevious):
            increasedWindow += 1
    
    sumPrevious = sumCurrent

print("Increasing Window: {}".format(increasedWindow))


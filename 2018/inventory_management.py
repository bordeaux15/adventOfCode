#!/usr/bin/env python

import sys
import os
import re

# inputFile = "puzzle2_input.txt"
inputFile = "puzzle2_example.txt"

#These regex patterns will match characters repeated one after another either twice or 3 times
#Requires the matching string to be sorted for this puzzle
rePattern = r"([a-z])\1\1?"
doubleMatch = 0
tripleMatch = 0
checkSum = 0

if not os.path.isfile(inputFile):
    print("Input File {} does not exist. Exiting...".format(inputFile))
    sys.exit()

with open(inputFile) as inFile:
    for line in inFile:
        line = line.strip('\n')
        sortedLine = ''.join(sorted(line))
        match = re.search(rePattern, sortedLine)
        if match:
            print("match is: {}".format(match.group()))

checkSum = doubleMatch * tripleMatch

print("doubleMatch is {}".format(doubleMatch))
print("tripleMatch is {}".format(tripleMatch))
print("checksum is {}".format(checkSum))
        

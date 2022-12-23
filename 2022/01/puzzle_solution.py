#!/usr/bin/env python

import sys
import os
import math

relPath = "2022/01/"
# inputFile = relPath + "sample.txt"
inputFile = relPath + "puzzle_input.txt"

elves = []
elfCount = 0
topElves = 3
topCountSum = 0
elfSum = 0
maxSum = 0
maxElf = 0

if not os.path.isfile(inputFile):
    print("Input File {} does not exist. Exiting...".format(inputFile))
    sys.exit()

with open(inputFile) as inFile:
    for line in inFile:
        if line.strip():
            elfSum += int(line)
        else:
            elfCount += 1
            if elfSum > maxSum:
                elves.append(elfSum)
            elfCount += 1
            elfSum = 0

elves.sort(reverse=True)

maxSum = elves[0]
for i in range(topElves):
    print("Elf Count " + str(elves[i]))
    topCountSum += elves[i]

print("Max Calorie Count: " + str(maxSum))
print("Top " + str(topElves) + " Calorie Count: " + str(topCountSum))

        
#!/usr/bin/env python

import sys
import os
import math

def intcodeCompute(computeList):
    # print(computeList)
    instructionPtr = 0
    while (instructionPtr < (len(computeList) - 1)):
        instruction = computeList[instructionPtr]

        if (instruction == 1):
            result = computeList[computeList[instructionPtr+1]] + computeList[computeList[instructionPtr+2]] 
        elif (instruction == 2):
            result = computeList[computeList[instructionPtr+1]] * computeList[computeList[instructionPtr+2]] 
        else:
            break

        computeList[computeList[instructionPtr+3]] = result
        instructionPtr += 4

    return computeList

inputFile = "puzzle2_input.txt"
# inputFile = "puzzle2_example.txt"
noun = 0
resultFound = 0
maxValue = 99
testValue = 19690720

if not os.path.isfile(inputFile):
    print("Input File {} does not exist. Exiting...".format(inputFile))
    sys.exit()

with open(inputFile) as inFile:
    for line in inFile:
        line = line.strip('\n')
        initialList = line.split(',')

#change all list elements to int
initialList = list(map(int, initialList))

while (noun < maxValue):
    verb = 0
    while (verb < maxValue):
        tempList = initialList.copy()
        tempList[1] = noun
        tempList[2] = verb
        resultList = intcodeCompute(tempList.copy())
        if (resultList[0] == testValue):
            resultFound = 1
            break
        verb += 1
    if (resultFound == 1):
        break
    noun += 1
        
print(resultList[0])
print("Noun = {}".format(noun))
print("Verb = {}".format(verb))
print("Final Answer = {}".format((100*noun)+verb))





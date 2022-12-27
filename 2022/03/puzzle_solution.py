#!/usr/bin/env python

import sys
import os
import math

relPath = "2022/03/"
# inputFile = relPath + "sample.txt"
inputFile = relPath + "puzzle_input.txt"

def main():
    duplicates = []
    groupsOfThree = []
    sum = 0
    sum2 = 0
    if not os.path.isfile(inputFile):
        print("Input File {} does not exist. Exiting...".format(inputFile))
        sys.exit()

    inFile = open(inputFile, 'r')
    lines = inFile.read().splitlines()
    inFile.close()
    
    for line in lines:
        lineCount = 0

        groupsOfThree.append(set(line))
        midpoint = int((len(line))/2)
        c1 = line[slice(0, midpoint)]
        c2 = line[slice(midpoint, len(line))]
        duplicates.append(findMatch(c1,c2))

    for i in duplicates:
        sum += priority(i)

    print("Part 1 answer: " + str(sum))

    for i in range(0, len(groupsOfThree), 3):
        shared = (groupsOfThree[i].intersection(groupsOfThree[i+1], groupsOfThree[i+2]))
        sum2 += priority("".join(shared))
    
    print("Part 2 answer: " + str(sum2))



def findMatch(str1, str2):
    for char in str1:
        if str2.find(char) >= 0:
            return char

def priority(char):
    if str.isupper(char):
        return int(ord(char) - 38)
    else:
        return int(ord(char) - 96)


if __name__ == "__main__":
    main()
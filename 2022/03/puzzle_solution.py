#!/usr/bin/env python

import sys
import os
import math

relPath = "2022/03/"
# inputFile = relPath + "sample.txt"
inputFile = relPath + "puzzle_input.txt"

def main():
    duplicates = []
    sum = 0
    if not os.path.isfile(inputFile):
        print("Input File {} does not exist. Exiting...".format(inputFile))
        sys.exit()

    with open(inputFile) as inFile:
        for line in inFile:
            line.strip()
            midpoint = int((len(line)-1)/2)
            c1 = line[slice(0, midpoint)]
            c2 = line[slice(midpoint, len(line)-1)]
            duplicates.append(findMatch(c1,c2))

        for i in duplicates:
            sum += priority(i)

        print(sum)


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
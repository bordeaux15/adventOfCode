#!/usr/bin/env python

import sys
import os
import math

inputFile = "puzzle3_input.txt"
# inputFile = "puzzle3_example.txt"

if not os.path.isfile(inputFile):
    print("Input File {} does not exist. Exiting...".format(inputFile))
    sys.exit()

rows = 1000
rows, cols = (1000,1000)
wireBoard = [[0 for i in range(cols)] for j in range(rows)]

centralPointX = rows/2
centralPointY = rows/2

with open(inputFile) as inFile:
    for line in inFile:
        line = line.strip('\n')
        initialList = line.split(',')

       





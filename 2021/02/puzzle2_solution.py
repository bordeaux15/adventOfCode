import sys
import os
import math

relPath = "2021/02/"
# inputFile = relPath + "sample.txt"
inputFile = relPath + "puzzle2_input.txt"

horizontalPos = 0
depth = 0
aim = 0

if not os.path.isfile(inputFile):
    print("Input File {} does not exist. Exiting...".format(inputFile))
    sys.exit()

with open(inputFile) as inFile:
    for line in inFile:
        commands = line.split()
        if (commands[0] == "forward"):
            horizontalPos += int (commands[1])
            depth += aim * int (commands[1])
            next
        if (commands[0] == "down"):
            # depth += int(commands[1])
            aim += int(commands[1])
            next
        if (commands[0] == "up"):
            # depth -= int(commands[1])
            aim -= int(commands[1])
            next

print("horizontal position is: {}".format(horizontalPos))
print("depth is:   {}".format(depth))
print("Answer is: {}".format(horizontalPos*depth))
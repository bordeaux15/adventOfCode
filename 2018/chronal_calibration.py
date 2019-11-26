#!/usr/bin/env python

import sys
import os

inputFile = sys.argv[1]
frequency = 0;
frequencyLoop = 0;
frequencyDuplicate = 0;
frequencyAdjustments = []
frequencyList = []

if not os.path.isfile(inputFile):
    print("Input File {} does not exist. Exiting...".format(inputFile))
    sys.exit()

with open(inputFile) as inFile:
    for line in inFile:
        line = line.strip('\n')
        freqAdjust = int(line)
        frequencyAdjustments.append(freqAdjust)


    while frequencyDuplicate == 0:
        frequencyLoop += 1
        for freqAdjust in frequencyAdjustments:
            frequency += freqAdjust
            # print("FrequencyDuplicate = {}".format(frequencyDuplicate))
            # print("Frequency = {}".format(frequency))
            if frequency not in frequencyList:
                frequencyList.append(frequency)
                # print (*frequencyList)
            else:
                frequencyDuplicate = 1
                break

            # print("Frequency Adjust = {}".format(freqAdjust))

    print("Frequency repeated is {}".format(frequency))
    print("Looped {} times".format(frequencyLoop))

    # print("Final Frequency is {}".format(frequency))

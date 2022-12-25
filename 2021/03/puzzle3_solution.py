import sys
import os
import math
import array

def binaryToDecimal(array):
    decimal = 0
    power = len(array) - 1
    for i in range(len(array)):
        decimal += 2**(power-i) * int(array[i])
    
    return decimal

def filterArray(array, criteria, pos):
    tempArray = []
    if (len(array) != 1):
        for i in range(len(array)):
            if (array[i][pos] == criteria):
                tempArray.append(array[i])

    return tempArray


relPath = "2021/03/"
inputFile = relPath + "sample.txt"
# inputFile = relPath + "puzzle3_input.txt"

bitsArray = []
gammaBits = []
gammaRate = 0
epsilonBits = []
epsilonRate = 0
o2Bits = []
o2GenArray = []
o2GenRate = 0
co2Bits = []
co2ScrubArray = []
co2ScrubRate = 0

if not os.path.isfile(inputFile):
    print("Input File {} does not exist. Exiting...".format(inputFile))
    sys.exit()

with open(inputFile) as inFile:
    for line in inFile:
        bits = list(line.strip('\n'))
        o2GenArray.append(bits)
        co2ScrubArray.append(bits)
        
        for i in range(len(bits)):
            if (len(bitsArray) < len(bits)):
                bitsArray.append(0)
            if (bits[i] == "0"):
                bitsArray[i] -= 1
            else:
                bitsArray[i] += 1

for i in range(len(bitsArray)):
    if bitsArray[i] >= 0:
        gammaBits.append('1')
        epsilonBits.append('0')
        o2Bits.append('1')
        co2Bits.append('0')
    else:
        gammaBits.append('0')
        epsilonBits.append('1')
        o2Bits.append('0')
        co2Bits.append('1')
         

gammaRate = binaryToDecimal(gammaBits)
epsilonRate = binaryToDecimal(epsilonBits)

for i in range(len(o2Bits)):
    o2GenArray = filterArray(o2GenArray, o2Bits[i], i)

o2GenRate = binaryToDecimal(o2GenArray[0])

for i in range(len(co2Bits)):
    co2ScrubArray = filterArray(co2ScrubArray, co2Bits[i], i)

co2ScrubRate = binaryToDecimal(co2ScrubArray[0])


print ("Gamma Rate is:   {}".format(gammaRate))
print (gammaBits)
print ("Epsilon Rate is: {}".format(epsilonRate))
print (epsilonBits)
print ("Power Consumption is: {}".format(gammaRate*epsilonRate))
print ("O2 Gen Rate is:  {}".format(o2GenRate))
print ("CO2 Scrub Rate is: {}".format(co2ScrubRate))
print ("Life Support Rating is: {}".format(o2GenRate*co2ScrubRate))


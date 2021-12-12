import sys
import os
import math

def binaryToDecimal(array):
    decimal = 0
    power = len(array) - 1
    for i in range(len(array)):
        decimal += pow(2,(power-i)) * int(array[i])
    
    return decimal

relPath = "2021/03/"
# inputFile = relPath + "sample.txt"
inputFile = relPath + "puzzle3_input.txt"

bitsArray = []
gammaBits = []
gammaRate = 0
epsilonBits = []
epsilonRate = 0

if not os.path.isfile(inputFile):
    print("Input File {} does not exist. Exiting...".format(inputFile))
    sys.exit()

with open(inputFile) as inFile:
    for line in inFile:
        bits = list(line.strip('\n'))
        for i in range(len(bits)):
            if (len(bitsArray) < len(bits)):
                bitsArray.append(0)
            if (bits[i] == "0"):
                bitsArray[i] -= 1
            else:
                bitsArray[i] += 1

for i in range(len(bitsArray)):
    if bitsArray[i] > 0:
        gammaBits.append(1)
        epsilonBits.append(0)
    else:
        gammaBits.append(0)
        epsilonBits.append(1)

gammaRate = binaryToDecimal(gammaBits)
epsilonRate = binaryToDecimal(epsilonBits)

print ("Gamma Rate is:   {}".format(gammaRate))
print (gammaBits)
print ("Epsilon Rate is: {}".format(epsilonRate))
print (epsilonBits)
print ("Power Consumption is: {}".format(gammaRate*epsilonRate))


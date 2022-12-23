#!/usr/bin/env python

import sys
import os
import math

relPath = "2022/02/"
# inputFile = relPath + "sample.txt"
inputFile = relPath + "puzzle_input.txt"



def main():
    totalScore = 0

    if not os.path.isfile(inputFile):
        print("Input File {} does not exist. Exiting...".format(inputFile))
        sys.exit()

    with open(inputFile) as inFile:
        for line in inFile:
            symbols = line.split()
            elfSymbol = symbolNames(symbols[0])
            # mySymbol = symbolNames(symbols[1])
            myResult = resultNames(symbols[1])
            mySymbol = resultSymbol(myResult, elfSymbol)
            totalScore += symbolScore(mySymbol)
            totalScore += outcomeScore(mySymbol, elfSymbol)
            
    print("Total Score " + str(totalScore))

def symbolNames(symbol):
    name = {
        'A': "rock",
        'X': "rock",
        'B': "paper",
        'Y': "paper",
        'C': "scissors",
        'Z': "scissors"
    }
    return name.get(symbol, 0)

def resultNames(symbol):
    name = {
        'X': "lose",
        'Y': "draw",
        'Z': "win"
    }
    return name.get(symbol, 0)

def symbolScore(symbol):
    scores = {
        "rock": 1,
        "paper": 2,
        "scissors": 3
    }
    return scores.get(symbol, 0)

def resultSymbol(result, symbol):
    
    if (symbol == "rock"):
        if (result == "win"):
            return "paper"
        elif (result == "lose"):
            return "scissors"
        else:
            return symbol 
    elif (symbol == "paper"):
        if (result == "win"):
            return "scissors"
        elif (result == "lose"):
            return "rock"
        else:
            return symbol
    else:
        if (result == "win"):
            return "rock"
        elif (result == "lose"):
            return "paper"
        else:
            return symbol
        

def outcomeScore(symbol1, symbol2):
    result = 0
    win = 6
    draw = 3
    loss = 0

    if (symbol1 == "rock"): 
        if symbol2 == "scissors":
            result = win
        elif symbol2 == "rock":
            result = draw
    elif (symbol1 == "scissors"):
        if symbol2 == "paper":
            result = win
        elif symbol2 == "scissors":
            result = draw
    elif (symbol1 == "paper"):
        if symbol2 == "rock":
            result = win
        elif symbol2 == "paper":
            result = draw
    
    return result


if __name__ == "__main__":
    main()

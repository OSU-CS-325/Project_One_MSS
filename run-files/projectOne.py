# Program:              projectOne.py (Python)
# Author:               Cash Stramel
# OSU Email:            stramelm@onid.oregonstate.edu
# Class/Section:        CS325-400
# Due Date:             October 2016
# Program Description:  Master program designed to launch test cases,
#                       experimental analyses, and problem solutions on four
#                       different Maximum Sum Subarray algorithms.  Coded in
#                       Python and designed to run on Oregon State University's
#                       'flip' servers.

import datetime
import random
import sys

import testAlg # remove before turning in
from testAlg import testAlg

sys.path.insert(0, "./../enumeration")
import alg1

sys.path.insert(0, "./../better-enumeration")
import alg2

sys.path.insert(0, "./../divide-and-conquer")
import alg3

sys.path.insert(0, "./../linear-time")
import alg4

def randomList(size):
#-------------------------------------------------------------------------------
# Description:      Generates list of integers of length=size.
#                   Integers will be between -99 and 99 (inclusive) and at
#                   least one of them will be positive (1 to 99).
# Receives:         Size of list to randomly generate.
# Returns:          List.
# Preconditions:    Size >= 1.
# ------------------------------------------------------------------------------
    posFound = False
    while not (posFound):
        retList = []
        for i in range(0, size):
            retList.append(random.randint(-99, 99))
        for i in range(0, size):
            if retList[i] > 0:
                posFound = True
                break
    return retList


def printAlgorithmIO(inputList, outputList, outputValue, outFil):
#-------------------------------------------------------------------------------
# Description:      Prints the results from a call to an algorithm function.
# Receives:         inputList, outputList, outputValue, outFil
# Returns:          Nothing.
# Preconditions:    Inputs are expected to be non-null.
# ------------------------------------------------------------------------------

    outFil.write("input array:      " + str(inputList))
    outFil.write("\n")
    outFil.write("max sum subarray: " + str(outputList))
    outFil.write("\n")
    outFil.write("maximum sum:      " + str(outputValue))
    outFil.write("\n")
    outFil.write("\n")
    

def runInputsThru(inFil, outFil):
#-------------------------------------------------------------------------------
# Description:      Does the real work of running inputs through algorithms.
# Receives:         File handles with input files to draw cases from and output
#                   files to write them to.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------

    # read contents of test problems into list of lists
    testLists = []
    for line in inFil:
        nextList = []
        nextLine = line.rstrip('\r\n').replace('[', '')
        nextLine = nextLine.replace(']', '').replace(',', ' ').split()
        if len(nextLine) > 0:
            testLists.append([int(i) for i in nextLine])

    # iterate through input for each algorithm
    for i in range(1, 6): # replace 6 with 5 later
        if i == 1:
            outFil.write("---- enumeration ----------------------------------")
            outFil.write("\n")
            outFil.write("\n")

            #for j in range(len(testLists)):
            #    retVal, retList = insertfunctionname(testLists[j])
            #    printAlgorithmIO(testLists[j], retList, retVal, outFil)
                
        elif i == 2:
            outFil.write("---- better-enumeration ---------------------------")
            outFil.write("\n")
            outFil.write("\n")

            #for j in range(len(testLists)):
            #    retVal, retList = insertfunctionname(testLists[j])
            #    printAlgorithmIO(testLists[j], retList, retVal, outFil)
                
        elif i == 3:
            outFil.write("---- divide-and-conquer----------------------------")
            outFil.write("\n")
            outFil.write("\n")

            #for j in range(len(testLists)):
            #    retVal, retList = insertFunctionName(testLists[j])
            #    printAlgorithmIO(testLists[j], retList, retVal, outFil)
                
        elif i == 4:
            outFil.write("---- linear-time ----------------------------------")
            outFil.write("\n")
            outFil.write("\n")

            #for j in range(len(testLists)):
            #    retVal, retList = insertFunctionName(testLists[j])
            #    printAlgorithmIO(testLists[j], retList, retVal, outFil)
                
        else:
            outFil.write("---- test -----------------------------------------")
            outFil.write("\n")
            outFil.write("\n")

            for j in range(len(testLists)):
                retVal, retList = testAlg(testLists[j])
                printAlgorithmIO(testLists[j], retList, retVal, outFil)


def runTestCases():
#-------------------------------------------------------------------------------
# Description:      Runs test cases.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------

    inFil = open("MSS_TestProblems.txt", 'r')
    outFil = open("MSS_TestResults.txt", 'w')

    runInputsThru(inFil, outFil)

    inFil.close()
    outFil.close()

                
def solveProblems():
#-------------------------------------------------------------------------------
# Description:      Solves assigned problems.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------

    inFil = open("MSS_Problems.txt", 'r')
    outFil = open("MSS_Results.txt", 'w')

    runInputsThru(inFil, outFil)

    inFil.close()
    outFil.close()


def runExperimentalAnalysis():
#-------------------------------------------------------------------------------
# Description:      Runs experimental analysis.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------
    print "runExperimentalAnalysis"


def main():
#-------------------------------------------------------------------------------
# Description:      Main function which launches test cases, experimental
#                   analyses, and problem solutions.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------
    
    runTestCases()
    solveProblems()
    #runExperimentalAnalysis

    randomList(2)
    randomList(4)    
    randomList(8)
    randomList(16)

    # dummy call just to demo how to pass args to and get return values
    #myList = [31,-41,59,26,-53,58,97,-93,-23,84] 
    #retVal, retList = testAlg(myList)

    #print "retVal = " + str(retVal)
    #print "retList = " + str(retList)

# ------------------------------------------------------------
if __name__ == "__main__":
    main()

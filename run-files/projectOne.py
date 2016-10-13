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

import testAlg 
from testAlg import testAlg

sys.path.insert(0, "./../enumeration")
import alg1

sys.path.insert(0, "./../better-enumeration")
import alg2
from alg2 import betterEnumeration

sys.path.insert(0, "./../divide-and-conquer")
import alg3

sys.path.insert(0, "./../linear-time")
import alg4
from alg4 import linearTime

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


def printAlgorithmIO(inputList, outputList, outputValue, runTime, outFil):
#-------------------------------------------------------------------------------
# Description:      Prints the results from a call to an algorithm function.
# Receives:         inputList, outputList, outputValue, runTime (mu-s), outFil
# Returns:          Nothing.
# Preconditions:    Inputs are expected to be non-null.
#                   outFil is open for writing.
# ------------------------------------------------------------------------------

    outFil.write("input array:        " + str(inputList))
    outFil.write("\n")
    outFil.write("input size:         " + str(len(inputList)))
    outFil.write("\n")
    outFil.write("max sum subarray:   " + str(outputList))
    outFil.write("\n")
    outFil.write("maximum sum:        " + str(outputValue))
    outFil.write("\n")
    outFil.write("runtime (microsec): " + str(runTime))
    outFil.write("\n")
    outFil.write("\n")
    

def runInputsThru(inFil, outFil, algsToRun):
#-------------------------------------------------------------------------------
# Description:      Does the real work of running inputs through algorithms.
# Receives:         File handles with input files to draw cases from and output
#                   files to write them to.
#
#                   algsToRun is a 5 bit binary number, each bit is assigned to
#                   an algorithm, and setting it to 1 means "run this algorithm"
#
#                    left-most bit: enumeration
#                         next bit: better-enumeration                   
#                         next bit: divide-and-conqure
#                         next bit: linear-time
#                   right-most bit: test-debug
#
#                   ex. 0b11111 (run all)
#                   ex. 0b10011 (run enum, linear, and test)
#                   ex. 0b01100 (run better-enum, d-and-c)
#                   
# Returns:          Nothing.
# Preconditions:    inFil is open for reading.  outFil is open for writing.
# ------------------------------------------------------------------------------

    # read contents of test problems into list of lists
    testLists = []
    for line in inFil:
        nextList = []
        nextLine = line.rstrip('\r\n').replace('[', '')
        nextLine = nextLine.replace(']', '').replace(',', ' ').split()
        if len(nextLine) > 0:
            testLists.append([int(i) for i in nextLine])

    if (algsToRun & 0b10000):
        outFil.write("---- enumeration ----------------------------------")
        outFil.write("\n")
        outFil.write("\n")

        #for j in range(len(testLists)):
        #    start = datetime.datetime.now()
        #    retVal, retList = insertfunctionname(testLists[j])
        #    end = datetime.datetime.now()
        #    delta = end - start
        #    delta = int(delta.total_seconds() * 1000000) 
        #    printAlgorithmIO(testLists[j], retList, retVal, delta, outFil)
                
    if (algsToRun & 0b01000):
        outFil.write("---- better-enumeration ---------------------------")
        outFil.write("\n")
        outFil.write("\n")

        for j in range(len(testLists)):
            start = datetime.datetime.now()
            retVal, retList = betterEnumeration(testLists[j])
            end = datetime.datetime.now()
            delta = end - start
            delta = int(delta.total_seconds() * 1000000) 
            printAlgorithmIO(testLists[j], retList, retVal, delta, outFil)
                
    if (algsToRun & 0b00100):
        outFil.write("---- divide-and-conquer----------------------------")
        outFil.write("\n")
        outFil.write("\n")

        #for j in range(len(testLists)):
        #    start = datetime.datetime.now()
        #    retVal, retList = insertFunctionName(testLists[j])
        #    end = datetime.datetime.now()
        #    delta = end - start
        #    delta = int(delta.total_seconds() * 1000000) 
        #    printAlgorithmIO(testLists[j], retList, retVal, delta, outFil)
                
    if (algsToRun & 0b00010):
        outFil.write("---- linear-time ----------------------------------")
        outFil.write("\n")
        outFil.write("\n")

        for j in range(len(testLists)):
            start = datetime.datetime.now()
            retVal, retList = linearTime(testLists[j])
            end = datetime.datetime.now()
            delta = end - start
            delta = int(delta.total_seconds() * 1000000) 
            printAlgorithmIO(testLists[j], retList, retVal, delta, outFil)
                
    if (algsToRun & 0b00001):
        outFil.write("---- test-debug------------------------------------")
        outFil.write("\n")
        outFil.write("\n")

        for j in range(len(testLists)):
            start = datetime.datetime.now()
            retVal, retList = testAlg(testLists[j])
            end = datetime.datetime.now()
            delta = end - start
            delta = int(delta.total_seconds() * 1000000) 
            printAlgorithmIO(testLists[j], retList, retVal, delta, outFil)


def runTestCases():
#-------------------------------------------------------------------------------
# Description:      Runs test cases.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------

    inFil = open("MSS_TestProblems.txt", 'r')
    outFil = open("MSS_TestResults.txt", 'w')

    runInputsThru(inFil, outFil, 0b11111)

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

    runInputsThru(inFil, outFil, 0b11111)

    inFil.close()
    outFil.close()


def runExperiment():
#-------------------------------------------------------------------------------
# Description:      Runs 'experiment' part of experimental analysis.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------
    
    #---- enumeration ----------------------------------
    # create input file with random inputs
    name = "ExpAnlys_enumeration"
    randFil = open("MSS_" + name + ".txt", 'w')
    n = 10
    for i in range(0, 10):
        for j in range(0, 10):
            randFil.write(str(randomList(n)))
            randFil.write("\n")
        n += 10
    randFil.close()

    # run algorithm(s) with random inputs
    inFil = open("MSS_" + name + ".txt", 'r')
    outFil = open("MSS_" + name + "_Results.txt", 'w')

    runInputsThru(inFil, outFil, 0b10000)

    inFil.close()

    #---- better-enumeration ---------------------------
    # create input file with random inputs
    name = "ExpAnlys_better-enumeration"
    randFil = open("MSS_" + name + ".txt", 'w')
    n = 10
    for i in range(0, 10):
        for j in range(0, 10):
            randFil.write(str(randomList(n)))
            randFil.write("\n")
        n += 10
    randFil.close()

    # run algorithm(s) with random inputs
    inFil = open("MSS_" + name + ".txt", 'r')
    outFil = open("MSS_" + name + "_Results.txt", 'w')

    runInputsThru(inFil, outFil, 0b01000)

    inFil.close()

    #---- divide-and-conquer----------------------------
    # create input file with random inputs
    name = "ExpAnlys_divide-and-conquer"
    randFil = open("MSS_" + name + ".txt", 'w')
    n = 10
    for i in range(0, 10):
        for j in range(0, 10):
            randFil.write(str(randomList(n)))
            randFil.write("\n")
        n += 10
    randFil.close()

    # run algorithm(s) with random inputs
    inFil = open("MSS_" + name + ".txt", 'r')
    outFil = open("MSS_" + name + "_Results.txt", 'w')

    runInputsThru(inFil, outFil, 0b00100)

    inFil.close()

    #---- linear-time ----------------------------------
    # create input file with random inputs
    name = "ExpAnlys_linear-time"
    randFil = open("MSS_" + name + ".txt", 'w')
    n = 10
    for i in range(0, 10):
        for j in range(0, 10):
            randFil.write(str(randomList(n)))
            randFil.write("\n")
        n += 10
    randFil.close()

    # run algorithm(s) with random inputs
    inFil = open("MSS_" + name + ".txt", 'r')
    outFil = open("MSS_" + name + "_Results.txt", 'w')

    runInputsThru(inFil, outFil, 0b00010)

    inFil.close()

    #---- test-debug------------------------------------
    # create input file with random inputs
    name = "ExpAnlys_test-debug"
    randFil = open("MSS_" + name + ".txt", 'w')
    n = 10
    for i in range(0, 10):
        for j in range(0, 10):
            randFil.write(str(randomList(n)))
            randFil.write("\n")
        n += 10
    randFil.close()

    # run algorithm(s) with random inputs
    inFil = open("MSS_" + name + ".txt", 'r')
    outFil = open("MSS_" + name + "_Results.txt", 'w')

    runInputsThru(inFil, outFil, 0b00001)

    inFil.close()


def analysisHelper(sumFil, resFil):
#-------------------------------------------------------------------------------
# Description:      Reads/average results and writes them to summary.
# Receives:         File handles for summary file and results file.
# Returns:          Nothing.
# Preconditions:    Files are open for writing.
# ------------------------------------------------------------------------------

    algName = resFil.name.replace("MSS_ExpAnlys_","").replace("_Results.txt","")

    results = []
    for line in resFil:
        if (line[:7] == "input a"):
            result = []
        if (line[:7] == "input s"):
            result.append(int(line[20:])) 
        if (line[:7] == "runtime"):
            result.append(int(line[20:])) 
            results.append(result)

    results = sorted(results, key=lambda x: (x[0], x[1]))

    n = -1
    sum = 0
    runTimes = []
    for result in results:
        if (n != result[0]):
            if (len(runTimes) > 0):
                sumFil.write(algName)
                sumFil.write(",")
                sumFil.write(str(n))
                sumFil.write(",")
                sumFil.write(str(sum / float(len(runTimes))))
                sumFil.write(",")
                sumFil.write(str(runTimes).replace(",", " "))
                sumFil.write("\n")
            n = result[0]
            runTimes = []
            sum = 0
        runTimes.append(result[1])
        sum += result[1]
        
    if (len(runTimes) > 0):
        sumFil.write(algName)
        sumFil.write(",")
        sumFil.write(str(n))
        sumFil.write(",")
        sumFil.write(str(sum / float(len(runTimes))))
        sumFil.write(",")
        sumFil.write(str(runTimes).replace(",", " "))
        sumFil.write("\n")
  
 
def runAnalysis():
#-------------------------------------------------------------------------------
# Description:      Runs 'analysis' part of experimental analysis.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------
   
    sumFil = open("MSS_ExpAnlys_Summary.csv", 'w')
    sumFil.write("algorithm,n,averageRunTime,allRunTimes\n")
 
    #---- enumeration ----------------------------------
    name = "ExpAnlys_enumeration"
    resFil = open("MSS_" + name + "_Results.txt", 'r')
    analysisHelper(sumFil, resFil)
    resFil.close()

    #---- better-enumeration ---------------------------
    name = "ExpAnlys_better-enumeration"
    resFil = open("MSS_" + name + "_Results.txt", 'r')
    analysisHelper(sumFil, resFil)
    resFil.close()

    #---- divide-and-conquer----------------------------
    name = "ExpAnlys_divide-and-conquer"
    resFil = open("MSS_" + name + "_Results.txt", 'r')
    analysisHelper(sumFil, resFil)
    resFil.close()

    #---- linear-time ----------------------------------
    name = "ExpAnlys_linear-time"
    resFil = open("MSS_" + name + "_Results.txt", 'r')
    analysisHelper(sumFil, resFil)
    resFil.close()

    #---- test-debug------------------------------------
    name = "ExpAnlys_test-debug"
    resFil = open("MSS_" + name + "_Results.txt", 'r')
    analysisHelper(sumFil, resFil)
    resFil.close()

    sumFil.close()


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
    runExperiment()
    runAnalysis()

    # dummy calls to test randomList function
    #randomList(2)
    #randomList(4)    
    #randomList(8)
    #randomList(16)

    # dummy call just to demo how to pass args to and get return values
    #myList = [31,-41,59,26,-53,58,97,-93,-23,84] 
    #retVal, retList = testAlg(myList)

    #print "retVal = " + str(retVal)
    #print "retList = " + str(retList)

# ------------------------------------------------------------
if __name__ == "__main__":
    main()

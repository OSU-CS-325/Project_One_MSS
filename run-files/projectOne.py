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
from alg1 import enumeration

sys.path.insert(0, "./../better-enumeration")
import alg2
from alg2 import betterEnumeration

sys.path.insert(0, "./../divide-and-conquer")
import alg3
from alg3 import enumer_d_and_c

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

        for j in range(len(testLists)):
            start = datetime.datetime.now()
            retVal, retList = enumeration(testLists[j])
            end = datetime.datetime.now()
            delta = end - start
            delta = int(delta.total_seconds() * 1000000) 
            printAlgorithmIO(testLists[j], retList, retVal, delta, outFil)
                
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

        for j in range(len(testLists)):
            start = datetime.datetime.now()
            retVal, retList = enumer_d_and_c(testLists[j])
            end = datetime.datetime.now()
            delta = end - start
            delta = int(delta.total_seconds() * 1000000) 
            printAlgorithmIO(testLists[j], retList, retVal, delta, outFil)
                
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


def runInputsThruNoFil(inputList, algToRun):
#-------------------------------------------------------------------------------
# Description:      Simpler version of runInputsThru with no I/O. 
# Receives:         List of integers.
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
#                   NOTE: IN THIS VERSION ONLY THE LEFT-MOST 1 BIT IS USED
#                         ONLY ONE ALGORITHM WILL BE RUN AT A TIME
#
#                   ex. 0b11111 (run enum)
#                   ex. 0b10011 (run enum)
#                   ex. 0b01100 (run better-enum)
#                   ex. 0b00010 (run linear-time)
#                   
# Returns:          Time to run algorithm in microseconds.
# Preconditions:    Input list shouldn't be empty.
# ------------------------------------------------------------------------------

    if (algToRun & 0b10000):
        #outFil.write("---- enumeration ----------------------------------")

        start = datetime.datetime.now()
        retVal, retList = enumeration(inputList)
        end = datetime.datetime.now()
        delta = end - start
        delta = int(delta.total_seconds() * 1000000) 
        print str(algToRun)           #debug only
        print str(len(inputList))     #debug only            
        print str(start)              #debug only
        print str(end)                #debug only
        print str(delta / 1000000)    #debug only
        return delta
                
    elif (algToRun & 0b01000):
        #outFil.write("---- better-enumeration ---------------------------")

        start = datetime.datetime.now()
        retVal, retList = betterEnumeration(inputList)
        end = datetime.datetime.now()
        delta = end - start
        delta = int(delta.total_seconds() * 1000000) 
        print str(algToRun)           #debug only
        print str(len(inputList))     #debug only            
        print str(start)              #debug only
        print str(end)                #debug only
        print str(delta / 1000000)    #debug only
        return delta
                
    elif (algToRun & 0b00100):
        #outFil.write("---- divide-and-conquer----------------------------")

        start = datetime.datetime.now()
        retVal, retList = enumer_d_and_c(inputList)
        end = datetime.datetime.now()
        delta = end - start
        delta = int(delta.total_seconds() * 1000000) 
        print str(algToRun)           #debug only
        print str(len(inputList))     #debug only            
        print str(start)              #debug only
        print str(end)                #debug only
        print str(delta / 1000000)    #debug only
        return delta
                
    elif (algToRun & 0b00010):
        #outFil.write("---- linear-time ----------------------------------")

        start = datetime.datetime.now()
        retVal, retList = linearTime(inputList)
        end = datetime.datetime.now()
        delta = end - start
        delta = int(delta.total_seconds() * 1000000)
        print str(algToRun)           #debug only
        print str(len(inputList))     #debug only            
        print str(start)              #debug only
        print str(end)                #debug only
        print str(delta / 1000000)    #debug only
        return delta 

    elif (algToRun & 0b00001):
        #outFil.write("---- test-debug------------------------------------")

        start = datetime.datetime.now()
        retVal, retList = testAlg(inputList)
        end = datetime.datetime.now()
        delta = end - start
        delta = int(delta.total_seconds() * 1000000) 
        print str(algToRun)           #debug only
        print str(len(inputList))     #debug only            
        print str(start)              #debug only
        print str(end)                #debug only
        print str(delta / 1000000)    #debug only
        return delta

    else:
        return 0 # just here to keep program from bombing if invalid 0bxxxxx input

def runTestCases():
#-------------------------------------------------------------------------------
# Description:      Runs test cases.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------

    inFil = open("MSS_TestProblems.txt", 'r')
    outFil = open("MSS_TestResults.txt", 'w')

    runInputsThru(inFil, outFil, 0b11110)

    inFil.close()
    outFil.close()

                
def runCustomTestCases():
#-------------------------------------------------------------------------------
# Description:      Runs test cases.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------

    inFil = open("MSS_Custom_TestProblems.txt", 'r')
    outFil = open("MSS_Custom_TestResults.txt", 'w')

    runInputsThru(inFil, outFil, 0b11110)

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

    runInputsThru(inFil, outFil, 0b11110)

    inFil.close()
    outFil.close()


def analysisHelper(resultsList):
#------------------------------------------------------------------------------
# Description:      Writes results to summary CSV file.
# Receives:         2-D list of results.
# Returns:          Nothing.
# Preconditions:    Each element of resultsList should be [alg, n, runTime].
# ------------------------------------------------------------------------------

    print "consolidating experimental outputs into csv formatted file..."
    
    sumFil = open("MSS_ExpAnlys_Results.csv", 'w')

    resultsList = sorted(resultsList, key=lambda x: (x[0], x[1]))

    sumFil.write("algorithm,n,avgRunTime\n")
    for result in resultsList:
      sumFil.write(result[0] + "," + str(result[1]) + "," + str(result[2]) + "\n") 

    sumFil.close()

 
def runExperiment():
#-------------------------------------------------------------------------------
# Description:      Runs 'experiment' part of experimental analysis.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------
    
    results = []

    #---- enumeration ----------------------------------
    name = "enumeration"
    n = 10 # 160 # use this value to get >= 60 sec for highest n
    for i in range(0, 10): # 10 different sizes of n
        totalRunTime = 0
        for j in range(0, 10): # 10 different random lists of size n
            runTime = runInputsThruNoFil(randomList(n), 0b10000)
            totalRunTime += runTime
        result = []
        result.append(name)
        result.append(n)
        result.append(totalRunTime / float(10))
        results.append(result)
        n += 10 # 160 # use this value to get >= 60 sec highest n

    #---- better-enumeration ---------------------------
    name = "better-enumeration"
    n = 10 # 3600 # use this value to get >= 60 sec for highest n
    for i in range(0, 10): # 10 different sizes of n
        totalRunTime = 0
        for j in range(0, 10): # 10 different random lists of size n
            runTime = runInputsThruNoFil(randomList(n), 0b01000)
            totalRunTime += runTime
        result = []
        result.append(name)
        result.append(n)
        result.append(totalRunTime / float(10))
        results.append(result)
        n += 10 # 3600 # use this value to get >= 60 sec for highest n

    #---- divide-and-conquer----------------------------
    name = "divide-and-conquer"
    n = 10
    for i in range(0, 10): # 10 different sizes of n
        totalRunTime = 0
        for j in range(0, 10): # 10 different random lists of size n
            runTime = runInputsThruNoFil(randomList(n), 0b00100)
            totalRunTime += runTime
        result = []
        result.append(name)
        result.append(n)
        result.append(totalRunTime / float(10))
        results.append(result)
        n += 10

    #---- linear-time ----------------------------------
    name = "linear-time"
    n = 37500000 # use this value to get >= 60 sec for highest n
    for i in range(0, 10): # 10 different sizes of n
        totalRunTime = 0
        for j in range(0, 10): # 10 different random lists of size n
            runTime = runInputsThruNoFil(randomList(n), 0b00010)
            totalRunTime += runTime
        result = []
        result.append(name)
        result.append(n)
        result.append(totalRunTime / float(10))
        results.append(result)
        n += 37500000 # use this value to get >= 60 sec for highest n

    #---- test-debug -----------------------------------
    # create input file with random inputs
    #name = "test-debug"
    #n = 10
    #for i in range(0, 10): # 10 different sizes of n
    #    totalRunTime = 0
    #    for j in range(0, 10): # 10 different random lists of size n
    #        runTime = runInputsThruNoFil(randomList(n), 0b00001)
    #        totalRunTime += runTime
    #    result = []
    #    result.append(name)
    #    result.append(n)
    #    result.append(totalRunTime / float(10))
    #    results.append(result)
    #    n += 10

    #---- write output ---------------------------------
    analysisHelper(results)


def main():
#-------------------------------------------------------------------------------
# Description:      Main function which launches test cases, experimental
#                   analyses, and problem solutions.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------
    
    print "running test cases provided with assignment..."
    runTestCases()
    
    print "running extra test cases created as part of assignment..."
    runCustomTestCases()
    
    print "solving problems provided with assignment..."
    solveProblems()
    
    print "running experiments to generate runtimes as a function of input size..."
    runExperiment()
    
# ------------------------------------------------------------
if __name__ == "__main__":
    main()

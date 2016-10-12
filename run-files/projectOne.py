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
import sys

import testAlg # remove before turning in
from testAlg import testAlg

sys.path.insert(0, "./../enumeration")
import alg1

sys.path.insert(0, "./../better-enumeration")
import alg2

sys.path.insert(0, "./../divide-and-conquer")
import alg3

#sys.path.insert(0, "./../linear-time")
#import alg4

def runTestCases(algNum):
#-------------------------------------------------------------------------------
# Description:      Runs test cases using a given algorithm.
# Receives:         Integer value between 1 and 4 inclusive.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------
    print "runTestCases" + str(algNum)


def solveProblems(algNum):
#-------------------------------------------------------------------------------
# Description:      Solves assigned problmes using a given algorithm.
# Receives:         Integer value between 1 and 4 inclusive.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------
    print "solveProblems" + str(algNum)


def runExperimentalAnalysis(algNum):
#-------------------------------------------------------------------------------
# Description:      Runs experimental analysis on a given algorithm.
# Receives:         Integer value between 1 and 4 inclusive.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------
    print "runExperimentalAnalysis" + str(algNum)


def main():
#-------------------------------------------------------------------------------
# Description:      Main function which launches test cases, experimental
#                   analyses, and problem solutions.
# Receives:         Nothing.
# Returns:          Nothing.
# Preconditions:    None.
# ------------------------------------------------------------------------------
    print "main"
    
    algNum = 1
    runTestCases(algNum)
    solveProblems(algNum)
    runExperimentalAnalysis(algNum)

    # dummy call just to demo how to pass args to and get return values
    myList = [31,-41,59,26,-53,58,97,-93,-23,84] 
    retVal, retList = testAlg(myList)

    print "retVal = " + str(retVal)
    print "retList = " + str(retList)

# ------------------------------------------------------------
if __name__ == "__main__":
    main()

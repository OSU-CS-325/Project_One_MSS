#!/usr/bin/python3

#--------------------------------------------------------------------
# Function: enumer_d_and_c
# Description: Computes the maximum sub-array and the associated sum using a div#    ide and conquer algorithm
# Receives: values - list of integers
# Returns: maximum sub-array sum, and maximum sub-array
# Preconditions: "values constains at least one positive integer
#--------------------------------------------------------------------

# Importing argv to allow the method to be used as a CL utility
from sys import argv

def enumer_d_and_c(values):
    # Checking 
    if len(values) == 0:
        return 0, values
    elif len(values) == 1:
        return values[0], values

    tempmax = 0
    midmax = 0
    midstart = 0
    midend = 0

    leftmax = 0
    rightmax = 0

    midpoint = int(len(values) / 2)

    midstart = midpoint
    midend = midpoint

    for i in reversed(range(midpoint)):
        tempmax += values[i]
        if tempmax > leftmax:
            leftmax = tempmax
            midstart = i

    tempmax = 0

    for i in range(midpoint, len(values)):
        tempmax += values[i]
        if tempmax > rightmax:
            rightmax = tempmax
            midend = i + 1

    midmax = leftmax + rightmax

    leftmax, leftsubarr = enumer_d_and_c(values[:midpoint])
    rightmax, rightsubarr = enumer_d_and_c(values[midpoint:])

    if midmax >= leftmax and midmax >= rightmax:
        return midmax, values[midstart:midend]
    elif leftmax >= rightmax and leftmax > midmax:
        return leftmax, leftsubarr
    elif rightmax > leftmax and rightmax > midmax:
        return rightmax, rightsubarr


if __name__ == "__main__":
    print(enumer_d_and_c([int(x) for x in argv[1:]]))

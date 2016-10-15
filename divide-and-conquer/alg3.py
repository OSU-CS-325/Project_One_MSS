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
    # Checking if the values array is either empty or only contains
    # a single element
    if len(values) == 0:
        return 0, values
    elif len(values) == 1:
        return values[0], values

    # Initializing variables to track the maximums and the indices for the
    # middle max subarray to check against the left and right halves
    tempmax = 0
    midmax = 0
    midstart = 0
    midend = 0

    leftmax = 0
    rightmax = 0

    # Calculating and storing the index at which the array is cut in approx.
    # half
    midpoint = int(len(values) / 2)

    midstart = midpoint
    midend = midpoint

    # Reverse iterating through the values array starting from the midpoint
    # and ending at the first element
    for i in reversed(range(midpoint)):
        tempmax += values[i]
        if tempmax > leftmax:
            leftmax = tempmax
            midstart = i

    # Resetting the tempmax variable
    tempmax = 0

    # Iterating through the right half of the values array to determine
    # the maximum right subarray
    for i in range(midpoint, len(values)):
        tempmax += values[i]
        if tempmax > rightmax:
            rightmax = tempmax
            midend = i + 1

    # Summing the leftmax and rightmax and setting that to be the midmax
    midmax = leftmax + rightmax

    # Recursively calling the main method to act on the left and 
    # right halves of the values array
    leftmax, leftsubarr = enumer_d_and_c(values[:midpoint])
    rightmax, rightsubarr = enumer_d_and_c(values[midpoint:])

    # If-else block used to determine the biggest subarray max
    # and to return that max with the subarray it reflects
    if midmax >= leftmax and midmax >= rightmax:
        return midmax, values[midstart:midend]
    elif leftmax >= rightmax and leftmax > midmax:
        return leftmax, leftsubarr
    elif rightmax > leftmax and rightmax > midmax:
        return rightmax, rightsubarr

# If block that allows this file to be run as a CL utility
if __name__ == "__main__":
    print(enumer_d_and_c([int(x) for x in argv[1:]]))

#!/usr/bin/python3

#---------------------------------------------------------------------------
# Function: enumeration
# Description: Computes the maximum sub-array and the associated sum using the e#  numeration algorithm.
# Receives: values - list/array of integers
# Returns: maximum sub-array sum, and maximum sub-array
# Preconditions: "values" contains at least one positive integer
#---------------------------------------------------------------------------

# Module used to facilitate the use of this function as a CL utility 
from sys import argv

def enumeration(values):
  
  # Checking if the values array is empty if so the function returns
  if len(values) != 0:
    max_sum = float("-inf")
  else:
    return 0, values

  # Iterate starting index over list of values
  for i in range(len(values)):

    # Inner for loop that explores the remaining array for the max sub-array
    for j in range(i, len(values)):
      cur_sum = 0
      
      # Inner for loop that explores the currently bounded sub-array between
      # indices i and j
      for k in range(i, j + 1):
        cur_sum += values[k]
  
        # If the current sum is the new max save it and the starting and ending
        # indices 
        if cur_sum > max_sum:
          max_sum = cur_sum
          start_idx = i
          end_idx = j

  # Return the max sum and the maximum sub-array
  return max_sum, values[start_idx : end_idx + 1]

# Code that allows this file to be executed as a CL utility accepting
# command line arguments
if __name__ == "__main__":
  print(enumeration([int(x) for x in argv[1:]]))

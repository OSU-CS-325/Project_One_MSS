#-------------------------------------------------------------------------------
# Function:			linearTime
# Description:      Computes the maximum sub-array and and associated sum using
#					the Kadane's algorithm.
# Receives:         values - list of integers
# Returns:          maximum sub-array sum, and maximum sub-array
# Preconditions:    "values" contains at least 1 positive integer
# ------------------------------------------------------------------------------
def linearTime(values):
	# Initialize to -Infinity so that any computed sum will be greater
	max_sum = -float("inf")
	ending_here_sum = -float("inf")

	for i in range(len(values)):

		# Index of sub-array that ends with current index
		ending_here_high = i

		# If the sum to this point is positive, continue the running sum
		if ending_here_sum > 0:
			ending_here_sum = ending_here_sum + values[i]
		# Otherwise, start the running sum over from here
		else:
			ending_here_low = i
			ending_here_sum = values[i]

		# If running sum is highest seen, save the sum and the indices
		if ending_here_sum > max_sum:
			max_sum = ending_here_sum
			start_idx = ending_here_low
			end_idx = ending_here_high

	# Return the maximum sub-array sum, and the maximum sub-array itself
	return max_sum, values[start_idx : end_idx + 1]
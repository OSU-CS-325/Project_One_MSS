#-------------------------------------------------------------------------------
# Function:			betterEnumeration
# Description:      Computes the maximum sub-array and and associated sum using
#					the "better enumeration" algorithm.
# Receives:         values - list of integers
# Returns:          maximum sub-array sum, and maximum sub-array
# Preconditions:    "values" contains at least 1 positive integer
# ------------------------------------------------------------------------------
def betterEnumeration(values):
	# Initialize to -Infinity so that any computed sum will be greater
	max_sum = -float("inf")

	# Iterate starting index over list of values
	for i in range(len(values)):

		# Track running sum for each starting index
		cur_sum = 0

		# Iterate ending index over list of values
		for j in range(i, len(values)):
			cur_sum += values[j]

			# If running sum is highest seen, save the sum and the indices
			if cur_sum > max_sum:
				max_sum = cur_sum
				start_idx = i
				end_idx = j

	# Return the maximum sub-array sum, and the maximum sub-array itself
	return max_sum, values[start_idx : end_idx + 1]
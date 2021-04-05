# Goal			: Find max area between any 2 lines given an array of positive height lines
# Given			: Array of bar-graph lines along a single axis with positve heights
# Assumption	: Each line's position is their index in the array and distance between consecutive lines are of length 1

def Max_Area( bars_array ):
	max_width = len( bars_array ) - 1				# Total bars 
	l = 0											# Starting left bounds
	r = max_width									# Starting right bounds
	res_area = 0									# Result holder for max area

	while l <= r :									# Loop until distance between 2 bounds is 0
													# Grab smaller height of 2 bounds to find max area at that point
		temp_area = min( bars_array[ l ] , bars_array[ r ] ) * ( r - l )
		res_area = max( temp_area , res_area )		# Update result area value if temp_area is bigger
		if bars_array[ l ] < bars_array[ r ]:		# If the left bounds is smaller, move left bounds over by 1
			l += 1
		else:										# Else move right bounds backwards by 1
			r -= 1
	return res_area							

def main():
	test1 = [ 1 , 8 , 6 , 2 , 5 , 4 , 8 , 3 , 7 ]	# User defined base case
	test2 = [ 1 , 1 ]								# User defined edge case
	test3 = [ 4 , 3 , 2 , 1 , 4 ]					# User defined bounds case
	test4 = [ 1 , 2 , 1 ]							# User defined mid case

	print( "Testing case {0}".format( test1 ) )
	result = Max_Area( test1 )
	print( result )

	print( "Testing case {0}".format( test2 ) )
	result = Max_Area( test2 )
	print( result )

	print( "Testing case {0}".format( test3 ) )
	result = Max_Area( test3 )
	print( result )

	print( "Testing case {0}".format( test4 ) )
	result = Max_Area( test4 )
	print( result )

main()
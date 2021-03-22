# Goal			: From an array, return a pair of nums that add up to target value 
# Given			: Array of ints, Target value
# Assumption	: Each Target value only has one possible solution

def Two_Sum( num_arr, target_val ):
	hash = {} 										# Hashtable to collect int pairs
	for element in num_arr: 						# Iterate through array 1 element at a time to use in hash
		if element not in hash: 					# Check if element in hash. If not, add to hash
			hash[ target_val - element ] = element  # Contrapositive of element's value is used as hash key value to quickly find its pair
		else:
			return ( element , hash[ element ] ) 	# If element in hash, return because it is the numeric pair of an already searched element
	return ( -1 , -1 )								# If no possible solution, return -1 , -1 pair

def Result_Check( result ):
	no_solution = ( -1 , -1 )						# No soltuion result ( numbers picked are arbitrary )
	if result != no_solution:
		print( "Solution found: {}".format( result ) )
	else:
		print( "No Solution found" )
	return

def main():
	num_arr = [2 , 7 , 11 , 15 ] 					# User defined input array
	target_val = 9				 					# User defined target value	
	error_case_val = 10								# User defined Error Test Case Value
	print( "Target Value is {0} and Num_arr contains {1}".format( target_val , num_arr ) )
	result = Two_Sum( num_arr , target_val )		# Result from function
	Result_Check( result )							# Show Result
	print( "Error Case Check, Target Value is {0} and Num_arr contains {1}".format( target_val , num_arr ) )
	error_case_result = Two_Sum( num_arr , error_case_val )
	Result_Check( error_case_result )

main()

# Goal			: Return a 32-bit int with its digits reversed, if the value is outside the 32-bit range, then return 0
# Given			: 32-bit signed int
# Assumption	: Assume given int is between  -21^31 <= x <= 2^31 - 1
def Reverse_int( input_int ):
	result = int( str( abs ( input_int ) ) [ ::-1 ] )	# Take absolute value of the input then turn into a string to reverse it using slicing 
														# Take reversed string and turn back into int and set to result
	if result.bit_length() > 32:						# If result is out of 32-bit range, return 0
		result = 0

	if input_int < 0:									# If input value is negative, return negative result
		result = -result
	return result
def main():
	test1 = 123											# User defined base test case
	test2 = -123										# User defined negative test case
	test3 = 120											# User defined leading 0 test case
	test4 = 0											# User defined single digit test case

	print( "Testing case {0}".format( test1 ) )
	result = Reverse_int( test1 )
	print( result )
	
	print( "Testing case {0}".format( test2 ) )
	result = Reverse_int( test2 )
	print( result )

	print( "Testing case {0}".format( test3 ) )
	result = Reverse_int( test3 )
	print( result )

	print( "Testing case {0}".format( test4 ) )
	result = Reverse_int( test4 )
	print( result )
main()
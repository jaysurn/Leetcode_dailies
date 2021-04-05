# Goal			: Return the number in the string as a signed 32-bit int, if the number is is out of bounds, set to closer bound
#				  -2^31 = -2147483648 , 2^31 - 1 = 2147483647
# Given			: A string containing a convertible number and may contain characters
# Assumption	: String may only contain letters, digits, and - sign
import re
def String_to_Int( input_str ):
	regex_result = re.search( '(\-?\d+)' , input_str )	# Regex search for a signed int in string
	result = int( regex_result.group( 1 ) )				# Convert from string to int
	if result.bit_length() > 32:							# If result is out of bound, round to 21-bit bounds
		if int( input_str ) < 0:
			result = -2**31
		else:
			result = ( 2**31 ) - 1
	return result 										# Return final result
def main():
	test1 = "42"										# User defined base case
	test2 = "-42"										# User defined negative case
	test3 = "4193 with words"							# User defined char + num case
	test4 = "words and -987"							# User defined char + num + negative case
	test5 = "-91283472332"								# User defined out of bounds case
	test6 = "91283472332"								
	print( "Testing case {0}".format( test1 ) )
	result = String_to_Int( test1 )
	print( result )

	print( "Testing case {0}".format( test2 ) )
	result = String_to_Int( test2 )
	print( result )

	print( "Testing case {0}".format( test3 ) )
	result = String_to_Int( test3 )
	print( result )

	print( "Testing case {0}".format( test4 ) )
	result = String_to_Int( test4 )
	print( result )

	print( "Testing case {0}".format( test5 ) )
	result = String_to_Int( test5 )
	print( result )

	print( "Testing case {0}".format( test6 ) )
	result = String_to_Int( test6 )
	print( result )
main()
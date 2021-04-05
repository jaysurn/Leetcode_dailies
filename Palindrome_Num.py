# Goal			: If an int is a palindrome, return true. Else return false
# Given			: A signed int
# Assumption	: Input is within the 32-bit bounds

def Palindrome_Num( input_int ):
	if input_int < 0 or ( input_int > 0 and input_int % 10 == 0 ) : 					# If input is negative, can't be a palindrome 
		return False 													# If input is base 10, it also can't be a palindrome due to leading 0 not being counted
	reversed_val = 0
	while input_int > reversed_val:										# Loop while input_int is bigger than reversed_val; each cycle input_int loses its last digit and appends to reversed_val
		reversed_val = reversed_val * 10 + input_int % 10 				# Update reversed value length by 1 each loop and append value in input_int's one's place
		input_int = input_int // 10										# Update input_int to decrease length 1 each loop 
	if input_int == reversed_val or input_int == reversed_val // 10 :	# Return true if the two ints are identical (when of equal length) or identical when ignoring 1's place in reversed_val (when of odd length) 
		return True 
	else:																# Return false if not a palindrome
		return False

def main():
	test1 = 121															# User defined base case
	test2 = -121														# User defined negative case
	test3 = 10															# User defined ending 0 case
	test4 = 1595														# User defined error case

	print( "Testing case {0}".format( test1 ) )
	result = Palindrome_Num( test1 )
	print( result )

	print( "Testing case {0}".format( test2 ) )
	result = Palindrome_Num( test2 )
	print( result )

	print( "Testing case {0}".format( test3 ) )
	result = Palindrome_Num( test3 )
	print( result )

	print( "Testing case {0}".format( test4 ) )
	result = Palindrome_Num( test4 )
	print( result )
main()
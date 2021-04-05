# Goal			: Return True/False based on if the regex finds the input string matches the pattern
# Given			: Input string and regex pattern
# Assumption	: Input string only contains chars and regex pattern uses standard regex rules
import re

def Regex_Matching( input_str , pattern ):
	result = re.fullmatch( pattern , input_str )	# Regex searches using input pattern and string
	if result:										# If a result exists, match was found, return True
		return True	
	else:											# Else result not found, return False
		return False

def main():
	test1 = "aa"									# User defined base case
	pattern1 = "a"									# User defined base pattern
	pattern2 = "a*"									# User defined regex mixed symbol case
	test2 = "ab"									# User defined non-repeating case
	pattern3 = ".*"									# User defined regex symbol only case
	test3 = "aab"									# User defined 0 or more case
	pattern4 = "c*a*b"								# User defined 0 or more pattern
	test4 = "mississippi"							# User defined repeating case
	pattern5 = "mis*is*p*."							# User defined strict pattern

	print( "Testing case {0} with pattern {1}".format( test1 , pattern1 ) )
	result = Regex_Matching( test1 , pattern1 )
	print( result )

	print( "Testing case {0} with pattern {1}".format( test1 , pattern2 ) )
	result = Regex_Matching( test1 , pattern2 )
	print( result )	

	print( "Testing case {0} with pattern {1}".format( test2 , pattern3 ) )
	result = Regex_Matching( test2 , pattern3 )
	print( result )

	print( "Testing case {0} with pattern {1}".format( test3 , pattern4 ) )
	result = Regex_Matching( test3 , pattern4 )
	print( result )

	print( "Testing case {0} with pattern {1}".format( test4 , pattern5 ) )
	result = Regex_Matching( test4 , pattern5 )
	print( result )
main()
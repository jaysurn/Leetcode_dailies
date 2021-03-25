# Goal			: Find and return the longest palindrome within a string
# Given			: A single string
# Assumption	: String can only contain digits and numbers and will always contain at least 1 character
def get_palindrome( string , left , right ):			# Helper function to get palindrome given a string and 2 index pairs to check with
														# While being in-bounds of the string, check if letters match at each index
	while left >= 0 and right < len( string ) and string[ left ] == string[ right ]:
		left -= 1										# Decrement left index and increment right index to see if palindrome could be longer
		right += 1
	return string[ left + 1 : right ]					# Return palindrome found between the indexes

def Longest_Paldindrome_Substring( string ):
	result = ""											# Result string holder starts empty 
	for index in range( len( string ) ):				# Iterate through the string and find a palindrome treating it as the middle of it
														# Result string gets updated based on which palindrome returned is the longest
														# Compares palindrome created for an odd-length string then a even-length string and previous paldindromes found
		result = max ( get_palindrome( string , index , index ) , get_palindrome( string , index , index + 1 ) , result , key = len )

	return result
def main():
	test1 = "babad"										# User defined test case for a basecase
	test2 = "c44d"										# User defined test case for numbers
	test3 = "a"											# User defined test case for strings of size 1
	test4 = "ac"										# User defined test case for even-length strings
	result = Longest_Paldindrome_Substring( test1 )
	print( result )

	result = Longest_Paldindrome_Substring( test2 )
	print( result )

	result = Longest_Paldindrome_Substring( test3 )
	print( result )

	result = Longest_Paldindrome_Substring( test4 )
	print( result )
main()
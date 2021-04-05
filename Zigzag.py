# Goal			: Return a string in a single line after converting it from a zigzag
#				  Example: paypalishiring zigzagging into 3 lines is
#				  P   A   H   N
#				  A P L S I I G
#				  Y   I   R
# 				  Then converts into PAHNAPLSIIGYIR when converted into a single line
# Given			: String and the number of rows to zigzag into
# Assumption	: String only contains letters and number of rows is positive
def Zigzag( string , numrows ):
	if numrows == 1 or numrows >= len ( string ):		# If numrows equals 1, you can't zigzag it, so return string as is
		return string 									# If numrows is more than length of string, you also can't zigzag it, so return string as is

	string_array = [ "" ] * numrows						# Populate character array with empty strings for each row needed
	index = 0 
	step = 1

	for char in string:									# Iterate through string and add character to string based on row number as index
		string_array[ index ] += char
		if index == 0:									# If at row 1, step is 1 to go to next line
			step = 1
		elif index == numrows - 1:						# If at at last row, step is -1 to go back to the previous line
			step = -1
		index += step									# Change index to go to next line based on is you're going forward or backwards based on step's value
	return "".join( string_array )						# Append each string from string array into one giant string
def main():
	test1 = "Example"									# User defined base case
	numrows1 = 2										# Used defined base case
	test2 = "X"											# Used defined edge case for numrows being bigger than string
	numrows2 = 1										# User defined edge case for numrows being 1
	
	result = Zigzag( test1 , numrows1 )
	print( result )
	result = Zigzag( test2 , numrows1 )
	print( result )
	result = Zigzag( test1 , numrows2 )
	print( result )
main()
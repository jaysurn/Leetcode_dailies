# Goal			: Return a positive int from a roman numeral 
# Given			: String that contains roman numeral
# Assumption	: Roman numeral may only contain I,V,X,L,C,D,M

def Roman_to_Int( roman ):
	numeral_dict = {							# Conversion dictionary
	'I'	: 1 ,
	'V'	: 5 ,
	'X'	: 10 ,
	'L'	: 50 ,
	'C' : 100 ,
	'D' : 500 ,
	'M' : 1000
	}
	total = 0									# Total holder
	for i in range( len( roman ) - 1 ):			# Loop and get index and element
		numeral = roman[ i ]					# If element's value is less than the next element's value, subtract element's value
		if numeral_dict[ numeral ] < numeral_dict[ roman[ i + 1 ] ]:	
			total -= numeral_dict[ numeral ]
		else:									# Else add element's value to total
			total += numeral_dict[ numeral ]
	total += numeral_dict[ roman[ -1 ] ]		# Loop only goes to second to last char, so add last char's value to total
	return total

def main():
	test1 = "III"								# User defined base case
	test2 = "IV"								# User defined IV case
	test3 = "IX"								# User defined IX case
	test4 = "LVIII"								# User defined L case
	test5 = "MCMXCIV"							# User defined mixed case

	print( "Testing case {0}".format( test1 ) )
	result = Roman_to_Int( test1 )
	print( result )

	print( "Testing case {0}".format( test2 ) )
	result = Roman_to_Int( test2 )
	print( result )

	print( "Testing case {0}".format( test3 ) )
	result = Roman_to_Int( test3 )
	print( result )

	print( "Testing case {0}".format( test4 ) )
	result = Roman_to_Int( test4 )
	print( result )

	print( "Testing case {0}".format( test5 ) )
	result = Roman_to_Int( test5 )
	print( result )
main()
# Goal			: Convert an int into a roman numeral
# Given			: Positive int
# Assumption	: Value is between 1 and 3999
def Int_to_Roman( input_int ):
	res = ""
	numerals = { 				# Numeral dict for appending to result
		1 		: "I" ,
		5 		: "V" ,
		10		: "X" ,
		50		: "L" ,
		100		: "C" ,
		500		: "D" ,
		1000	: "M"
	}
	divisor = 1000				# Starting divisor set to bigger numeral and decreases by base 10 each loop

	while input_int != 0:		# Loop until divisor hits 0, quo gets first digit, remainder gets save the remaining digits for next loop iteration
		quo , remainder = divmod( input_int , divisor )
								# Append case for 9
		if quo == 9:
			res += numerals[ divisor ] + numerals[ divisor * 10 ]
								# Append case for 4
		elif quo == 4:
			res += numerals[ divisor ] + numerals[ divisor * 5 ]
								# Append case for values between 4 and 9
		elif quo >= 5:
			res += numerals[ divisor * 5 ] + numerals[ divisor ] * (  quo - 5 )
								# Append case for values between 1 and 3
		else:
			res += numerals[ divisor ] * quo
								# Decrease divisor by base 10
		divisor = divisor // 10
								# Update input_int to be remainder for next iteration
		input_int = remainder
	return res

def main():
	test1 = 3					# User defined base case
	test2 = 4					# User defined IV case
	test3 = 9					# User defined IX case
	test4 = 58					# User defined mixed case
	test5 = 1994				# User defined thousands case

	print( "Testing case {0}".format( test1 ) )
	result = Int_to_Roman( test1 )
	print( result )

	print( "Testing case {0}".format( test2 ) )
	result = Int_to_Roman( test2 )
	print( result )

	print( "Testing case {0}".format( test3 ) )
	result = Int_to_Roman( test3 )
	print( result )

	print( "Testing case {0}".format( test4 ) )
	result = Int_to_Roman( test4 )
	print( result )

	print( "Testing case {0}".format( test5 ) )
	result = Int_to_Roman( test5 )
	print( result )
main()
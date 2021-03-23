# Goal			: Given a string, find the length of the longest substring ( i.e. abcabcbb: abc , bbbb: b )
# Given			: Single string
# Assumption	: String consists only of letters , numbers, and symbols

def longest_substr_len( string ):
	len_max = 0											# Used to record length
	start = 0											# Used to track beginning index of current substring
	hash = {}											# Used to track non-repeating characters
	for i , char in enumerate( string ):				# Enumerate to get index value and character
		if char in hash and start <= hash[char]:		# If character is repeated, check if it starts after current start point
			start = hash[char] + 1						# Update substring start point ( +1 since index starts at 0 )
		else:											
			len_max = max( len_max , i - start + 1 )	# Update longest substring length 
		hash[char] = i 									# Enter character into dict with current index
	return len_max

def main():
	str1 = "racecar"									# User defined teststring 1
	str2 = "tmmzuxta"									# User defined teststring 2 using repeating characters
	str3 = "6.02234"									# User defined teststring 3 using symbols

	print( "Finding length of longest substring of {0}".format( str1 ) )
	res_val = longest_substr_len( str1 )
	print( res_val )

	print( "Finding length of longest substring of {0}".format( str2 ) )
	res_val = longest_substr_len( str2 )
	print( res_val )
	
	print( "Finding length of longest substring of {0}".format( str3 ) )
	res_val = longest_substr_len( str3 )
	print( res_val )	
main()
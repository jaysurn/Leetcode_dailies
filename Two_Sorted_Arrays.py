# Goal 			: Return Median of the 2 sorted arrays of integers
# Given			: 2 Sorted Arrays of same or different sizes
# Assumption	: Arrays can be of any size and can contain different elements

def Two_Sorted_arrays( arr1 , arr2 ):
	total_len = len( arr1 ) + len( arr2 )				# Get total length of combined arrays
	if total_len % 2 == 1:								# If new array size is odd, get middle as median
		return Partition_Medians( arr1 , arr2 , total_len // 2 )
	else:												# If new array size is even, get the 2 middles as the median and average them
		return ( Partition_Medians( arr1 , arr2 , ( total_len // 2 ) - 1 ) + Partition_Medians( arr1 , arr2 , total_len // 2 ) ) / 2.0
def Partition_Medians( arr1 , arr2 , part ):			# Recursive helper function to find medians using partitions
	if  len( arr1 ) > len( arr2 ) :
		arr1 , arr2 = arr2 , arr1						# Swap arrays if array1 is bigger
	len1 , len2 = len( arr1 ) , len( arr2 )
	if not arr1:
		return arr2[ part ]								# Return median of array2 if array1 is empty
	if part == len1 + len2 - 1:							# if the partition is equal to the middle of the 2 arrays, get the last value of each array and return the bigger one
		return max( arr1[-1] , arr2[-1] )

	index = len1 // 2									# Get partition index for array1
	index2 = part - index 								# Create new partition on array2 to equally balance the partitioned elements in array1
	
	if arr1[ index ] > arr2[ index2 ]:					# Find bigger partition median then use that as an index to narrow down the median
														# Array1 being bigger means median is somewhere left of the index of array1 but right of index of array2
		return Partition_Medians( arr1[ :index ] , arr2[ index2: ] , index )
	else:
														# Array 2 being bigger means median is somewhere right of the index of array1 but left of index of array2
		return Partition_Medians( arr1[ index: ] , arr2[ :index2 ] , index2 )
def main():
	arr1 = [ 1 , 3 ]									# User defined arrays for different sized arrays 
	arr2 = [ 2 ]
	median = Two_Sorted_arrays( arr1 , arr2 )
	print( median )										# User defined arrays for same size arrays
	arr3 = [ 1 , 2 ]
	arr4 = [ 3 , 4 ]
	median = Two_Sorted_arrays( arr3 , arr4 )
	print( median )	
	arr5 = [ 0 , 0 ]									# User defined arrays for repeating elements
	arr6 = [ 0 , 0 ]
	median = Two_Sorted_arrays( arr5, arr6 )
	print( median )
	arr7 = []											# User defined arrasy for empty arrays
	arr8 = [ 2 ]
	median = Two_Sorted_arrays( arr7, arr8 )
	print( median )
main()
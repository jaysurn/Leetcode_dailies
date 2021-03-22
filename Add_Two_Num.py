# Goal			: Return the sum of 2 postive integers stored as reverse linked lists
# Given			: 2 linked lists of ints stored in reverse ( ex. 123 stored as 3->2->1 in list )
# Assumption	: Lists' int value does not begin with 0

class Node:												# Class definition for creating a Linkedlist
	def __init__( self , data ):
		self.data = data
		self.next = None

def insert( L_list , data ):							# Helper functon add a new node to a linkedlist
	temp_node = Node ( data )							# New node created

	if ( L_list == None ):								# Create new linkedlist if doesn't exist and add new node
		L_list = temp_node
	else :
		ptr = L_list									# Pointer created to loop through node till you reach end
		while ( ptr.next != None ):
			ptr = ptr.next
		ptr.next = temp_node							# Add new node to end of linkedlist
	return L_list

def print_L( L_list ):									# Helper function to see the whole linkedlist
	while ( L_list != None ):
		print( L_list.data , end = " " )
		L_list = L_list.next
	print( "\n" )
	return
def int_to_list( Integer ):								# Helper function to convert ints used to linkedlists
	L_list = None
	for digit in reversed( Integer ):
		L_list = insert( L_list , int( digit ) )
	return L_list
def Add_Two_Num( list1 , list2 ):						# Adds 2 lists and forms a new linkedlist with result stored in the same manner
	carry = 0											# Used to perform math to see if a carry is needed to be added in the next addition
	result_node = curr_node = Node( 0 )					# result_node and curr_node set to an empty node, result_node will stay at this root point while curr_node loops through lists

	while list1 or list2 or carry:						# while list1,list2,or the carry exists
		if list1:										# if list1 has another node, add data to carry and go to next node
			carry += list1.data
			list1 = list1.next
		if list2:
			carry += list2.data							# if list2 has another node, add data to carry and go to next node
			list2 = list2.next
		curr_node.next = Node( carry % 10 )				# new node in result_node created from modular division forcing value to be between 0-9
		curr_node = curr_node.next						# go to next node
		carry //= 10									# check if carry is greater than 10 using floor division to see if a carry-1 is needed for next addition
	return result_node.next

def main():
	int1 = "243"										# User defined positive ints stored in reverse
	int2 = "564"

	list1 = int_to_list( int1 )
	list2 = int_to_list( int2 )
	print( "Adding lists {0} and {1}".format( int1 , int2 ) )
	result_list = Add_Two_Num( list1 , list2 )			# Math performed here then prints on next line
	print_L( result_list )

	int3 = "2048"										# User defined positives ints for testing ints of different lengths
	int4 = "128"

	list3 = int_to_list( int3 )
	list4 = int_to_list( int4 )
	print( "Adding lists {0} and {1}".format( int3 , int4 ) )
	result_list = Add_Two_Num( list3, list4 )			# Math performed here then prints on next line
	print_L( result_list )
main()
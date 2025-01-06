# Python program to remove given element from the list
list1 = [1, 9, 8, 4, 9, 2, 9]
	
# Printing initial list
print ("original list : "+ str(list1))
n = int(input("Enter the number of elements: "))
remove = n
	
# using pop()
# to remove list element 9
if remove in list1:
# get index of 9 and pop it out
	list1.pop(list1.index(remove))
	
# Printing list after removal
print ("List after element removal is : " + str(list1))
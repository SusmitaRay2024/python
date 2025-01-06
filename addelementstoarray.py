# Python3 code to demonstrate working of 
# Random insertion of elements K times
# Using randint() + list slicing + loop + choice()
import random

# initializing list
test_list = [5, 7, 4, 2, 8, 1]

# printing original list
print("The original list : " + str(test_list))

# initializing add list 
add_list = ["Gfg", "Best", "CS"]

# initializing K 
K = 3

for idx in range(K):
	
	# choosing index to enter element
	index = random.randint(0, len(test_list))
	
	# reforming list and getting random elem
 # reforming list and getting random element to add
test_list = test_list[:index] + [random.choice(add_list)] + test_list[index:]
 
# printing result 
print("The created List : " + str(test_list))
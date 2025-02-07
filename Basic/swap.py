val_1 = int(input("Enter first value: "))
val_2 = int(input("Enter second value: "))

temp = val_1
val_1 = val_2
val_2 = temp

print (f"The value of 1 after swapping {val_1} ")
print (f"The value of 2 after swapping {val_2} ")
###########################################################

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))

num_1, num_2 = num_2, num_1
print(f"number 1 = {num_1}")
print(f"number 2 = {num_2}")
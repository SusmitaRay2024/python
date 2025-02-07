
elements_list = []

# Get the number of elements
number_of_elements = int(input("Enter the number of elements: "))

# Append elements to the list
for index in range(number_of_elements):
    element = input(f"Enter element {index+1}: ")
    elements_list.append(element)

print("List:", elements_list)
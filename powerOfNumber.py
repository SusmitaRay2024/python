# Program to print squares of numbers: 1, 4, 9, 16, 25, ..., up to n
limit = int(input("Enter the limit: "))
current_number = 1

while current_number <= limit:
    print(current_number * current_number, end=" ")
    current_number += 1

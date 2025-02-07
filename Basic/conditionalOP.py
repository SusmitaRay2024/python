# Check if a number is greater than 10
number = int(input("Enter a Number: "))
print("Hello the number is greater than 10") if number > 10 else print("Bye")

# Check if a number is positive or negative
number = int(input("Enter a Number: "))
print("Positive Number") if number >= 0 else print("Negative Number")

# Check if a number is even or odd
number = int(input("Enter a Number: "))
print("Even Number") if number % 2 == 0 else print("Odd Number")

# Find the greater of two numbers
first_number = int(input("Enter the First Number: "))
second_number = int(input("Enter the Second Number: "))
print(f"Greater Number is {first_number}") if first_number > second_number else print(f"Greater Number is {second_number}")

# Find the maximum of three numbers
first = int(input("Enter the First Number: "))
second = int(input("Enter the Second Number: "))
third = int(input("Enter the Third Number: "))
print(f"Greatest Number is {first}") if (first > second and first > third) else print(f"Greatest Number is {second}") if second > third else print(f"Greatest Number is {third}")
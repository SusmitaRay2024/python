# Palindrome Number: A number whose reverse is equal to the number itself, e.g., 181, 242, 989
number_input = int(input("Enter a number: "))
original_number = number_input
reversed_number = 0

while number_input != 0:
    remainder = number_input % 10
    reversed_number = reversed_number * 10 + remainder
    number_input = number_input // 10

print("Number is Palindrome") if original_number == reversed_number else print("Number is not Palindrome")

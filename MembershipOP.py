# 'in', 'not in'
# It tracks the presence of a sequence in data
string_hello = "Hello"
print('e' in string_hello)  # True
print('i' in string_hello)  # False

welcome_message = "Hello Welcome to Python World"
print('Python' in welcome_message)  # True

email_address = 'susmita@gmail.com'
print("Valid Email") if ('@' in email_address) else print("Invalid Email")

number_list = [10, 5, 70, 30, 35]
user_input = int(input("Enter a number: "))
print("Search Successful") if (user_input in number_list) else print("Search Not Successful")
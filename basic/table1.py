# Input number to generate multiplication table
num = int(input("Enter a number for the multiplication table: "))

# Initialize a counter to 1
i = 1

# While loop to generate the multiplication table
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
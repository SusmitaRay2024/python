# Program to print patterns based on user input
limit = int(input("Enter Limit: "))

# Pattern 1: Printing stars in increasing order
for row in range(1, limit + 1):
    for column in range(1, row + 1):
        print("*", end=" ")
    print()

print("---------------------------------")

# Pattern 2: Printing row numbers in increasing order
for row in range(1, limit + 1):
    for column in range(1, row + 1):
        print(row, end=" ")
    print()

print("---------------------------------")

# Pattern 3: Printing column numbers in increasing order
for row in range(1, limit + 1):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()

print("---------------------------------")



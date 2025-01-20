# Nested Loop - The "inner loop" will finish all of its iterations before finishing one iteration of the "outer loop"

rows = int(input("How many Rows?: "))
columns = int(input("How many Columns?: "))
symbol = input("Enter a Symbol to use: ")

for i in range (rows):
    for j in range (columns):
        print(symbol, end=" ")
    print()
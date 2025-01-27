n = int(input("Enter Linit: "))
for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print("*", end=" ")
    print()

print("---------------------------------")

for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print(i, end=" ")
    print()
    
print("---------------------------------")

for i in range(1, n+1, 1):
    for j in range(1, i+1, 1):
        print(j, end=" ")
    print()
    
print("---------------------------------")



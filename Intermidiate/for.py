#For loop (Initialization - Condition - Step)
for i in range(10):
    print(i)
print("------")
    
for i in range(1, 11):
    print(i)
print("------")

#print 1,4,9,16,25....100
for i in range(1, 11):
    print(i*i)
print("------")

#Print no of table
n=int(input("Enter a Number"))
for j in range(1, 11):
    print(n*j)

#Step - 1,3,5,7,9
n = int(input("Enter a Number"))
for i in range (1, n+1, 2):
    print(i)
    
#Reverse
for i in range (10, 0, -1):
    print(i)
    
#Nested Loop
#How to implement nesting of for loop
for i in range(1, 6, 1):
    for j in range(1, 6, 1):
        print(i, j)
    print()
    
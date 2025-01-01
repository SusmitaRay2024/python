#write a program to print the following input - 1, 4, 9, 16, 25 ..... n 
n=int(input("Enter the limit"))
i=1
while(i<=n):
    print(i*i, end=" ")
    i+=1
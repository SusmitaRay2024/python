# if, else
n= int(input("Enter a No"))
print ("hello") if(n>10) else print("Bye")

# Write a program to enter a number & check it's positive or negetive 
a= int(input("Enter a No"))
print ("positive number") if(a>=0) else print("Negetive Number")

# Write a program to enter a number & check even or odd
b= int(input("Enter a No"))
print ("Even number") if(b%2==0) else print("Odd Number")

# Write a program to enter two number & print greater between two number
c= int(input("Enter First No"))
d= int(input("Enter Second No"))
print ("Greater Number is ", c) if(c>d) else print("Greater Number is ", d)

#Print Max Number between 3 number
e= int(input("Enter First No"))
f= int(input("Enter Second No"))
g= int(input("Enter Third No"))
print ("Greater Number is ", e) if(e>f)and(e>g) else print("Greater Number is ", f) if(f>e)and(f>g) else print("Greater Number is ", g) 



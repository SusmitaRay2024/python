#Simple 
print("..Simple if..")
n=int(input("Enter a Number "))
if(n>50):
    print("Hello")
    
#Ladder if
#print word of number
print("print word of number between 1-5")
n=int(input("Enter a Number "))
if(n==1):
    print("One")
if(n==2):
    print("Two")
if(n==3):
    print("Three")
if(n==4):
    print("Four")
if(n==5):
    print("Five")
if(n>5 or n<1):
    print("Invalid Number")
    
#Nested if
#program for Driver selection
print("program for Driver selection")
name = input("Enter Your Name ")
age = int(input("Enter Your Age "))
ms = input("Enter Marital Status- M/U: ")
if(name=='Rajesh'):
    if(age>18 and age<50):
        if(ms=='M'):
            print("You are Selected...")


#if-else
#Program for Even or Odd
print("Program for Even or Odd")
n=int(input("Enter a Number "))
if(n%2==0):
    print("Number is even")
else:
    print("Number is Odd")
    
#Program for positive or negetive number
print("Program for positive or negetive number")
n=int(input("Enter a Number "))
if(n>=0):
    print("Number is Positive")
else:
    print("Number is Negetive")
    
    
#Greater Between two number
print("Greater Between two number")
a=int(input("Enter First Number "))
b=int(input("Enter Second Number "))
if(a>b):
    print("Greater Number is %d " %(a))
else:
    print("Greater Number is %d " %(b))
    
    
#if-elif-else
#Greater Between three number
print("Greater Between three number")
a=int(input("Enter First Number "))
b=int(input("Enter Second Number "))
c=int(input("Enter Thrid Number "))
if(a>b and a>c):
    print("Greater Number is %d " %(a))
elif(b>c):
    print("Greater Number is %d " %(b))
else:
    print("Greater Number is %d " %(c))
    
    
#Get max, min swap value of variables
print("Get max, min swap value of variables")
print("\n 1.Max \n 2.Min \n 3.Swap")
a,b = map(int,input("enter two numbers ").split(","))
choice = int(input("Enter your Choice"))
if(choice==1):
    print(max(a,b))
elif(choice==2):
    print(min(a,b))
elif(choice==3):
    a,b = b,a
    print("After swaping %d %d " %(a,b))
else:
    print("Invalid Choice")
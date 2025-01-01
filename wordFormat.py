# input-> 254 
# 2
# 5
# 4 


# n = int(input("Enter a Number"))
# s=0
# while(n!=0):
#     r = n % 10
#     s = s * 10 + r
#     n = n // 10
# while(s!=0):
#     r = s % 10
#     print(r)
#     s = s // 10 

#How to print word format of number ex - 254 -> TwoFiveFour
n = int(input("Enter a Number"))
s = 0
while(n!=0):
    r = n % 10       
    s = s * 10 + r   
    n = n // 10      
while(s!=0):
    r = s % 10   
    if(r==0):
        print("Zero")
    elif(r==1):
        print("One")
    elif(r==2):
        print("Two")
    elif(r==3):
        print("Three")
    elif(r==4):
        print("Four")
    elif(r==5):
        print("Five")
    elif(r==6):
        print("Six")
    elif(r==7):
        print("Seven")
    elif(r==8):
        print("Eight")
    elif(r==9):
        print("Nine")
    s = s // 10


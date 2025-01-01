# Palindrome Number = a number which is reverse is equal to the number ex-181,242,989
n = int(input("Enter a number"))
m=n
s=0
while(n!=0):
    r = n%10
    s = s*10+r
    n = n//10
print("Number is Palindrome") if(m==s) else print("Number is not Palindrome")

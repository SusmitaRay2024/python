#Armstrong Number = a number whose sum of cube of individual digit is equal to the number 
#Ex- 153 -> 1^3 + 5^3 + 3^3 => 1 + 125 + 27 => 153

n=int(input("Enter a Number"))
m = n
s = 0
while(n!=0):
    r = n % 10
    s = s + (r*r*r)
    n = n // 10
if(m==s):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
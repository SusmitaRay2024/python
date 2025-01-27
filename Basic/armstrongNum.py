#Armstrong Number = a number whose sum of cube of individual digit is equal to the number 
#Ex- 153 -> 1^3 + 5^3 + 3^3 => 1 + 125 + 27 => 153

number=int(input("Enter a Number"))
original_number = number
sum_of_cubes = 0
while(number!=0):
    digit = number % 10
    sum_of_cubes = sum_of_cubes + (digit**3)
    number = number // 10
if(original_number==sum_of_cubes):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
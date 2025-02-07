#Armstrong Number = a number whose sum of cube of individual digit is equal to the number 
#Ex- 153 -> 1^3 + 5^3 + 3^3 => 1 + 125 + 27 => 153

number=int(input("Enter a Number")) #153
original_number = number
sum_of_cubes = 0
while(number!=0):
    digit = number % 10 #153%10 = 15.3 =3 #15%10 = 1.5 = 5 #1%10 = .1 = 1
    sum_of_cubes = sum_of_cubes + (digit**3) #=0+27 =27 #27+ 5*5*5 =27+125 = 152 #152+1 =153
    number = number // 10 #153//10 =15.3 =15 #15//10 =1.5 =1 #1//10 0.1 =0
if(original_number==sum_of_cubes):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
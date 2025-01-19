# if statement - a block of code that will execute if it's condition is True
age = int(input("How old are you?: "))

if age == 100:
    print("You are a Centuary Old!")
elif age >= 18: 
    print("You are Adult!")
elif age<0:
    print("You haven't been born yet!")
else:
    print("You are a Child!")
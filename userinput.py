name = input("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))
age = age + 1

print("Hello "+name)
print("You are "+ str(age) +" years old") #change age value int to string
print(f"You are {age} years old") #formatted string
print(f"You are {height} cm tall") #formatted string
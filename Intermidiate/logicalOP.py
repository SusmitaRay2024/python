# Logical Operator (and, or, not) -used to check if two or more conditional statements is true

temp = int(input("What is the temperature outside?: "))

# if temp>=0 and temp<=30:
#     print("The temperature is good today!")
#     print("Go outside!")
# elif temp<0 or temp>30:
#     print("The temperature is Bad today!")
#     print("Stay outside!")
    
########################################################

if not (temp>=0 and temp<=30):
    print("The temperature is Bad today!")
    print("Stay outside!")
elif not (temp<0 or temp>30):
    print("The temperature is good today!")
    print("Go outside!")
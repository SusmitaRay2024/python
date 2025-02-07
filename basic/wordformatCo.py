n = int(input("Enter a Number: "))
s = 0

# Reverse the number
while n != 0:   #144 
    r = n % 10  # Get the last digit 14.4
    s = s * 10 + r  # Reverse the digits 0*10+14.4 =14.4
    n = n // 10  # Remove the last digit from n = 1.44

# Iterate through the reversed number
while s != 0:
    r = s % 10  # Extract each digit from the reversed number
    if r == 0:
        print("Zero")
    elif r == 1:
        print("One")
    elif r == 2:
        print("Two")
    elif r == 3:
        print("Three")
    elif r == 4:
        print("Four")
    elif r == 5:
        print("Five")
    elif r == 6:
        print("Six")
    elif r == 7:
        print("Seven")
    elif r == 8:
        print("Eight")
    elif r == 9:
        print("Nine")
    s = s // 10  # Move to the next digit
# in, not in
# It's tracks sequence in data
a= "Hello"
print('e' in a) #True
print('i' in a) #False

s= "Hello Welcome to Python World"
print('Python' in s) #True

email = 'susmita@gmail.com'
print("Valid Email") if ('@' in email) else print("Invalid Email")

m = [10, 5, 70, 30, 35]
x = int(input("Enter a number"))
print ("Searching Success") if (x in m) else print ("Searching Not Succesfull")

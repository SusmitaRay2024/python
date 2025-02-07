import time

# for loop - a statement that will execute it's block of code. 
#          - a limited amount of times
##         While Loop - Unlimited
##         For Loop - limited

for i in range (10): # +1 =10
    print(i)
print("------------------------------------------")
for i in range(50,100): # +1 = 100
    print(i)
print("------------------------------------------")
for i in range (50, 100+1, 2):
    print(i)
print("------------------------------------------")
    
for i in "Corporates Guide":
    print(i)
print("------------------------------------------")
    
    
for i in range (10, 0, -1):
    print(i)
    time.sleep(1)
print("Happy New Year! 2025")
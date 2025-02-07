# x = 20 #global variable

def modify_global():
    global x
    x = 20 #instance variable
    print(x)
    
modify_global()

print(x)
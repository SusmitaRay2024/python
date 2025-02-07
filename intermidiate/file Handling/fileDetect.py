import os


# path= "C:\\Users\\justs\\OneDrive\\Desktop\\folder"
path = "rai.txt"

if os.path.exists(path):
    print("The location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a Directory!")
else: 
    print("That's location doesnot exists!")
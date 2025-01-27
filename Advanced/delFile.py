import os 
import shutil

path = "C:\\Users\\justs\\OneDrive\\Desktop\\test.txt"

try:
    os.remove(path) #delete a file
except:
    print("That file was not found!")
    
######################################################

path = "empty_folder"

try:
    os.rmdir(path) #delete an empty-directory
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that ")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")

##############################################################

path = "folder"

try:
    shutil.rmtree(path) #delete a folder containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that ")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")

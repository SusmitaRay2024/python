import shutil

#copyfile()= copies contents of a file
#copy() = copyfile()+permission mode+ destination can be a directory
#copy2() = copy() + copies metadata (files creation and modification times)

# shutil.copyfile('test.txt', 'copy.txt') #src, dst
shutil.copyfile('test.txt', 'C:\\Users\\justs\\OneDrive\\Desktop\\copy.txt') #src, dst
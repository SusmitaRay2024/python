#Indexing[] = gives access to asequence's element (str, list, tuples)

name = "corporates guide!"

if(name[0].islower()):
    name = name.capitalize()
print(name)

######################################

first_name = name[0:10].upper()
print(first_name)

last_name = name[11:16].lower()
print(last_name)

last_char = name[-1]
print(last_char)
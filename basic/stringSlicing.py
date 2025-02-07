# Slicing - Create a substring by extracting elements from another string 
# indexing[] or slice() [start:stop:step]

name = "Corporates Guide"

first_name = name[0:10] 
last_name = name[11:16]
funky_name = name[0:16:2]
reverse_name = name[::-1]

print(first_name)
print(last_name)
print(funky_name)
print(reverse_name)

#######################################

website1 = "http://google.com"
slice = slice(7, -4)
print(website1[slice]) #google

website2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website2[slice]) #wikipedia
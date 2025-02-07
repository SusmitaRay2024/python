#Sets - Collection which is unordered, unindexed, no duplicate values

utensils = {"fork", "spoon", "knife","knife", "knife"}

utensils.add("napkin")
print(utensils)
utensils.remove("fork")
utensils.clear()
###################################

dishes = {"bowl", "plate", "cup"}

utensils.update(dishes) #utensils+dishes
dishes.update(utensils) #dishes+utensils

for i in utensils:
    print(i)
    
for j in dishes:
    print(j)

# ########################################

dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

# ###########################################

print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))

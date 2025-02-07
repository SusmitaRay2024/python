# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
# squares = []                # create an empty list
# for i in range(1,11):       # create a for loop
#     squares.append(i * i)    # define what each loop iteration should do
# print(squares)

# # create a list AND defines what each loop iteration should do
# squares1 = [i**2 for i in range(1,11)]
# print(squares1)
# --------------------------------------------------------------
students = [100, 90, 80, 70, 60, 50, 40, 30,0]

# pass_studentes= list(filter(lambda x:x>=60, students))
# pass_studentes= [i for i in students if i>=60]
pass_studentes= [i if i>=60 else "Failed" for i in students]
print(pass_studentes)
# --------------------------------------------------------------
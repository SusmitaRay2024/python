#str.format() = optinal method that gives users.
#more control when displaying output

animal = "cow"
item = "moon"
print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format("cow", "moon"))
print("The {1} jumped over the {0}".format(animal, item)) #positional argument
########################################
print("The {animal} jumped over the {item}".format(animal="cow", item="moon")) #keywork argument

######################################
text = "The {} jumped over the {}"
print(text.format(animal,item))
#######################################
name = "Corporates"
print("Hello, my name is {}". format(name))
print("Hello, my name is {:20}. nice to meet you".format(name)) #gives the space after word
print("Hello, my name is {:<20}. nice to meet you".format(name)) #left align
print("Hello, my name is {:>20}. nice to meet you".format(name)) #right align
print("Hello, my name is {:^20}. nice to meet you".format(name)) #center
###################################################################
number = 3.14159
print("The number pi is {:.2f}".format(number))
number = 1000
print("The number pi is {:,}".format(number)) #add comma
print("The number pi is {:b}".format(number)) #binary
print("The number pi is {:o}".format(number)) #octal
print("The number pi is {:X}".format(number)) #Hexa decimal
print("The number pi is {:E}".format(number)) #Scientific notation




# Function - a block of code which is executed only when it is called.

def hello():
    print("hello!")
    print("Have a Nice day!")
    
hello()

###################################3

def hi(name):
    print("hi "+name)
    print("Have a Nice day!")
    
hi("Bro")
    
## if the variable is already declared

def hi(name):
    print("hi "+name)
    print("Have a Nice day!")
my_name = "Bro"
hi(my_name)

## passing more agruments so passing more variable

def hi(first_name, last_name):
    print("hi "+first_name+" "+ last_name)
    print("Have a Nice day!")
hi("Corporates", "Guide")
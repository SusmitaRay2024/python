#**Kwargs - parameter that will pack all arguments into a dictonary.
#useful so that a function can accept a varying amount of keyward arguments

def hello(**kwargs):
    print("Hello "+ kwargs['first']+ " "+ kwargs['last'])
    
hello( middle = "Learning", last = "Guide", first = "Corporates",)

###############################################################

def hello(**kwargs):
    print("Hello ", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")
hello(title = "Mr.", first = "Corporates", middle = "Learining", last = "Guide")
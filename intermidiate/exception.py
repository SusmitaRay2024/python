#Exception = events detected during execution that interrupt the flow of a program.

try:
    numerator = int(input("Enter a number to devide: "))
    denominator = int(input("Enter a number to devide by: "))
    result = numerator/denominator
except ZeroDivisionError as e:
    print(e)
    print("You cannot devide by Zero! Idiot!" )
except ValueError as e:
    print(e)
    print("Enter only number please")    
except Exception as  e:
    print(e)
    print("Something Went wrong :( ")
else: 
    print(result)
finally:
    print("This will always execute")



# numerator = int(input("Enter a number to devide: "))
# denominator = int(input("Enter a number to devide by: "))
# result = numerator/denominator
# print(result)

try:
    x= 10/2
except ZeroDivisionError:
    print("Cannot Devided by Zero.")
else:
    print(x)
    print("No errors occured")
finally:
    print("Excution completed")
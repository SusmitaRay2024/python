try:
    f=input("Enter filenmae")
    file=open(f)
    print(file.read())

except FileNotFoundError:
    print('file not found')
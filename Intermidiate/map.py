# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store  = [("Shirt", 20.00),
          ("pants", 25.00),
          ("jacket", 50.00),
          ("socks",10.00)]

to_INR = lambda data: (data[0],data[1]*87.11)

store_INR = list(map(to_INR, store))

for i in store_INR:
    print(i)
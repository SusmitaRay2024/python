# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

# factorial = [5,4,3,2,1] #5*4 =20 *3 = 60*2 = 120*1 =120
# result = functools.reduce(lambda x, y: x*y, factorial)
# print(result)

alphabet = ["H","E","L","L","O"] #HELLO
word = functools.reduce(lambda x, y: x+y, alphabet)
print(word)
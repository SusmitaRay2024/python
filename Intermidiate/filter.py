# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)


friend = [("Rachel", 19),
          ("Monica", 18),
          ("Phobe",17),
          ("Joey", 16),
          ("Chandeler", 21),
          ("Ross", 20)]

age  = lambda data:data[1] >= 18

travel_buddies = list(filter(age,friend))

for i in travel_buddies:
    print(i)
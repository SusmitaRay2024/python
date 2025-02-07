# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# -------------------------------------------------------------------------


# cities_in_F = {'New York':32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# cities_in_C = {key:round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}

# print(cities_in_C)

weather = {'New York':"Snowing", 'Boston': "Sunny", 'Los Angeles': "Sunny", 'Chicago':"Cloudy"}

sunny_weather = {key: value for (key,value) in weather.items() if value == "Sunny"}

print(sunny_weather)
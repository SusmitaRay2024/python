import re

# # Pattern to match any character
# pattern = r'.'
# text = "Hello World"
# matches = re.findall(pattern, text)

# print(matches)  # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

#---------------------------------------------------------------------

# # Pattern to match 'Hello' only at the start
# pattern = r'^Hello'
# text = "Hello World"
# matches = re.findall(pattern, text)

# print(matches)  # Output: ['Hello']

#---------------------------------------------------------------------------


# # Pattern to match 'World' only at the end
# pattern = r'World$'
# text = "Hello World"
# matches = re.findall(pattern, text)

# print(matches)  # Output: ['World']

#------------------------------------------------------------------------


# # Pattern to match 'a' followed by zero or more 'b's
# pattern = r'ab*'
# text = "abbbbb abb ab abbb"
# matches = re.findall(pattern, text)

# print(matches)  # Output: ['abbbbb', 'abb', 'ab', 'abbb']

#----------------------------------------------------------------------------


# # Pattern to match 'a' followed by one or more 'b's
# pattern = r'ab+'
# text = "abbbbb abb ab abbb"
# matches = re.findall(pattern, text)

# print(matches)  # Output: ['abbbbb', 'abb', 'abbb']

#-------------------------------------------------------------------------------


# # Pattern to match 'a' followed by zero or one 'b'
# pattern = r'ab?'
# text = "ab abb a abbb"
# matches = re.findall(pattern, text)

# print(matches)  # Output: ['ab', 'ab', 'a']

#-------------------------------------------------------------------

# Pattern to match 'a' followed by exactly 3 'b's
pattern = r'ab{3}'
text = "abbbb abbb ab abbbb"
matches = re.findall(pattern, text)

print(matches)  # Output: ['abbb', 'abbb']


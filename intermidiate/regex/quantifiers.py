import re

# # Pattern to match 'a' followed by zero or more 'b's
# pattern = r'ab*'
# text = "abbbbb abb ab abbb"
# matches = re.findall(pattern, text)

# print(matches)  # Output: ['abbbbb', 'abb', 'ab', 'abbb']

#-----------------------------------------------------------------------

# # Pattern to match 'a' followed by one or more 'b's
# pattern = r'ab+'
# text = "abbbbb abb ab abbb"
# matches = re.findall(pattern, text)

# print(matches)  # Output: ['abbbbb', 'abb', 'abbb']

#------------------------------------------------------------------------------

# Pattern to match 'a' followed by zero or one 'b'
pattern = r'ab?'
text = "ab abb a abbb"
matches = re.findall(pattern, text)

print(matches)  # Output: ['ab', 'ab', 'a']

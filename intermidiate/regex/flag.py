import re

# # Pattern to match 'hello' regardless of case
# pattern = r'hello'
# text = "Hello World! hello world!"
# matches = re.findall(pattern, text, flags=re.IGNORECASE)

# print(matches)  # Output: ['Hello', 'hello']

#----------------------------------------------------------------------------


# # Pattern to match the beginning of a line
# pattern = r'^hello'
# text = """hello world
# hello python
# hello regex"""
# matches = re.findall(pattern, text, flags=re.MULTILINE)

# print(matches)  # Output: ['hello', 'hello', 'hello']

#-------------------------------------------------------------------------


# # Pattern to match any character including newlines
# pattern = r'hello.world'
# text = """hello
# world"""
# matches = re.findall(pattern, text, flags=re.DOTALL)

# print(matches)  # Output: ['hello\nworld']

#-----------------------------------------------------------------------


# Pattern with verbose mode, using whitespace and comments
pattern = r"""
    ^\d{3}      # Area code
    -           # Dash separator
    \d{3}       # First 3 digits
    -           # Dash separator
    \d{4}       # Last 4 digits
"""
text = "123-456-7890"
matches = re.findall(pattern, text, flags=re.VERBOSE)

print(matches)  # Output: ['123-456-7890']



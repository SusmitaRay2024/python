import re

# Pattern with a group to match a word followed by a number
pattern = r'(\w+)(\d+)'
text = "abc123 def456 ghi789"
matches = re.findall(pattern, text)

print(matches)  # Output: [('abc', '123'), ('def', '456'), ('ghi', '789')]

# --------------------------------------------------------------------------------------


# # Pattern with two groups
# pattern = r'(\w+)(\d+)'
# text = "abc123"
# match = re.search(pattern, text)

# if match:
#     print(match.group(0))  # Output: 'abc123' (the entire match)
#     print(match.group(1))  # Output: 'abc' (first group)
#     print(match.group(2))  # Output: '123' (second group)

# -------------------------------------------------------------------------


# # Pattern with non-capturing group
# pattern = r'(?:\w+)-(\d+)'
# text = "abc-123 def-456 ghi-789"
# matches = re.findall(pattern, text)

# print(matches)  # Output: ['123', '456', '789']

# ------------------------------------------------------------------------
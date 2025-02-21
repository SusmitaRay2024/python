import re

pattern = r'[a-zA-Z0-9]'  # Matches any alphanumeric character
text = "apple 123 BANANA"
matches = re.findall(pattern, text)

print(matches)  # Output: ['a', 'p', 'p', 'l', 'e', '1', '2', '3', 'B', 'A', 'N', 'A', 'N', 'A']

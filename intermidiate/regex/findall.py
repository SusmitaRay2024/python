import re

# Pattern to match one or more digits
pattern = r'\d+'

# String to search
text = "There are 123 apples, 456 oranges, and 789 bananas."

# Find all matches
matches = re.findall(pattern, text)

print(matches)  # Output: ['123', '456', '789']
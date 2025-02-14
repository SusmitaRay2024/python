import re

# Pattern to match one or more digits
pattern = r'\d+'

# String to search
text = "There are 123 apples, 456 oranges, and 789 bananas."

# Find all matches using finditer
matches = re.finditer(pattern, text)

# Iterate over the matches and print match details
for match in matches:
    print(f"Match: {match.group()} | Start: {match.start()} | End: {match.end()}")
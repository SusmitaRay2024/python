import re

# Compile the pattern
pattern = re.compile(r'\d+')  # Match one or more digits

# Search in the string
result = pattern.search("The price is 100 dollars")
if result:
    print("Match found:", result.group())  # Outputs: Match found: 100
else:
    print("No match found.")

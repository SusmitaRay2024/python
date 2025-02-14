import re

# Regex pattern to extract phone numbers in various formats
pattern = r'\+?(\d{1,3})?[-.\s]?\(?(\d{1,4})\)?[-.\s]?(\d{1,4})[-.\s]?(\d{1,4})'

text = "Call me at +1-234-567-8900 or (987) 654-3210."
matches = re.findall(pattern, text)

print(matches)  # Output: [('1', '234', '567', '8900'), ('987', '654', '321', '210')]

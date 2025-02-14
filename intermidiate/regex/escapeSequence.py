import re

# Pattern to match a dot (.), asterisk (*), and dollar sign ($) literally
pattern = r'\.|\\|\$'  # Escape dot, backslash, and dollar sign
text = "This is a test string with dot., asterisk*, and dollar$."
matches = re.findall(pattern, text)

print(matches)  # Output: ['.', '*', '$']

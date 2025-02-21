import re

# Regex pattern to validate an email address
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

email = "test@example.com"
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

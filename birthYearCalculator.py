from datetime import datetime

# Input today's date and birth date as strings
date1_input = input("Enter Today's Date (YYYY-MM-DD): ")
date2_input = input("Enter your Birth Date (YYYY-MM-DD): ")

# Parse the input strings into datetime objects
date1 = datetime.strptime(date1_input, "%Y-%m-%d")
date2 = datetime.strptime(date2_input, "%Y-%m-%d")

# Calculate the difference in total days
difference_in_days = (date1 - date2).days

# Calculate years, months, and remaining days
years = difference_in_days // 365
remaining_days = difference_in_days % 365
months = remaining_days // 30
days = remaining_days % 30

# Print the difference in years, months, and days
print(f"The difference is {years} years, {months} months, and {days} days.")

#Python program for extracting dates from given text
import re

#sample text containing dates 
text = "On 2023-09-17, the conference will begin. The event will end on 2023-09-19"

#Regex pattern to match dates in the format YYYY-MM-DD
date_pattern = r"\d{4}-\d{2}-\d{2}"

#Find all matches of the date pattern in the text
dates = re.findall(date_pattern,text)

#print the extracted dates
print(dates)
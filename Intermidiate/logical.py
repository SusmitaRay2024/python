# &, or, not
print((15 > 10) and (9 < 5))  # False
print((15 > 10) or (9 < 5))   # True

# 'and', 'or' are short circuit operators
percentage = int(input("Enter a percentage: "))
is_second_class = (percentage >= 45) and (percentage < 60)
is_pass = (percentage >= 45) or (percentage < 60)
print(is_second_class, is_pass)

condition_and = (5 >= 10) and (17 < 5) and (6 > 6)
condition_or = (5 >= 10) or (17 < 5) or (6 > 6)
print(condition_and, condition_or)

# 'not' operator
# Just change the condition
first_value = 15
second_value = 10
is_first_greater = (first_value > second_value)
is_not_first_greater = not (first_value > second_value)
print(is_first_greater, is_not_first_greater)
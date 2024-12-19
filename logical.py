# &, or, not
print((15>10) and (9<5)) #False
print((15>10) or (9<5)) #True

#and, or are short circuit operator
per = int(input("Enter a percentage"))
x = (per>=45)and(per<60)
y = (per>=45)or(per<60)
print(x, y)

x = (5>=10)and(17<5)and(6>6)
y = (5>=10)or(17<5)or(6>6)
print(x, y)

#not operator
#Just change the condition
a = 15
b = 10
c = (a>b)
d = not(a>b)
print(c, d)
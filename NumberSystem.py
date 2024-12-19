#Binary-01110010-base2, Decimal-0to9-base10, Octal-0to7-base-8, HexaDecimal-0to15-base16 (10-15=A-F)

#Octal to Decimal
#(13)8 = (?)10
a=0O13
print(a) #11
#(113)8 = (?)10
b=0O113
print(b) #75

#HexaDecimal to Decimal
#(2A)16 = (?)10
c=0X2A
print(c) #42
#(DAD)16 = (?)10
d=0XDAD
print(d) #3501

#Binary to Decimal
#(1011)2 = (?)10
e=0B1011
print(e) #11
#(101101)2 = (?)10
f=0B101101
print(f) #45

#0B-> Binary, 0O-> Octal, 0X-> Hexadecimal, default id Decimal
#Reverse 

#Decimal to Binary - bin()
g = 13
print(bin(g))

#Decimal to Binary - oct()
h = 13
print(oct(h))

#Decimal to Binary - hex()
i = 36
print(hex(i))

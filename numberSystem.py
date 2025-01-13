# Binary (Base-2), Decimal (Base-10), Octal (Base-8), Hexadecimal (Base-16)
# Binary: 0B, Octal: 0O, Hexadecimal: 0X (default is Decimal)

# Octal to Decimal
# (13)8 = (?)10
octal_number_1 = 0O13
print(octal_number_1)  # 11

# (113)8 = (?)10
octal_number_2 = 0O113
print(octal_number_2)  # 75

# Hexadecimal to Decimal
# (2A)16 = (?)10
hexadecimal_number_1 = 0X2A
print(hexadecimal_number_1)  # 42

# (DAD)16 = (?)10
hexadecimal_number_2 = 0XDAD
print(hexadecimal_number_2)  # 3501

# Binary to Decimal
# (1011)2 = (?)10
binary_number_1 = 0B1011
print(binary_number_1)  # 11

# (101101)2 = (?)10
binary_number_2 = 0B101101
print(binary_number_2)  # 45

# Reverse Conversions

# Decimal to Binary - bin()
decimal_to_binary = 13
print(bin(decimal_to_binary))  # 0b1101

# Decimal to Octal - oct()
decimal_to_octal = 13
print(oct(decimal_to_octal))  # 0o15

# Decimal to Hexadecimal - hex()
decimal_to_hexadecimal = 36
print(hex(decimal_to_hexadecimal))  # 0x24

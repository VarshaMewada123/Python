# Arithmetic Operators
a = 10
b = 3

print("Addition:", a + b)          # 13
print("Subtraction:", a - b)       # 7
print("Multiplication:", a * b)    # 30
print("Division:", a / b)          # 3.333...
print("Floor Division:", a // b)   # 3
print("Modulus:", a % b)           # 1
print("Exponentiation:", a ** b)   # 1000

# Comparison Operators
print("Equal:", a == b)            # False
print("Not Equal:", a != b)        # True
print("Greater Than:", a > b)      # True
print("Less Than:", a < b)         # False
print("Greater or Equal:", a >= b) # True
print("Less or Equal:", a <= b)    # False

# Logical Operators
x = True
y = False

print("AND:", x and y)             # False
print("OR:", x or y)               # True
print("NOT:", not x)               # False

# Assignment Operators
c = 5
c += 3    # same as c = c + 3
print("c after += 3:", c)          # 8

# Bitwise Operators
print("Bitwise AND:", a & b)       # 2
print("Bitwise OR:", a | b)        # 11
print("Bitwise XOR:", a ^ b)       # 9

# Membership Operators
list1 = [1, 2, 3]
print("2 in list1:", 2 in list1)   # True
print("4 not in list1:", 4 not in list1) # True

# Identity Operators
d = 10
print("a is d:", a is d)           # True (same memory reference)
print("a is not b:", a is not b)   # True

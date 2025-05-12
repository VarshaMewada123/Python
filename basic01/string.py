# Creating strings
s1 = 'Hello'
s2 = "World"
s3 = '''This is a multi-line
string in Python'''

# Printing strings
print(s1)             # Output: Hello
print(s2)             # Output: World
print(s3)             # Output:This is a  multi-line 
                      # string in Python

# String concatenation
full = s1 + " " + s2
print("Concatenated String:", full)

# String repetition
print("Repeat:", s1 * 3)  # HelloHelloHello

# Accessing characters
print("First character:", s1[0])   # H
print("Last character:", s1[-1])  # o

# String slicing
print("Slice:", s1[1:4])  # ell

# String methods
print("Uppercase:", s1.upper())
print("Lowercase:", s2.lower())
print("Length:", len(full))
print("Replace:", full.replace("World", "Python"))
print("Split:", full.split())  # Splits into list

# Checking substring
print("Is 'Hell' in s1?", 'Hell' in s1)

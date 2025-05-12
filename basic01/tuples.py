# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)

# Accessing elements in a tuple (using index)
print("Element at index 0:", my_tuple[0])  # Output: 1
print("Element at index 3:", my_tuple[3])  # Output: 4

# Slicing a tuple (Getting a range of elements)
print("Sliced Tuple (from index 1 to 3):", my_tuple[1:4])  # Output: (2, 3, 4)

# Concatenating two tuples
another_tuple = (6, 7, 8)
concatenated_tuple = my_tuple + another_tuple
print("Concatenated Tuple:", concatenated_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7, 8)

# Repeating a tuple
repeated_tuple = my_tuple * 2
print("Repeated Tuple:", repeated_tuple)  # Output: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

# Checking membership in a tuple
print("Is 3 in the tuple?", 3 in my_tuple)  # Output: True
print("Is 10 in the tuple?", 10 in my_tuple)  # Output: False

# Tuple length
print("Length of the tuple:", len(my_tuple))  # Output: 5

# Nested Tuples
nested_tuple = (1, 2, (3, 4), 5)
print("Nested Tuple:", nested_tuple)
print("Element at index 2:", nested_tuple[2])  # Output: (3, 4)
print("Element at index 2, index 0:", nested_tuple[2][0])  # Output: 3

# Tuples with different data types
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)

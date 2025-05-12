# Creating a list
my_list = [1, 2, 3, 4, 5]

# Printing the list
print("Original List:", my_list)

# Accessing elements by index
print("First Element:", my_list[0])  # Output: 1
print("Last Element:", my_list[-1])  # Output: 5

# Slicing a list
print("Slice (from 1 to 3):", my_list[1:4])  # Output: [2, 3, 4]

# Modifying a list
my_list[2] = 10  # Changing the third element (index 2)
print("Modified List:", my_list)  # Output: [1, 2, 10, 4, 5]

# Adding elements
my_list.append(6)  # Adds 6 to the end
print("After Append:", my_list)  # Output: [1, 2, 10, 4, 5, 6]

my_list.insert(2, 7)  # Inserts 7 at index 2
print("After Insert:", my_list)  # Output: [1, 2, 7, 10, 4, 5, 6]

# Removing elements
my_list.remove(10)  # Removes the first occurrence of 10
print("After Remove:", my_list)  # Output: [1, 2, 7, 4, 5, 6]

# Popping an element
popped_element = my_list.pop()  # Removes and returns the last element
print("Popped Element:", popped_element)  # Output: 6
print("After Pop:", my_list)  # Output: [1, 2, 7, 4, 5]

# Length of the list
print("Length of List:", len(my_list))  # Output: 5

# Checking if an element is in the list
print("Is 7 in the list?", 7 in my_list)  # Output: True
print("Is 10 in the list?", 10 in my_list)  # Output: False

# List with mixed data types
mixed_list = [1, "Python", 3.14, True]
print("Mixed List:", mixed_list)

# Nested list (list inside a list)
nested_list = [[1, 2, 3], [4, 5, 6]]
print("Nested List:", nested_list)
print("Accessing nested list element:", nested_list[1][2])  # Output: 6

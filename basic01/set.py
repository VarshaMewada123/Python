# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)  # Output: {1, 2, 3, 4, 5}

# Adding an element to the set
my_set.add(6)
print("After Adding 6:", my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Adding multiple elements to the set using update()
my_set.update([7, 8, 9])
print("After Updating with multiple elements:", my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

# Removing an element from the set
my_set.remove(9)  # Removes 9 from the set
print("After Remove 9:", my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# If the element does not exist, remove() raises a KeyError
# my_set.remove(10)  # Uncommenting this line will raise KeyError

# Using discard() to remove an element (won't raise an error if element doesn't exist)
my_set.discard(10)  # 10 doesn't exist, so no error
print("After Discarding 10:", my_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Popping an element (removes and returns an arbitrary element)
popped_element = my_set.pop()
print("Popped Element:", popped_element)
print("After Pop:", my_set)

# Checking if an element is in the set
print("Is 4 in the set?", 4 in my_set)  # Output: True
print("Is 10 in the set?", 10 in my_set)  # Output: False

# Length of the set
print("Length of Set:", len(my_set))  # Output: 7

# Set with mixed data types
mixed_set = {1, "Python", 3.14, True}
print("Mixed Set:", mixed_set)

# Set with duplicate elements (duplicates will be removed)
set_with_duplicates = {1, 2, 3, 3, 2, 1}
print("Set with Duplicates:", set_with_duplicates)  # Output: {1, 2, 3}

# Set Operations: Union, Intersection, Difference
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union: Elements in either set
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Elements in both sets
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)  # Output: {3, 4}

# Difference: Elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b:", difference_set)  # Output: {1, 2}

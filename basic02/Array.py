# Creating a list
my_list = [3, 1, 4, 1, 5, 9]

# append() - Adds an element at the end
my_list.append(2)
print("After append(2):", my_list)

# insert() - Adds an element at a specific index
my_list.insert(2, 10)
print("After insert(2, 10):", my_list)

# extend() - Adds elements from another iterable
my_list.extend([6, 7])
print("After extend([6, 7]):", my_list)

# pop() - Removes and returns element at index (default last)
removed = my_list.pop()
print("After pop():", my_list, "| Removed:", removed)

# remove() - Removes first matching element
my_list.remove(1)
print("After remove(1):", my_list)

# index() - Finds the first index of a value
idx = my_list.index(4)
print("Index of 4:", idx)

# count() - Counts occurrences
cnt = my_list.count(1)
print("Count of 1:", cnt)

# sort() - Sorts the list in place
my_list.sort()
print("After sort():", my_list)

# reverse() - Reverses the list
my_list.reverse()
print("After reverse():", my_list)

# copy() - Returns a shallow copy
copied_list = my_list.copy()
print("Copied List:", copied_list)

# clear() - Removes all items
copied_list.clear()
print("After clear():", copied_list)

# Slicing - Extract part of the list
sliced = my_list[2:5]
print("Sliced [2:5]:", sliced)

# Extra methods/features

# len() - Length of list
print("Length:", len(my_list))

# in - Membership check
print("Is 9 in the list?", 9 in my_list)

# del - Delete an element or entire list
del my_list[0]
print("After del my_list[0]:", my_list)

# List comprehension - Creating list using logic
squared = [x**2 for x in range(5)]
print("Squares 0-4:", squared)

# Importing array module
import array

# Creating an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Displaying the array
print("Array:", arr)

# Accessing elements in the array
print("First element:", arr[0])  # Output: 1
print("Last element:", arr[-1])  # Output: 5

# Modifying an element in the array
arr[2] = 10
print("Array after modification:", arr)  # Output: array('i', [1, 2, 10, 4, 5])

# Appending an element to the array
arr.append(6)
print("Array after appending 6:", arr)  # Output: array('i', [1, 2, 10, 4, 5, 6])

# Removing an element from the array
arr.remove(4)
print("Array after removing 4:", arr)  # Output: array('i', [1, 2, 10, 5, 6])

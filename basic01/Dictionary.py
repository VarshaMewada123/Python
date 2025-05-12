# Creating a dictionary
my_dict = {
    "name": "Varsha", 
    "age": 21, 
    "city": "Indore"
}

# Accessing values using keys
print("Name:", my_dict["name"])  # Output: varsha
print("Age:", my_dict["age"])    # Output: 21

# Modifying a value
my_dict["age"] = 31
print("Updated Age:", my_dict["age"])  # Output: 31

# Adding a new key-value pair
my_dict["job"] = "Engineer"
print("Updated Dictionary:", my_dict)

# Removing a key-value pair using pop()
removed_value = my_dict.pop("city")
print("Removed Value:", removed_value)  # Output: Indore
print("Dictionary after removal:", my_dict)

# Checking if a key exists
print("Is 'name' key present?", "name" in my_dict)  # Output: True
print("Is 'city' key present?", "city" in my_dict)  # Output: False

# Iterating over a dictionary (keys, values, items)
print("Keys:")
for key in my_dict:
    print(key)

print("Values:")
for value in my_dict.values():
    print(value)

print("Items (Key-Value pairs):")
for key, value in my_dict.items():
    print(key, ":", value)

# Dictionary length
print("Length of dictionary:", len(my_dict))  # Output: 3

# Copying a dictionary
copied_dict = my_dict.copy()
print("Copied Dictionary:", copied_dict)

# Nested dictionary
nested_dict = {
    "person1": {"name": "John", "age": 30},
    "person2": {"name": "Anna", "age": 25}
}
print("Nested Dictionary:", nested_dict)
print("Accessing nested value:", nested_dict["person1"]["name"])  # Output: John

# Using get() method
print("Getting age using get:", my_dict.get("age"))  # Output: 31
print("Getting non-existing key using get:", my_dict.get("city", "Not Found"))  # Output: Not Found

# Merging dictionaries using update()
another_dict = {"gender": "Male", "country": "USA"}
my_dict.update(another_dict)
print("Dictionary after update:", my_dict)

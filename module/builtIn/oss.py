# Importing the os module
import os

# 1. os.getcwd(): Returns the current working directory
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")

# 2. os.listdir(path): Returns a list of entries in the directory given by path
# Listing files in the current directory
directory_contents = os.listdir(current_directory)
print(f"Contents of the current directory: {directory_contents}")

# 3. os.rename(src, dst): Renames the file or directory src to dst
# First, we'll create a test file to rename
test_file = "test_file.txt"
with open(test_file, "w") as file:
    file.write("This is a test file.")

# Renaming the file
new_name = "renamed_file.txt"
os.rename(test_file, new_name)
print(f"File renamed from '{test_file}' to '{new_name}'")

# 4. os.remove(path): Removes the file path
# Removing the renamed file
os.remove(new_name)
print(f"File '{new_name}' has been removed.")

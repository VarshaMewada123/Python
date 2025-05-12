# Function to find the maximum of two numbers
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

# Lambda function for the same operation
max_lambda = lambda a, b: a if a > b else b

# Calling both functions
print("Max using function:", max_of_two(10, 20))  # Output: Max using function: 20
print("Max using lambda:", max_lambda(10, 20))  # Output: Max using lambda: 20

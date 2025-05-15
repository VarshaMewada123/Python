# This is a decorator function
def my_decorator(func):
    def wrapper():
        print("Before calling the function")  # Pre-processing
        func()  # Calling the original function
        print("After calling the function")   # Post-processing
    return wrapper  # Closure: 'wrapper' remembers 'func'

# Now use the decorator
@my_decorator
def say_hello():
    print("Hello, world!")

# Call the decorated function
say_hello()

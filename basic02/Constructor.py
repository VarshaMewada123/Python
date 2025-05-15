# Class with all types of constructor examples
class Person:

    # Constructor with default argument (acts as both default and parameterized)
    def __init__(self, name="Unknown", age=None):
        self.name = name
        self.age = age

        # Check what kind of data was passed
        if name == "Unknown" and age is None:
            print("Default Constructor Called")
        elif age is None:
            print(f"Constructor with only name: {self.name}")
        else:
            print(f"Parameterized Constructor: Name = {self.name}, Age = {self.age}")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# -------------------------------------------
# Case 1: Default Constructor (no arguments)
print("Case 1: Default Constructor")
p1 = Person()
p1.display()
print()

# Case 2: Constructor with only name
print("Case 2: Constructor with one argument")
p2 = Person("Varsha")
p2.display()
print()

# Case 3: Parameterized Constructor (name and age)
print("Case 3: Parameterized Constructor")
p3 = Person("Varsha", 21)
p3.display()
print()

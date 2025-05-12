class Dog:
    species = "Canine"  # Class attribute
#In Python, the constructor __init__() is a special method that is called 
# when an object is created. However, __init__() is not just a normal method — it is a 
# special method, often called a dunder method (because it has double underscores 
# before and after its name).
# Can you change the name of the constructor?
# No, you cannot change the name of the constructor in Python. 
# The constructor must always be named __init__().
# Why? Because:
# Python defines it: The __init__() method is defined by Python itself, 
# and this special method is automatically called when an object is created 
# from the class. Python expects this specific method name.
# Standard Naming Convention: Python relies on the naming 
# convention (like __init__(), __str__(), etc.) to recognize when to call certain methods.
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute
        # how we can create any obejct of the class
        dog1=Dog("Qw",1)
        print(dog1.name)
        


   
    
# Types of Abstraction:
# Partial Abstraction: Abstract class contains both abstract and concrete methods.
# Full Abstraction: Abstract class contains only abstract methods (like interfaces).
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):

    @abstractmethod
    def make_sound(self):   # Abstract method (no body)
        pass

# Child class 1
class Dog(Animal):
    def make_sound(self):
        return "Bark"

# Child class 2
class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Creating objects
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Bark
print(cat.make_sound())  # Output: Meow

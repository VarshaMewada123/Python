class Dog:
    def speak(self):
        return "Bark"

class Cat:
    def speak(self):
        return "Meow"

def animal_sound(animal):
    print(animal.speak())

d = Dog()
c = Cat()

animal_sound(d)  # Output: Bark
animal_sound(c)  # Output: Meow
#method overriding 
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.sound()  # Output: Animal makes a sound
d.sound()  # Output: Dog barks
c.sound()  # Output: Cat meows

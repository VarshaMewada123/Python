class parent:
    def add(a,b):
        print(a+b)
# inheritance single 
class chlid(parent): 
        def multi(a,b):
            print(a*b)
#multilevel inheritance            
class Animal:
    def eat(self):
        print("Eating...")
    def sound(self):
        print("Animal makes a sound")
    

class Dog(Animal):
    def bark(self):
        print("Barking...")

class Puppy(Dog):
    def weep(self):
        print("Weeping...")

# Object of Puppy class
puppy = Puppy()
puppy.eat()   # Inherited from Animal
puppy.bark()  # Inherited from Dog
puppy.weep()  # Defined in Puppy

class Cat(Animal):
    def sound(self):  # Overrides parent method
        print("Cat says Meow")

c = Cat()
c.sound()  # Output: Cat says Meow
# multiple inheritance 
class Father:
    def skills(self):
        print("Maths and Driving")

class Mother:
    def talents(self):
        print("Singing and Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills()     # Inherited from Father
c.talents()    # Inherited from Mother
#Hierarchical Inheritance
#Definition: Multiple child classes inherit from the same parent class.
class Parent:
    def home(self):
        print("Owns a house")

class Son(Parent):
    def bike(self):
        print("Has a bike")

class Daughter(Parent):
    def scooty(self):
        print("Has a scooty")

s = Son()
d = Daughter()
s.home()      # From Parent
d.home()      # From Parent
#hybride inheritance 
class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C:
    def showC(self):
        print("Class C")

class D(B, C):  # Hybrid: D inherits from B (which inherits from A) and C
    def showD(self):
        print("Class D")

d = D()
d.showA()
d.showB()
d.showC()
d.showD()



class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

# Both classes have the same method `fly`
def make_it_fly(flyable_thing):
    flyable_thing.fly()

# Passing objects of Bird and Airplane to the same function
bird = Bird()
plane = Airplane()

make_it_fly(bird)  # Output: Bird is flying
make_it_fly(plane) # Output: Airplane is flying

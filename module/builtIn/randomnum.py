# Importing the random module
import random

# 1. random.random(): Returns a random float between 0.0 and 1.0
random_float = random.random()
print(f"Random float between 0.0 and 1.0: {random_float}")

# 2. random.randint(a, b): Returns a random integer between a and b (inclusive)
random_int = random.randint(10, 50)
print(f"Random integer between 10 and 50: {random_int}")

# 3. random.choice(sequence): Returns a randomly selected element from a non-empty sequence
colors = ['red', 'blue', 'green', 'yellow']
random_choice = random.choice(colors)
print(f"Randomly selected color: {random_choice}")

# 4. random.shuffle(sequence): Shuffles the sequence in place
numbers = [1, 2, 3, 4, 5]
print(f"Original list before shuffling: {numbers}")
random.shuffle(numbers)
print(f"List after shuffling: {numbers}")

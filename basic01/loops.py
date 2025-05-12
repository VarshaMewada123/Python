# Example: Print each item in a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Example: Print numbers 1 to 5
for i in range(1, 6):
    print(i)
# Example: Print numbers from 1 to 5 using while loop
count = 1

while count <= 5:
    print("Varsha")
    count += 1  # Increment count to avoid infinite loop
# Break example – exits the loop when condition met
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Continue example – skips the current iteration
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
# else block runs only if loop is not broken
for i in range(3):
    print(i)
else:
    print("Loop completed without break")

# If break happens, else won’t run
for i in range(3):
    if i == 1:
        break
    print(i)
else:
    print("This won't print because of break")

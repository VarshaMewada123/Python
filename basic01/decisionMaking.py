# Example: Decision making based on age

age = 18

if age < 13:
    print("You are a child.")       # Executes if age is less than 13
elif age >= 13 and age < 18:
    print("You are a teenager.")    # Executes if age is between 13 and 17
else:
    print("You are an adult.")      # Executes if age is 18 or more

# Example: Checking if a number is even or odd

num = 7

if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

# Nested if example

marks = 85

if marks >= 50:
    if marks >= 75:
        print("Distinction")
    else:
        print("Pass")
else:
    print("Fail")

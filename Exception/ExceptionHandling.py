# Exception Handling in Python

try:
    # Code that may raise an exception
    num1 = int(input("Enter a number: "))  # Taking input and converting to integer
    num2 = int(input("Enter another number: "))  # Taking second input and converting to integer
    result = num1 / num2  # Trying to divide
    print("Result is:", result)

except ZeroDivisionError:  # Handling division by zero error
    print("Error: You cannot divide by zero!")

except ValueError:  # Handling invalid input (non-integer) error
    print("Error: Please enter valid integers.")

else:  # Executes if no exceptions were raised in the try block
    print("Operation completed successfully.")

finally:  # Executes no matter what (even if there was an exception)
    print("Execution completed.")

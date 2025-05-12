import logging

try:
    n = 0
    res = 100 / n       # This raises ZeroDivisionError


except Exception as e:
    print("Enter a valid number!",e)     

except ZeroDivisionError:
    print("You can't divide by zero!")   # This will execute
   

else:
    print("Result is", res)

finally:
    print("Execution complete.")
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")


try:
    set(-5)
except ValueError as e:
    print(e)
try:
    set2(12)
except AgeLessException as e1:
    print(e)
ging
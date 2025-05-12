# Using the pass keyword
# The 'pass' keyword is a null operation. It is used when a statement is syntactically required, but no action is needed.

def functionWithPass():
    pass  # The function does nothing but avoids syntax error




# Using the break keyword
# The 'break' keyword is used to exit from a loop prematurely when a condition is met.

for i in range(5):
    if i == 3:
        break  # Breaks the loop when i equals 3
    print(i)  # Output: 0 1 2



# Using the continue keyword
# The 'continue' keyword is used to skip the rest of the current loop iteration and move to the next iteration.

for i in range(5):
    if i == 3:
        continue  # Skips the iteration when i equals 3
    print(i)  # Output: 0 1 2 4



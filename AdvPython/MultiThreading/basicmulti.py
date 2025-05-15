import threading
import time
# How do you create and start a thread?
# Threads can be created using the threading.Thread class, 
# passing a target function and its arguments.
# The thread is started using the start() method.
# Task 1
def task1():
    for i in range(5):
        print(f"Task 1 - Count: {i}")
        time.sleep(1)  # Simulate delay

# Task 2
def task2():
    for i in range(5):
        print(f"Task 2 - Count: {i}")
        time.sleep(1)

# Creating threads
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

# Starting threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("All tasks done.")

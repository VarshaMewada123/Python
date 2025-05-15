import threading


def greet(name):
    print(f"Hello, {name}!")

# Pass argument to thread using args
t = threading.Thread(target=greet, args=("Varsha",))
t2=threading.Thread(target=greet,args=("Cubexo",))
t.start()
t.join()
t2.start()
# args=("Varsha")     # This is not a tuple, it's just a string
# args=("Varsha",)    # This is a tuple with one element
# and in the tuple if single value is present then we have to put a comma
# threading.Thread(target=..., args=(...))

# multiprocessing.Process(target=..., args=(...))
# ye args as tuple expect karte hai 


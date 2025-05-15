def Outer_Fun(msg):
    def Inner_fun():
        print(f"Message is: {msg}")  # string formatting sahi kiya
    return Inner_fun  # yeh outer function ka return hai, properly indented

# create a closure
my_closure = Outer_Fun("Hello from Closure!")  # outer_function runs here and returns inner_function

# now call the inner function (which remembers 'msg')
my_closure()  # Output: Message is: Hello from Closure!

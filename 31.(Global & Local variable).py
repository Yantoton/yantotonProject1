print(f"Global x is {x}")
hello()
print(f"Global x is {x}")

x = 10

def my_function():
    global x
    x = 5 # this will change the value of the global variable of x
    y = 6 #this is a local variable
    print(y)

my_function()
print(x)

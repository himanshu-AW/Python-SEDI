# function: a function is a block of code that perform a specific task it helps in organzing port making it reusable and improving readability.

# Argunment: values pass to function when it's called.
# parameters: variables that receive the argumnets with in the function.

# def funcName(parameters):
    # body of the function
    # return statement to return a value

def greet(name):
    print("Hello", name)

a=greet("Himanshu")
# a
# print(a)

# sum of twom numbers
def SUM(n1, n2):
    return n1 + n2
result = SUM(5, 10)
print(result)

# power of x^y
def POWER(x,y):
    return x**y
result = POWER(2, 3)
print(result)

# Area of Rectangle
def area_of_rectangle(l,b):
    return l * b
result = area_of_rectangle(5,8)
print(result)

# use help() or __doc__() attribute to access a function documentations

def my_function(x,y):
    '''there are two variables which add up and return its sum'''
    print("this is inner body in function body")
    '''This is 2nd doc string'''
    return x + y
help(my_function)
print(my_function.__doc__)

# How functions are executed in memory ?
# 1st: The function code in  memory.
# 2nd: When a function is called, a new function is created on the call-stack.
#3rd:  Argunments are passed to the funciton and their values are stored in the function frame.
# 4th: The code is executed within the function.
# 5th: If the function returns a value, it stored in callers frame.
# 6th: The function frame is pop from the call-stack.


# local vs global
a=10
def demo(aa):
    a=110
    b=20
    print(a)
    print(b)
    print(aa)
demo(a)
print(a)  # 10

# nested functions
def outer():
    x=10
    def inner():
        print(x)
        return"inner function called"
    print(inner())

outer()

# delete function
del outer

# outer()

# return:-
    # Return statement is used to exit a function and return a value.
    # It can be used to return multiple values from a function.
    # It can be used to break the loop.

def multiply(a,b):
    if b == 0:
        return 0
    return a+multiply(a,b-1)
print(multiply(5, 3))

def greet():
    print("Hello")
    return
greet()

# Lambda function/ anonymous function:-
    # A lambda function is a small anonymous function.
    # It can take any number of arguments, but can only have one expression.
    # It is defined using the lambda keyword.
    # It is not assigned to a variable.
    # It can be used wherever function is required.

z=lambda x:x**2
print(z(8))

# map function
    # The map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.
    # The map() function is a built-in Python function that takes two arguments: a function and an iterable.
cal=map(lambda x:x**2,[1,2,3,4])
print(list(cal))
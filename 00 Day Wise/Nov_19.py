# *args and **kwargs 
    # *args - Allows a function to accept any number of arguments, including none.
    # The arguments are packed into a tuple.
    # **kwargs - Allows a function to accept any number of keyword arguments, including none.
    # The arguments are packed into a dictionary.

def add(*num):
    total = 0
    for n in num:
        total += n
    return total
print(add(1, 2, 3, 4, 5))

def demo1(a, *args):
    print(a)
    print(type(a))
    print(args)
    print(type(args))
demo1(1, 2, 3, 4, 5)

def demo(**him):
    for k,v in him.items():
        print(f"{k} = {v}")

demo(name="Himanshu", age=26, city="Pune")

def demo2(x,y,**kwargs):
    print(f"{x} = {y}")
    for k,v in kwargs.items():
        print(f"{k} = {v}")
    
demo2(1, 2, z=3, w=4)

def xyz(*args, **kwargs):
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

xyz(1, 2, 3, name="Himanshu", age=26)
xyz(1, 2)
xyz(name="Himanshu", age=26)

# OOPs is programming prardime that organzie s/w around data or object rather then function.
# It is based on the classes which are blueprints of creating objects.

# Class is a blue print or a template of an object. it defines the properties and behavior.

# Object is an instance of class. it has its own state(vales of attributes and behavior).

#Method: They operate on the object data.
# Function: Standalone function that can be used anywhere in the program

# Magic and Dunder method
# Dunder method are special methods that start and end with double underscore.they are used it defines specific behavior for objects such as string representation, arithmetic operations, etc.


# The benifits of constructor :-
# A constructor is special method that initializes the object's properties when an  object are created state.
# eg- __init__,

# the concept of self.
# the self keyword that refers to the current  instance of the class. it is used object's attribute and functions with in the class.

class ABC:
    def f1(self):
        print("Hello from f1")
    def f2(self):
        print("Hello from f2")

obj = ABC()
obj.f1()

class Rectangle:
    def __init__(self, l, b):
        self.l=l
        self.b=b
    def area(self):
        print(f"Area of rectangle :{self.l * self.b}")
    def perimeter(self):
        print(f"Perimeter of rectangle :{2 * (self.l + self.b)}")
    
rect = Rectangle(5, 8)
rect.area()
rect.perimeter()



# Polymorphism:-
# types of polymorphism
# 1. overloading
    # methods with same name but different parameters are allowed
class abc:
    def F1(self):
        print("Hello from F1")
    def F1(self):
        print("Hello from F2")
    def F1(self):
        print("Hello from F3")

obj = abc()
obj.F1()    

class Student:
    '''This is Student class with required data'''

print(Student.__doc__)
help(Student)

# 1. overloading
    # methods with same name but different parameters are allowed
class abc:
    def F1(self, a):
        print(f"Hello from F1 with {a}")
    def F1(self, a, b):
        print(f"Hello from F1 with {a} and {b}")
    def F1(self, a, b, c):
        print(f"Hello from F1 with {a}, {b} and {c}")

# obj = abc()
# obj.F1(10)
# obj.F1(10, 20)
# obj.F1(10, 20, 30)

# 2. overriding
    # method with same name and parameters in parent class and child class are allowed
class Parent:
    def F1(self):
        print("Hello from Parent")

class Child(Parent):
    def F1(self):
        super().F1()
        print("Hello from Child")
    
# obj1 = Parent()
# obj1.F1()
obj2 = Child()
obj2.F1()
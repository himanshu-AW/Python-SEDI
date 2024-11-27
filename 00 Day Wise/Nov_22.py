# Question1: Define a class-name Shape and its sub class square . the square class has init function which takes a length as argument. both classes have an area function which can print the area of shape. where shape area is Zero  by default.

class Shape:
    def __init__(self):
        pass
    def area(self):
        return f"Area of Shape: {0}"

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return f"Area of Square: {self.length*self.length}"

# square = Square(5)
# print(square.area())

# Math, random, calinder, datetime
# Encapsulation: it is a teachnique of bundling data(attributes) and methods that operate on that data within a single unit(or class). This encapsulation hides the implementation details from the outside world making the code module reusable and easy to maintain.

# public access modifier
class Car:
    def __init__(self, model, speed):
        self.model = model
        self.speed =speed
    def accelerate_car(self, speed):
        print(f"Accelerating the car to {speed} km/h")
    def F1(self):
        print("Public F1 method")

# c = Car(2024,40)
# print(c.model)
# c.F1()

# protected access modifier
class Car1:
    def __init__(self, model, speed):
        self._model = model
        self._speed =speed
    def accelerate_car(self, speed):
        print(f"Accelerating the car to {speed} km/h")
    def _F1(self):
        print("Protected F1 method")

# c1 = Car1(2024,40)
# print(c1.model)
# c1._F1()
# c1.F1()


# Private access modifier
class Car2:
    def __init__(self, model, speed):
        self.__model = model
        self.__speed =speed
    def accelerate_car(self, speed):
        print(f"Accelerating the car to {speed} km/h")
    def __F1(self):
        print("Private F1 method")

# c2 = Car2(2024,40)
# print(c2.model)
# c2.F1()
# c2._Car2__F1()


# Qurstion: B is a sub class of A. to invoke the init method in A from B. What is the line of code you sholud write.
class A:
    def __init__(self):
        print("executed from class A")
class B(A):
    def __init__(self):
        # super().__init__()
        A.__init__(self)
        # print("executed from class B")

# b = B()


# Abstraction 
from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def color(self):
        pass
    @abstractmethod
    def model(self):
        pass
    @abstractmethod
    def accelerate(self):
        print("Your car is accelerating.")

class Honda_City(Car):
    def color(slef):
        print("Honda city of White color.")
    def model(slef):
        print("Model : November 2024 ")
    def accelerate(self):
        return super().accelerate()
    def isAutomatic(slef,automatic=False):
        if(automatic):
            print("Honda City Car is Automatic")
        else:
            print("Honda City Car is Manual")
    
hc = Honda_City()
hc.color()
hc.model()
hc.accelerate()
hc.isAutomatic(True)

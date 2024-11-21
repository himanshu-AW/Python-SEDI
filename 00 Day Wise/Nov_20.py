# To understand the concept of polymorphism  in oops. polymorphism is fundamental of oops that allows objects of diffeent classes to be treated object of a super class. 
# In programming polymorphism allows a single function/methos or to work to different ways depending upon thype of object.
# Polymorphism provides provides flexibility and ability to define methods in the base class which can be overridder in drive class.

# Overloading / Compile time polymorphism AND Overriding / run-time polymorphism / dynamic polymorphism

# Inheritence: it's one of the fundamental priencipal of oops. it allows a new class(sub-class/child-class) to inherites the properties and behavious from exitsing class(parent / super class). it helps to reuse the code making the system and easy to maintain.

print("--------Single Inheritence--------")
class Parent:
    def F1(self):
        print("this is f1 from parent")

class Child(Parent):
    def F2(self):
        print("this is f2 from child")

# p = Parent()
# p.F1()

c = Child()
c.F1()
c.F2()

print("---------Multilevel interface----------")
class GrandChild(Child):
    def F3(self):
        print("this is f3 from grandchild")
    
g = GrandChild()
g.F1()
g.F2()
g.F3()

print("--------Multiple Inheritence--------")
class Parent1:
    def F1(self):
        print("this is f1 from Parent1")

class Parent2:
    def F2(self):
        print("this is f2 from Parent2")

class Child(Parent1, Parent2):
    def F3(self):
        print("this is f3 from Child")

child = Child()
child.F1()
child.F2()
child.F3()

print("--------Hierarchy Inheritance--------")
class Parent:
    def F1(self):
        print("this is f1 from Parent")
    
class Child1(Parent):
    def F2(self):
        print("this is f2 from Child1")

class Child2(Parent):
    def F3(self):
        print("this is f3 from Child2")
    
child1 = Child1()
child1.F1()
child1.F2()

child2 = Child2()
child2.F1()
child2.F3()

print("--------Hybrid Inheritance--------")
class Parent:
    def F1(self):
        print("this is f1 from parent")
class Child2(Parent):
    def F2(self):
        print("this is f2 from child2")
class Child2(Parent):
    def F3(self):
        print("this is f3 from child2")
class commonGrandChild(Child1,Child2):
    def F4(self):
        print("this is f4 from common grandchild")

d = commonGrandChild()
d.F1()
d.F2()
d.F3()
d.F4()
'''
a=10
b="rd"
c=str
c=str(a)
d=b+c
print(d)
print(id(a))
print(id(c))
print(type(a))
print(type(c))

a="123"
b=int(a)
print(type(b))'''



#Python Arithmetic operators
#Addtion
a=10
b=3
print(a+b)
#Subtraction
print(a-b)
#Multiplication
print(a*b)
#Division with float value - floor value
print(a/b)
#Division with integer part
print(a//b)
#power
print(a**b)
#modulas or reminder
print(a%b)


#logical operator
print((a==10)and(b==2))
print((a==10)and(b!=2))

#identity operator
c=a
print(id(a))
print(id(b))
print(id(c))
print(a is c)
print(a is b)

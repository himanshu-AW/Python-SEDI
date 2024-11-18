# split- break a string into a list of sub-strings based on specify delimiter.
print("Hello world".split())

# strip- Remove leading and trailing white space
print("      Hello world!     ".strip())
print("********Hello world!******".strip("*"))

# Join- makes a string from  list of strings
print("-".join(["Hello","world","!"]))

# replace- takes 2 argunment 
    # 1st argument is old value
    # 2nd argument is new value
print("Hello world!".replace("world","RD"))

# find- find the index of the first sequence of characters
print("Hello world".find("world"))


# Difference between list and Array
import numpy as np
x= np.array([1,2,3,4,5])
print(x)
print(type(x)) #<class 'numpy.ndarray'> nd:N-dimensional array

lst=["Rd",35,280,False]
print(lst)
print(type(lst))

#List:- most versatile data structure in python. used to store collection of items. they are ordered and mutable-meaning:yoy can change their order and elements
# How list store in memory ?
# List are stored in contiguous memory locations. Each element in the list has its own memory address and list object stores the address of 1st elements and the length of list.

lst=[1,2,3.9999,5,6,"Kuldeep","Oxford",True]
# Accessing elements of list
print(lst[0])
print(lst[-1])
print(lst[2:5])
print(lst[:5])
print(lst[2:])

# append method- it will add a new element in the last of the list
lst.append(99)
print(lst)
# extend method- it will add a new list in the last of the list
lst.extend([100,101,102])
print(lst)
# insert method- it will add a new element at the specified index
lst.insert(2,"Kanika")
print(lst)
# replace with slicing
lst[2]="New"
print(lst)
lst[2:5]=["New","Value"]
print(lst)
lst[1:2]="Poker"
print(lst)

# pop- it remove the last element in the list
lst.pop()
print(lst)
lst.pop(2)
print(lst)

# reomve- it remove the 1st occurance of the specific element
lst.remove(1)
print(lst)

# delete- it will delete all elements
# del lst
# print(lst)

# sorting of list
lst=[1,2,8,3,9,4]
lst.sort(reverse=False)
print(lst)

for i in lst:
    print(i,end=" ")
print()

i=0
while i<len(lst):
    c=lst[i]
    print(c,end=" ")
    i+=1
print()

# combine elements from multiple iterable into tuple
l1=[1,2,3,4]
l2=["A", "B", "C",]
c=list(zip(l1,l2))
print(c)


# Ques-1: Given a list of number find the sum and product of all element.
lst=[1,2,3,4,5,6,7,8,9,10]
sum=0
product=1
for i in lst:
    sum+=i
    product*=i
print(f"Sum of all elements: {sum}")
print(f"Product of all elements: {product}")

#Ques-2: Given a list of string print only vowel of string
lst=["Kuldeep","Ansu","Sharuf","Mansih"]
vowel=['a','i','o','u','e']

for word in lst:
    for char in word:
        if char.lower() in vowel:
            print(char,end=" ")
    print()


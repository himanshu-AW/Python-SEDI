# Dictonary:
dic={}
print(type(dic))
# x=dict()
# print(type(x))

dic={'a':1, 'b':2, 'c':3, 'd':4}
print(dic)

# accessing of value
print(dic['a'])
print(dic['c'])

# assing values to dictionary 
dic['a'] = 10
print(dict)

# for deleting a value from the dictionary.
del dic['d']

# check a key is exits or not
if 'A' in dic:
    print("it exits")
else:
    print("it doesn't exits")

# length of dictionary
print(len(dic))

print(dic.keys())
print(dic.items())
a,b,c=dic.items()
print(a,b,c)
print(type(a))

print(dic.get('A'))
print(dic.get('A',"not exits"))
print(dic.get('b'))

# pop: to remove elements from dict by indexing 
print(dic.pop('c'))
# print(dic.pop('A'))

# update: All items present in the dictionary x will be added to dictionary d
dic.update({'d':11,'e':12})
print(dic)

# clear : it removes all values from the dictionary
# dic.clear()
# print(dic)

# print dictionary
for key in dic.keys():
    print(f"Key:{key} , Value:{dic[key]}")

d2={'s':100,'t':200}
d3=dict(zip(dic.keys(),d2.values()))
print(d3)

# d3={'':{'a':10,'b':20},{'c':30,'d':40}}
# print(d3)

# x={}
# for i in range(3):
#     temp={}
#     for key in range(i+1,3+i+1):
#         temp[key]=key*key
#     x[i]=temp
# print(x)

# x={x:{y:x*y for y in range(1,3)} for x in range(1,3)}
# print(x)




print("-----------set-------------------")
s=set()
print(type(s))

# sets are unordered and do not allow duplicates elements. so you can't edit it.
s={1,2,3,4,5}
print(s)

# add element
s.add(6)
print(s)

# remove element by .remove() method or .discard() method
s.remove(6)
print(s)
# s.remove(0)

s.discard(4)
print(s)

# union of 2 sets
s1={1,2,3}
s2={2,3,4,5}
print(s1.union(s2))
print(s1 | s2)

# intersection of 2 sets
print(s1.intersection(s2))
print(s1 & s2)

# difference of 2 sets
print(s1.difference(s2))
print(s2.difference(s1))
print(s1-s2)
print(s2-s1)

# symmetric difference of 2 sets
print(s1.symmetric_difference(s2))
print(s1 ^ s2)

# len(), clear(), copy()
s3=s1.copy()
print(id(s1))
print(id(s3))

s1={1,2}
s2={1,2,3,4}
print(s1.issubset(s2))

print(s1.issuperset(s2))
print(s2.issuperset(s2))

print("-------------tuple-------------")
# tuple is immutable and ordered.
x=(1)
print(type(x))
x=(1,)
print(type(x))
y=(1,2,3)
print(type(y))
z=tuple()
print(type(z))

# concatenation

x=(1,2,3)
y=(4,5,6)
print(x+y)

# slicing
print(x[1])
print(x[-1])

# len(), count(), index(), iterable

# tuple packing and unpacking
a,b,c=10,20,30
print(a,b,c)
tup=a,b,c
print(tup)

a,b,c=tup
print(a,b,c)
print("\n-------------Pass--------------------")
# Pass statement act as a placeholder and do nothing.
# often used to create code blocks where syntex require statement but no action needed.
# Pass statement we can use anywhere in code blocks.
for i in range(10):
    if i <= 5:
        pass
    else:
        print(i)

print("\n-------------continue--------------------")
# Skips the cuurent iterartion of the loop and moves on to the next one.
# Usefull for skipping certain iteration based on condition.
for i in range(10):
    if i == 5:
        continue
    else:
        print(i)

print("\n-------------Break--------------------")
# Break immeditaly terminate the loops regardless iteration is remaining.
# Often used to prematurialy of a certain condition is ture.
# Break only used in loops
for i in range(10):
    if i == 5:
        break
    else:
        print(i)

# true=False
# while true:
#     print(true)
#     break

print("\n------------String -------------------")
# String is a sequence of characters enclosed in single quotes, double quotes or triple quotes.
# String is immutable in nature.
s="Sharuf Ali"
print(s)

print("\n-------------String Concatenation--------------------")
# combination of strings.
s2=12
# print(s+s2)
print(s+str(s2))
#
print("\n----------Repeatation---------")
# repetation of string
print("Hello "*5)

print("\n-------Indexing-----------")
# Indexing in Python starts from 0.
s="Sharuf Ali"
print(s[0])
print(s[5])

print("\n-------Slicing-----------")
print(s[0])
print(s[-1])
print(s[1:3])
print(s[:3])
print(s[2:])
print(s[:])
print(s[::1])
print(s[::-1])
print(s[::2])


# Removing complete string using the del keyword
print("\n-------Deleting String-----------")
s="Sharuf Ali"
del s
# print(s)

print("\n-------len() function-----------")
# len() return length of the String
s="Sharuf Ali"
print(len(s))

print("\n-------Membership operator-----------")
# in , not in
print('r' in s)
print('r' not in s)


print("\n----Common string function---")
# len,split,join,find,replace,upper, lower,strip
s=input("Enter Some String:")   
i=0   
print(s.strip())
for x in s:   
    print("The character present at positive index {} and at nEgative index {}  is {}".format(i,i-len(s),x))   
    i=i+1   
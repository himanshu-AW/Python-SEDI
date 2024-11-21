# Question 8- Write a program if you are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
# e.g : 'this is a string' output should be like ''this' 'is' 'a' 'string''

strr = input("Enter a string: ")
# words = strr.split(" ")
print("-".join(strr.split(" ")))

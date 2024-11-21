# Question 11- Write a program to arrange string characters into lowercase letters.
# e.g :
# input : str1 = PyThon
# output : python

str = "TasAUvaR"
new_str=""
for char in str:
    if 65 <= ord(char) <= 90:
       new_str += chr(ord(char)+32)
    else:
        new_str += char
print(f"New lower string: {new_str}")
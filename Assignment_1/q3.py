# Question 3- Write a program to check given string is present in user input.
# S = "I love python Programming"

user_input = "Hii, this is Himanshu.i love PYTHON programming!!"
s = "I love python Programming"
if s.lower() in user_input.lower():
    print("The string is present.")
else:
    print("The string is not present.")
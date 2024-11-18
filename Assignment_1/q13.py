# Question 13- Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

fname =input("Enter your first: ")
lname = input("Enter your last: ")
reverse_of_full_name = lname[::-1]+" "+fname[::-1]
print(f"Your full name in reverse order: {reverse_of_full_name}")
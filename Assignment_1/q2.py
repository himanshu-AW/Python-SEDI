# Question 1- Write a program to input three numbers and swap them as this:
# First number becomes second number, second number becomes third number, and third number becomes the first number

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))
print(f"num1:{num1},num2:{num2},num3:{num3}")
num2,num3,num1=num1,num2,num3
print(f"num1:{num1},num2:{num2},num3:{num3}")
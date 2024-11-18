# Question 2- Write a program to input three numbers and swap them as this:
# 1st number gets the value of 1st+2nd
# 2nd number gets the value of 1st+3rd
# 3rd number gets the value of 3rd+2nd

num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))
print(f"num1:{num1},num2:{num2},num3:{num3}")
num1,num2,num3=num1+num2,num1+num3,num3+num2
print(f"num1:{num1},num2:{num2},num3:{num3}")
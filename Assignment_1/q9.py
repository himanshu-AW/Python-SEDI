# Question 9- Write a program to calculate the area of triangle using Heron's Formula where a, b, c are the sides of the triangle.
# Hint :- s=(a+b+c)/2 and Area = sqrt( s(s-a)(s-b)(s-c) )

import math

a = float(input("Enter 1st side of triangle: "))
b = float(input("Enter 2nd side of triangle: "))
c = float(input("Enter 3rd side of triangle: "))
if a+b>=c and b+c>=a and a+c>=b:
    s =(a + b + c) // 2
    area_of_triangle = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"Area of triangle: {round(area_of_triangle,)} ")
else:
    print('Please,Enter valid side of triangle!!')
# Question 14- Write a program to given a three-digit integer (i.e. an integer from 100 to 999). Find the sum of its digits and print the result.
# e.g : Input : 476
# Output : 17

three_digit_num=int(input("Enter the three digit: "))
sum_of_digits=0
while three_digit_num>0:
    sum_of_digits+=three_digit_num%10
    three_digit_num=three_digit_num//10
print(f"Sum of digits: {sum_of_digits}")

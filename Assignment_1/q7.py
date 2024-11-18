# Question 7- Given a string s ="12345" . Can you write an expression that gives sum of all the digits shown inside the string s
# i.e : the program should be able to produce the result as 15 ( 1+2+3+4+5 )
# 'HINT : use indexes and convert to integer'

s = "12345"
sum_of_digits = sum(int(digit) for digit in s)
print(sum_of_digits) 

# or
# sum_of_digits = 0
# for digit in s:
#     sum_of_digits += int(digit)
# print(sum_of_digits)
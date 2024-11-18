# Questions 5- Write a program to calculate compound interest .
# a = p * (pow((1 + r / 100), t))
# CI = a - p
# A = Amount
# P = initial principal balance
# r = interest rate
# t = number of time periods elapsed

principal = int(input("Enter the principal balance: "))
interest_rate = float(input("Enter the interest rate: "))
time_periods = int(input("Enter the time periods: "))

amount = principal * (pow((1+interest_rate/100),time_periods))
compound_interest = round((amount - principal),2)
print(f"Compound Interest: {compound_interest}")
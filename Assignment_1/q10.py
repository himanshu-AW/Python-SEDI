# Question 10- Write a program given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1.
# e.g :
# inputs : s1 = "Ault" s2 = "Kelly"
# ouput : AuKellylt

s1='Ault'
s2='Kelly'
new_str=s1[:len(s1)//2]+s2+s1[len(s1)//2:]
print(f"New string: {new_str}")
print("\n# sum of digits")
sum=0
for i in range(1,10+1):
    sum +=i
print(sum)

print("\n# print table")
num=5
for i in range(1,11):
    print(f"{i}x{num}={i*5}")

print("\n# WAP to check that Num is even or odd")
num=5
if(num==0):
    print("Neither even or nor odd.")
elif(num%2==0):
    print(f"{num} Even number")
else:
    print(f"{num} Odd number")

print("\n# WAP which print all divisor of a numbers")
num=12
for i in range(1,num+1):
    if(num%i==0):
        print(i)

print("\n WAP to check whether the input number is prime or not.")
num=17
flag=True
for i in range(2,num//2):
    if(num%i==0):
        flag=False
        break
if(flag):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

print("\n#WAP to take input of a number 1 to 100 then if the number is multiple of 3 print 'Fizz' if the mutiple of 5 print 'Buzz' if both the condition is true the print 'Fizz and Buzz'")
# num=int(input("Enter a number of range 1 to 100: "))
num=55
if(num%3==0 and num%5==0):
    print("Fizz and Buzz!!")
elif(num%3==0):
    print("Buzz!!")
elif(num%5==0):
    print("Buzz!")


print("\n# WAP to print b/w 100 and 200 are divisible by 7 but not 5.")
for i in range(100,201):
    if(i%7==0 and i%5!=0):
        print(i,end=" ")

print("\n# WAP that accept a word fromthe user and reverse it.")
word="Kuldeep"
temp=word[::]
print(temp)

print("\n#WAP that accept a string and calculate digits and letter")
# strr = input("Enter a alpha_numberic string: ")
strr="k1u2l3d4e5e6p7"
number=["1","2","3","4","5","6","7","8","9","0"]
c_num=0
c_str=0
for i in strr:
    if(i in number):
        c_num+=1
    else:
        c_str+=1
print(f"Number of Alphabetic characters in {strr} : {c_str}")
print(f"Number of Digit characters in {strr} : {c_num}")


print("\n#WAP to find median of three value")
# num1=int(input("Enter 1st number: "))
# num2=int(input("Enter 3st number: "))
# num3=int(input("Enter 3st number: "))
num1=14
num2=53
num3=6
print((num1+num2+num3)/3)

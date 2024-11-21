class Calculator:

    def __init__(self,result=0):
        self.__result = result

    # addition method
    def addition(self, num):
        self.__result+=num
        return self.__result
    def subtract(self,num):
        self.__result-=num
        return self.__result
    def product(self,num):
        self.__result*=num
        return self.__result
    def division(self,num):
        self.__result/=num
        return self.__result
    
print("*************** Calculator ****************")
print("Note: Valid arithmetic operators are: + , - , * , / ")
# option = input("Enter operation: ")
# num1 = float(input("Enter number: "))
# calc = Calculator(num1)

calc = Calculator()

expression = input()
operator = ["+","-","*","/"]
result=0
for i in expression:
    if i in operator:
        result = 


# while True:
#     option = input("Enter operation: ")
#     # option = input()
#     match option: 
#         case "+":
#             num = float(input("Enter number: "))
#             result = calc.addition(num)
#             print(f"Result : {result}")
#         case "-":
#             num = float(input("Enter number: "))
#             result = calc.subtract(num)
#             print(f"Result : {result}")
#         case "*":
#             num = float(input("Enter number: "))
#             result = calc.product(num)
#             print(f"Result : {result}")
#         case "/":
#             num = float(input("Enter number: "))
#             result = calc.division(num)
#             print(f"Result : {result}")
#         case _:
#             print("Please enter valid arithmetic operator.")
#             exit()



    # choice = input("Do you want to continue??( Y / N )")
    # if choice.lower() == "n":
    #     exit()




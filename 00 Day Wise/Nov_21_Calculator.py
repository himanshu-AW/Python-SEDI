import os
import math

class Calculator:
    def __init__(self, result=0):
        self.__result = result
        self.__memory = 0
        self.__history = []

    # Basic operations
    def addition(self, num):
        self.__result += num
        self.__add_to_history(f"{self.__result - num} + {num} = {self.__result}")
        return self.__result

    def subtract(self, num):
        self.__result -= num
        self.__add_to_history(f"{self.__result + num} - {num} = {self.__result}")
        return self.__result

    def product(self, num):
        self.__result *= num
        self.__add_to_history(f"{self.__result / num} * {num} = {self.__result}")
        return self.__result

    def division(self, num):
        if num == 0:
            raise ValueError("Division by zero is not allowed!")
        self.__result /= num
        self.__add_to_history(f"{self.__result * num} / {num} = {self.__result}")
        return self.__result

    # Additional functionality
    def square_root(self):
        if self.__result < 0:
            raise ValueError("Cannot calculate the square root of a negative number!")
        prev_result = self.__result
        self.__result = math.sqrt(self.__result)
        self.__add_to_history(f"√{prev_result} = {self.__result}")
        return self.__result

    def power(self, exponent):
        prev_result = self.__result
        self.__result **= exponent
        self.__add_to_history(f"{prev_result} ^ {exponent} = {self.__result}")
        return self.__result

    def store_memory(self):
        self.__memory = self.__result
        return self.__memory

    def retrieve_memory(self):
        return self.__memory

    def clear_result(self, value=0):
        self.__result = value
        self.__add_to_history(f"Result cleared to {value}")
        return self.__result

    def get_history(self):
        return "\n".join(self.__history) if self.__history else "No history available."

    def __add_to_history(self, operation):
        self.__history.append(operation)

    # Getter for current result
    def get_result(self):
        return self.__result


# Main Program
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("*************** Calculator ****************")
    print("Type 'help' for the list of commands.")
    num1 = float(input("Enter initial number: "))
    calc = Calculator(num1)

    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"Current Result: {calc.get_result()}")
            option = input("Enter operation (or type 'help'/'quit'): ").strip()

            if option.lower() == "help":
                print("""
                        Valid operations:
                        +  : Addition
                        -  : Subtraction
                        *  : Multiplication
                        /  : Division
                        sqrt : Square root
                        ^  : Power
                        mem  : Store current result in memory
                        rec  : Retrieve value from memory
                        clr  : Clear result
                        hist : View operation history
                        quit : Exit the calculator
                    """)
                input("Press Enter to continue...")
                continue

            if option.lower() == "quit":
                confirm = input("Are you sure you want to quit? (y/n): ").strip().lower()
                if confirm == "y":
                    print("Goodbye!")
                    break
                else:
                    continue

            if option.lower() == "mem":
                memory = calc.store_memory()
                print(f"Stored {memory} in memory.")
                input("Press Enter to continue...")
                continue

            if option.lower() == "rec":
                memory = calc.retrieve_memory()
                print(f"Retrieved {memory} from memory.")
                input("Press Enter to continue...")
                continue

            if option.lower() == "clr":
                value = input("Enter value to reset result to (default is 0): ").strip()
                value = float(value) if value else 0
                result = calc.clear_result(value)
                print(f"Result reset to {result}.")
                input("Press Enter to continue...")
                continue

            if option.lower() == "hist":
                print("History:")
                print(calc.get_history())
                input("Press Enter to continue...")
                continue

            if option.lower() == "sqrt":
                result = calc.square_root()
                print(f"Square Root Result: {result}")
                input("Press Enter to continue...")
                continue

            if option.lower() == "^":
                exponent = float(input("Enter exponent: "))
                result = calc.power(exponent)
                print(f"Exponentiation Result: {result}")
                input("Press Enter to continue...")
                continue

            # Basic arithmetic operations
            if option in ["+", "-", "*", "/"]:
                num = float(input("Enter number: "))
                if option == "+":
                    result = calc.addition(num)
                elif option == "-":
                    result = calc.subtract(num)
                elif option == "*":
                    result = calc.product(num)
                elif option == "/":
                    result = calc.division(num)
                print(f"Result: {result}")
                input("Press Enter to continue...")
                continue

            print("Invalid operation! Type 'help' for the list of commands.")
            input("Press Enter to continue...")

        except ValueError as e:
            print(f"Error: {e}")
            input("Press Enter to continue...")
        except Exception as e:
            print(f"Unexpected error: {e}")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()

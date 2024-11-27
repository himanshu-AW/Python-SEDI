import time
import os
from datetime import datetime

class ATM:
    def __init__(self):
        self.__attempt = 0
        self.__user_data = [
            {"name": "Ram", "PIN": "1234", "balance": 200000, "isSaving": True},
            {"name": "Shyam", "PIN": "1122", "balance": 30000, "isSaving": False},
            {"name": "Rohan", "PIN": "3344", "balance": 240000, "isSaving": False},
            {"name": "Tarun", "PIN": "9988", "balance": 500000, "isSaving": True},
            {"name": "Karan", "PIN": "0012", "balance": 400000, "isSaving": False}
        ]
        self.__current_user = None

    def __clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def __greet_user(self):
        hour = datetime.now().hour
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 17:
            greeting = "Good afternoon"
        elif 17 <= hour < 21:
            greeting = "Good evening"
        else:
            greeting = "Good night"
        print(f"\n{greeting}, {self.__current_user['name']}!")

    def __display_menu(self):
        self.__clear_screen()
        print("\n****** Welcome to Ambuja Foundation *******")
        print("Please choose an option:")
        print("1. Current Account")
        print("2. Savings Account")
        print("3. Generate New PIN")
        print("4. Change PIN")
        print("5. Exit")

    def __account_options(self):
        while True:
            self.__clear_screen()
            self.__greet_user()
            account_type = "Savings Account" if self.__current_user["isSaving"] else "Current Account"
            print(f"\nAccount Type: {account_type}")
            print("Select an option:")
            print("1. Withdraw")
            print("2. Balance Enquiry")
            print("3. Deposit")
            print("4. Exit")
            option = input("Enter your option: ")
            match option:
                case "1":
                    self.__withdraw()
                case "2":
                    self.__balance_enquiry()
                case "3":
                    self.__deposit()
                case "4":
                    print("Thank you for banking with us.")
                    break
                case _:
                    print("Invalid choice. Please try again.")
                    time.sleep(2)

    def __check_PIN(self, user_pin, account_type):
        for user in self.__user_data:
            if user["PIN"] == user_pin and (
                (account_type == "1" and not user["isSaving"]) or
                (account_type == "2" and user["isSaving"])
            ):
                self.__current_user = user
                return True
        return False

    def __account(self, account_type):
        while True:
            PIN = input("Enter your 4-digit PIN: ")
            if len(PIN) != 4 or not PIN.isdigit():
                self.__attempt += 1
                if self.__attempt >= 3:
                    print("Too many invalid attempts. Try again after 5 minutes.")
                    time.sleep(10)
                    self.__attempt = 0
                    self.__clear_screen()
                else:
                    print("Invalid PIN. Please try again.")
            elif self.__check_PIN(PIN, account_type):
                return True
            else:
                print("Incorrect PIN or account type mismatch. Please try again.")
                self.__attempt += 1

    def __withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount % 500 == 0 and amount <= self.__current_user["balance"]:
            print("Transaction processing...")
            time.sleep(2)
            self.__current_user["balance"] -= amount
            print(f"Please collect your cash. Updated balance: ₹{self.__current_user['balance']:.2f}")
        else:
            print("Invalid amount or insufficient balance.")
        time.sleep(2)

    def __balance_enquiry(self):
        print(f"Your current balance is: ₹{self.__current_user['balance']:.2f}")
        time.sleep(8)

    def __deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.__current_user["balance"] += amount
        print(f"Deposit successful. Updated balance: ₹{self.__current_user['balance']:.2f}")
        time.sleep(2)

    def __generate_pin(self):
        name = input("Enter your name: ")
        new_pin = input("Set a new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__user_data.append({"name": name, "PIN": new_pin, "balance": 0, "isSaving": True})
            print("Account created successfully.")
        else:
            print("Invalid PIN. Must be 4 digits.")
        time.sleep(2)

    def __change_pin(self):
        old_pin = input("Enter your current PIN: ")
        if self.__check_PIN(old_pin, "1") or self.__check_PIN(old_pin, "2"):
            new_pin = input("Enter your new 4-digit PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                self.__current_user["PIN"] = new_pin
                print("PIN changed successfully.")
            else:
                print("Invalid PIN. Must be 4 digits.")
        else:
            print("Incorrect current PIN.")
        time.sleep(2)

    def start(self):
        while True:
            self.__display_menu()
            choice = input("Enter your choice: ")
            match choice:
                case "1" | "2":
                    if self.__account(choice):
                        self.__account_options()
                case "3":
                    self.__generate_pin()
                case "4":
                    self.__change_pin()
                case "5":
                    print("Thank you for using Ambuja Foundation ATM.")
                    break
                case _:
                    print("Invalid choice. Please try again.")
                    time.sleep(2)


# main program
atm = ATM()
atm.start()



# generate pin
# change pin
#pin validation and account validation
#wishing to the user with its name

# hum aasa bhi kar sakte h:
# ek list of dictionary create user:PIN for validation. agar pin match karta to age ki process ka access dege. warna nhi access dege
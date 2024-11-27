import os
from random import choice

def stone_paper_scissors():
    # Clear screen for Windows/Linux compatibility
    os.system("cls" if os.name == "nt" else "clear")  
    choice_list = ["Stone", "Paper", "Scissors"]
    computer_choice = choice(choice_list)

    print("******** Welcome to Stone, Paper, Scissors! *********")
    print("1: Stone")
    print("2: Paper")
    print("3: Scissors")

    try:
        user_input = int(input("Enter your choice (1/2/3): "))
        if user_input not in [1, 2, 3]:
            print("Invalid choice! Please select 1, 2, or 3.")
            return
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    user_choice = choice_list[user_input - 1]

    print(f"You chose: {user_choice}, Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("Tie game! Please try again.")
    elif (user_choice == "Stone" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Stone") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        print("---------- Congratulations! You win! ------------")
    else:
        print("---------- You lose! Better luck next time. ---------")

while True:
    stone_paper_scissors()
    try:
        run_again_choice = int(input("Do you want to play again?\nPress 0 to play again or any other key to exit: "))
        if run_again_choice != 0:
            print("Thank you for playing!")
            break
    except ValueError:
        print("Exiting the game. Thank you for playing!")
        break

import random
def Rock_paper_scissors():
    choices = ["rock","paper","scissors"]
    print("Welcome to rock paper scissors game!")
    print("Available choices: rock, paper, scissors")
    user_choice = input("Enter your choice: ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter rock, paper, scissors: ").lower()

    computer_choice = random.choice(choices)
    print(f"Computer choice {computer_choice}")
    if user_choice == computer_choice:
        print("It's tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or\
    (user_choice == "scissors" and computer_choice == "paper"):
        print("User Wins!")
    else:
        print("Computer wins!")

Rock_paper_scissors()












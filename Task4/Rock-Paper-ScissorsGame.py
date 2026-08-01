import random

OPTIONS = ["rock", "paper", "scissors"]


def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in OPTIONS:
            return choice
        print("Invalid choice. Please enter rock, paper, or scissors.")


def get_computer_choice():
    return random.choice(OPTIONS)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }
    if wins[user_choice] == computer_choice:
        return "user"
    return "computer"


def main():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("Welcome to Rock-Paper-Scissors!")
    print("Enter rock, paper, or scissors. Type q or quit to stop.")

    while True:
        print(f"\nRound {round_number}")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        if result == "tie":
            print("It's a tie!")
        elif result == "user":
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round.")
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        again = input("Play again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            break
        round_number += 1

    print("\nThanks for playing!")
    print(f"Final score: You {user_score} - {computer_score} Computer")


if __name__ == "__main__":
    main()

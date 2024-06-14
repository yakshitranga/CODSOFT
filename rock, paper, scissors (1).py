import random
def get_user_choice():
#Prompt the user to choose rock, paper, or scissors.
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
#Generate a random choice for the computer.
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
#Determine the winner based on the choices.
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        
# Update scores
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"\nFinal scores: You: {user_score} - Computer: {computer_score}")
            break

if __name__ == "__main__":
    main()

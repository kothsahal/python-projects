
import random

player_score = 0
computer_score = 0

def play_game():
    global player_score, computer_score

    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)

    player = input("\nEnter rock, paper or scissors: ").lower()

    if player not in choices:
        print("Invalid choice! Please try again.")
        return

    print("Computer selected:", computer)

    if player == computer:
        print("It's a Draw!")

    elif player == "rock" and computer == "scissors":
        print("You Win!")
        player_score += 1

    elif player == "paper" and computer == "rock":
        print("You Win!")
        player_score += 1

    elif player == "scissors" and computer == "paper":
        print("You Win!")
        player_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1


print("===== ROCK PAPER SCISSORS GAME =====")

while True:

    play_game()

    print("\nYour Score:", player_score)
    print("Computer Score:", computer_score)

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        break

print("\n===== FINAL RESULT =====")
print("Your Final Score:", player_score)
print("Computer Final Score:", computer_score)

if player_score > computer_score:
    print("Congratulations! You won the game.")

elif computer_score > player_score:
    print("Computer won the game. Better luck next time!")

else:
    print("The game is a tie!")

print("Thanks for playing!")

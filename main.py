import random

class RockPaperScissorsGame:
    def __init__(self):
        self.choices = {'R': 'Rock', 'P': 'Paper', 'S': 'Scissors'}
    
    def generate_choice(self):
        return random.choice(list(self.choices.keys()))

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Tie"
        elif (user_choice == 'R' and computer_choice == 'S') or \
             (user_choice == 'S' and computer_choice == 'P') or \
             (user_choice == 'P' and computer_choice == 'R'):
            return "User"
        else:
            return "Computer"

    def play_game(self):
        while True:
            user_choice = input("Enter R (Rock), P (Paper), or S (Scissors): ").upper()
            if user_choice not in self.choices:
                print("Invalid choice, please try again.")
                continue
            
            computer_choice = self.generate_choice()
            print(f"Your choice: {self.choices[user_choice]}")
            print(f"Computer's choice: {self.choices[computer_choice]}")
            
            result = self.determine_winner(user_choice, computer_choice)
            if result == "Tie":
                print("It's a tie! Try again.")
            elif result == "User":
                print("You win!")
                break
            else:
                print("The computer wins!")
                break

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.play_game()

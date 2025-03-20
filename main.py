import random

def rock_paper_scissors():
   
    choices = ["rock", "paper", "scissors"]
   
    user_score = 0
    computer_score = 0
    
    max_rounds = 5 
    
    print("Welcome to Rock, Paper, Scissors!")
    print(f"This game will run for {max_rounds} rounds.")
    print("Enter 'rock', 'paper', 'scissors' to play, or 'quit' to exit early.")
    
    round_count = 0
    
    while round_count < max_rounds:
        round_count += 1
        print(f"\nRound {round_count} of {max_rounds}")
        
        user_choice = input("Your choice: ").lower()
                
        if user_choice == 'quit':
            print("Game ended early by player.")
            break
        
        
        if user_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            round_count -= 1 
            continue
        
    
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")
        
    
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1
        
    
        print(f"Score - You: {user_score}, Computer: {computer_score}")
    
    
    print("\nGame Over!")
    print(f"Final Score - You: {user_score}, Computer: {computer_score}")
    
    if user_score > computer_score:
        print("Congratulations! You won the game!")
    elif user_score < computer_score:
        print("The computer won the game. Better luck next time!")
    else:
        print("The game ended in a tie!")

if __name__ == "__main__":
    rock_paper_scissors()
import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Choose rock, paper or scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == 'rock' and computer_pick == 'scissors':
        print("You won!")
        user_wins += 1
    elif user_input == 'paper' and computer_pick == 'rock':
        print("You won!")
        user_wins += 1
    elif user_input == 'scissors' and computer_pick == 'paper':
        print("You won!")
        user_wins += 1
    elif user_input == computer_pick:
        print("It's a tie!")
    else:
        print("You lost!")
        computer_wins += 1

    print(f"Score: You {user_wins} - {computer_wins} Computer")

print(f"Final Score: You won {user_wins} times!")
print(f"The computer won {computer_wins} times!")
print("Goodbye!")
import random

user_wins = 0
computer_wins = 0

options = ['fire', 'water', 'earth', 'air', 'lightning', 'ice']

winning_combinations = {
    'fire': ['earth', 'ice'],
    'water': ['fire', 'lightning'],
    'earth': ['water', 'lightning'],
    'air': ['fire', 'earth'],
    'lightning': ['air', 'ice'],
    'ice': ['water', 'air']
}

while True:
    user_input = input("Choose fire, water, earth, air, lightning, or ice (or Q to quit): ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        print("Invalid choice. Please choose a valid option.")
        continue

    computer_pick = random.choice(options)
    print(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        print("It's a tie!")
    elif computer_pick in winning_combinations[user_input]:
        print("You won!")
        user_wins += 1
    else:
        print("You lost!")
        computer_wins += 1

    print(f"Score: You {user_wins} - {computer_wins} Computer")

print(f"Final Score: You won {user_wins} times!")
print(f"The computer won {computer_wins} times!")
print("Goodbye!")

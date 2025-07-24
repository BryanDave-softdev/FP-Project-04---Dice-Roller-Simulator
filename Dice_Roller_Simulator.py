import random

print("🎲 Welcome to the Dice Roller Simulator!")
print("----------------------------------------")

while True:
    input("Press Enter to roll the dice... ")
    dice_result = random.randint(1, 6)
    
    print(f"You rolled a {dice_result}!")

    # Option to roll again or exit
    roll_again = input("Roll again? (y/n): ").lower()
    if roll_again != 'y':
        print("Thanks for playing! Goodbye 👋")
        break

'''
Write a program to simulate a die/dice
die has 6 faces with number 1 to 6 written on them
The program should randomly prints a number between 1 and 6
'''
import random
print("Welcome to the game of rolling a dice.")
while True:
    choice = input('Press "Enter" to roll the dice or "q" to quit.')
    choice = choice.strip()
    
    if (choice == "q"):
        print("Thanks for playing the game, bye!")
        break
    elif choice == "":
        number = random.randint(1, 6)
        print(f"Your number is {number}")
    else:
        print("Invalid input")
        
print("Game Over!!!")
'''
Create a simple number guessing game.
The user gets 10 chances to guess a number.
If  the user guesses the number before 10 chances, stop asking the number from the user, say Congrats and end the game.
If the user never guesses the number, ask them 10 times end the game!!
'''
import random
print("Welcome to the number guessing game. We have a number that needs to be guessed. You have 10 choices.")
print("The secret numbe is between 1 and 50")
print("You have 10 attempts.")
secret_number = random.randint(1, 50)

for attempt in range(1, 11):
    guess = int(input("Enter your guess: "))
    
    if guess < 1 or guess > 50:
        print("Please enter a number: ")
    elif guess == secret_number:
        print("Congrats!! You guessed the number!")
        break
    elif guess < secret_number:
        print("Too Low!!")
    else:
        print("Too high!!")
else:
    print("Game Over!!")
    print(f"The secret number was: {secret_number}")

    

    



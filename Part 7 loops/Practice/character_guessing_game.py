import random
print("Welcome to the character guessing game. We have a character that needs to be guessed. You have 10 choices.")
print("The secret character is between small 'a' to small 'z'")
print("You have 10 attempts.")
secret_character = random.choice("abcdefghijklmnopqrstuvwxyz")

for i in range(1, 11):
    guess = input("Enter a small letter character from a to z: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue
    
    if guess == secret_character:
        print("Congrats!! You guessed the right character!")
        break
    elif ord(guess) < ord(secret_character):
        print("Too Low!")
    
    else:
        print("Too High!")
else:
    print("\nGame Over!")
    print(f"The secret letter was{secret_character}")
    

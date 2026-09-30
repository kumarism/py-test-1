


import random

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("You have 5 attempts to guess the secret number between 1 and 50.")
    
    secret_number = random.randint(1, 50)
    attempts = 5
    
    while attempts > 0:
        guess = int(input("Enter your guess: "))
        
        if guess < secret_number:
            print("Your guess is too low! ❄️")
        elif guess > secret_number:
            print("Your guess is too high! 🔥")
        else:
            print("Congratulations! You've guessed the secret number! 🎉")
            break
        
        attempts -= 1
        print(f"You have {attempts} attempts remaining. ❤️")
    
    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")



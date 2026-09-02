import random

play_again = "yes"

while play_again == "yes":
    guess = None
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 100)
    print("I have selected a number between 1 and 100. Can you guess what it is?")

    while guess != secret_number:
        guess = input("Enter your guess: ")
        attempts += 1
        guess = int(guess)
        if guess == secret_number:
            print("You got it! The number was", secret_number, "and it took you", attempts, "guesses.")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    play_again = input("Do you want to play again? (yes/no): ")

print("Thanks for playing!")
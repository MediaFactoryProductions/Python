import random

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

def play_number_guessing_game():
    min_value = 1
    max_value = 100
    number_to_guess = generate_random_number(min_value, max_value)
    attempts = 0

    print(f"Welcome to the Number Guessing Game! Guess a number between {min_value} and {max_value}.")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if (user_guess == number_to_guess):
            print(f"Awesome job, you guess the number {number_to_guess} in {attempts} attempts.")
            break

        elif (user_guess < number_to_guess):
            print("Try a higher number.")

        else:
            print("Try a lower number")

play_number_guessing_game()

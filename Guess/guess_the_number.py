import random

print("Hi sisters! Welcome to the Number Guessing Game."
      "\nYou have 10 chances to guess the number. "
      "Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 10 chances to guess the number between {low} and {high}. Let's start!")

number = random.randint(low, high)
chances = 10
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    guess = int(input('Enter your guess: '))

    if guess == number:
        print(f'Correct! The number is {number}. You guessed it in {guess_counter} attempts.')
        break

    elif guess_counter >= chances and guess != number:
        print(f'Sorry but you so unlucky the number was {number}')

    elif guess > number:
        print('Too high! Try a lower number.')

    elif guess < number:
        print('Too low! Try a higher number.')

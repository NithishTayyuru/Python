import random
import guess_art
print(guess_art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
level=input("Choose a difficulty.Type 'easy' or 'hard'\n")
if level=="easy":
    attempts=10
elif level=="hard":
    attempts=5
number=random.randint(1,101)
guess=0
while guess!=number and attempts>=0:
    print(f"Attempts left are {attempts}")
    guess=int(input("Enter a number:"))
    if guess>number:
        print("Too high")
    elif guess<number:
        print("Too low")
    else:
        print(f"You guessed it right! Number is {number}")
    attempts-=1
if guess!=number:
    print("Better luck next time!")
    print("Number is {0}".format(number))

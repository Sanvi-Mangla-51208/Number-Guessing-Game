print("Number Guessing Game")
print("Guess a number between 1 and 9")
import random
number=random.randint(1,9)
chances=0
while chances < 5:
    guess= int(input("Enter your guess:- "))
    if guess > number:
        print("Your guess was high - Pick a number lower than",guess)
        guess=input("Enter your guess:- ")
    elif guess < number:
        print("Your guess was low - Pick a number higher than",guess)
        guess=input("Enter your guess:- ")
    if guess == number:
        print("Congratulations!! YOU WON!!")
        break
    chances=chances+1
if chances > 5:
    print("You Lose!!! The number is",number)
    

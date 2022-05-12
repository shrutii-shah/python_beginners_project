#Begineers guess number project - simple
#This project uses, random module from python library, user input, while loop with if else statement, print statement and python operators 

import random

random_number = random.randint(1,50)

guess_number = int(input("Enter your guess number between 1 and 50: "))

while True:
    if guess_number == random_number:
        print("You have guessed the correct number!! Yay!!")
        break

    elif guess_number > random_number and guess_number <= 50:
        print("Your guess is High!! Guess Again!!")
        guess_number = int(input("Enter your guess number between 1 and 50: "))
    elif guess_number < random_number and guess_number > 0:
        print("Your guess is low!! Guess Again!!")
        guess_number = int(input("Enter your guess number between 1 and 50: "))
    elif guess_number > 50 or guess_number < 1:
        print("Please input the number between 1 and 50")
        guess_number = int(input("Enter your guess number between 1 and 50: "))
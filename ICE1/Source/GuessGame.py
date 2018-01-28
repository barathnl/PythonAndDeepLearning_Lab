import random

print("Welcome to Guess Game. Please select a lucky number between 0 and 9")

while 0 == 0:
    n = random.randint(0,9)
    n1 = input("Enter the lucky number between 0-9:")
    guess = int(n1)
    if guess == n:
        print("Yipeee! Number guessed by you is right on target. ")
        break
    elif guess > n:
        print("Hard Luck! The Number guessed is above the random number")
    else:
        print("Try Harder! The  Number guessed is below the random number")
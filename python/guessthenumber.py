import random
number = random.randint(1,10)
attempts = 0

while attempts < 10:
    guess = input("Enter a number between 1 and 10!")

    if guess != number:
        print("Try again")

    if guess == number:
        break

    attempts += 1

    if attempts >= 10:
        print("You lose!")

if guess == number:
    print("Congrats")

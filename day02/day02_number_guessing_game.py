import random

number = random.randrange(1,21)
rounds = 0

while True:
    rounds += 1
    user_guess = int(input("Guess a number between 1 and 20 "))
    if user_guess == number:
        print(f"Good guess!")
        break
    if user_guess < number:
        print(f"your guess is too small, try again")
    else:
        print(f"your guess is too big, try again")
print(f"You found the correct number after {rounds} rounds")

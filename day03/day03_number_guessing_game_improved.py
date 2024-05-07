import random

def main():
    while True:
        user_guess = game()
        if user_guess != "x":
            answer = input("Would you like to start a new game? (enter 'yes' or 'no'): ")
            if answer.lower() == "no":
                print("Hope you enjoyed!")
                break
            elif answer.lower() == "yes":
                continue
            else:
                print("Invalid answer. Restarting the game")
        else:
            break

def random_number_generation():
    number = random.randrange(1, 21)
    return number

def reset_game_parameters():
    number = random_number_generation()
    rounds = 0
    return (number,rounds)

def game():
    (number,rounds) = reset_game_parameters()
    while True:
        user_guess = input("Guess a number between 1 and 20: ")

        if not user_guess.isnumeric():
            if user_guess == "x":
                return(user_guess)
                break
            elif user_guess == "n":
                print("Starting a new game:")
                (number,rounds) = reset_game_parameters()
            elif user_guess == "s":
                print(f"The secret number is {number}")
            else:
                print("Please enter a valid number.")
        else:
            rounds += 1
            guess = int(user_guess)
            if guess == number:
                print("Good guess!")
                print(f"You found the correct number after {rounds} rounds")
                break
            elif guess < number:
                print("Your guess is too small, try again")
            else:
                print("Your guess is too big, try again")
    

main()

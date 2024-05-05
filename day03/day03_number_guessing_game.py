
def main():
    number = random_number_generation()
    game_generator(number)
    
def random_number_generation():
    import random
    number = random.randrange(1,21)
    return (number)

def play_again():
    answer = input("Would you like to play again?(enter 'yes' or 'no')")
    if answer == "yes":
        main()
    else:
        print("Hope you enjoyed  :)")

def game_generator(number):
    rounds = 0
    while True:
        user_guess = input("Guess a number between 1 and 20 ")

        if user_guess.isnumeric():
            rounds += 1
            if int(user_guess) == number:
                print(f"Good guess!")
                print(f"You found the correct number after {rounds} rounds")
                play_again()
                break
            if int(user_guess) < number:
                print(f"your guess is too small, try again")
            else:
                print(f"your guess is too big, try again")
            
        else:
            if user_guess == "x":
                break
            elif user_guess == "n":
                play_again()
            elif user_guess == "s":
                print(f"The secret number is {number}")
            else:
                user_guess = input("put a valid answer ")
    

main()
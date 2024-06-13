import random
import tkinter as tk
from tkinter import messagebox

def random_number_generation():
    return random.randrange(1, 21)

def reset_game_parameters(game_state):
    game_state["number"] = random_number_generation()
    game_state["rounds"] = 0

def start_new_game(game_state, label_result):
    reset_game_parameters(game_state)
    label_result.config(text="nnn")

def show_secret_number(game_state):
    messagebox.showinfo("Secret Number", f"The secret number is {game_state['number']}")

def guess_number(game_state, label_result, entry_guess):
    user_guess = entry_guess.get()
    if user_guess.isnumeric():
        guess = int(user_guess)
        game_state["rounds"] += 1
        if guess == game_state["number"]:
            messagebox.showinfo("Good Guess!", f"You found the correct number after {game_state['rounds']} guesses")
            start_new_game(game_state, label_result)
        elif guess < game_state["number"]:
            label_result.config(text="Your guess is too small, try again")
        else:
            label_result.config(text="Your guess is too big, try again")
        entry_guess.delete(0, tk.END)
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

def exit_game(game_gui):
    game_gui.quit()

def main():
    game_state = {
        "number": random_number_generation(),
        "rounds": 0
    }

    game_gui = tk.Tk()
    game_gui.title("Guess the Number")

    label_result = tk.Label(game_gui, text="")
    label_result.pack()

    label_instruction = tk.Label(game_gui, text="Guess a number between 1 and 20:")
    label_instruction.pack()

    entry_guess = tk.Entry(game_gui)
    entry_guess.pack()

    button_guess = tk.Button(game_gui, text="Guess", command=lambda: guess_number(game_state, label_result, entry_guess))
    button_guess.pack()

    button_new_game = tk.Button(game_gui, text="New Game", command=lambda: start_new_game(game_state, label_result))
    button_new_game.pack()

    button_show_number = tk.Button(game_gui, text="Show Number", command=lambda: show_secret_number(game_state))
    button_show_number.pack()

    button_exit = tk.Button(game_gui, text="Exit", command=lambda: exit_game(game_gui))
    button_exit.pack()

    game_gui.mainloop()

main()

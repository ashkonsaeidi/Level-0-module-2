import random
import sys
from tkinter import messagebox, Tk
from playsound import playsound


def crack_the_safe():
    pass
    # TODO: Your mission: Use the try_code method to crack the safe
    #  by trying all possible combinations
chicken = random.randint(0, 999)


def try_code(guess):
    print("trying " + str(guess))

    secret_code = 999999 - chicken

    if guess == secret_code:
        messagebox.showinfo(None, "Congratulations! You cracked the safe with " + str(guess))
        play_the_sound_of_success()



def play_the_sound_of_success():
    playsound('me-gusta.wav')


# ======================= DO NOT EDIT THE CODE BELOW =========================




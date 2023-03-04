import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.askstring(None, prompt="Enter a question for the magic 8 ball to answer")
    # Make a variable and initialize it to a random number between 0 and 3
    number = random.randint(0,3)
    print(number)
    # If the random number is 0
    if number == 0:
        messagebox.showinfo(None, message="Yes")

        # tell the user "Yes"

    # If the random number is 1
    if number == 1:
        messagebox.showinfo(None, message="No")
        # tell the user "No"

    # If the random number is 2
    if number == 2:
        messagebox.showinfo(None, message="Maybe ask google?")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
    if number == 3:
        message

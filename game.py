import tkinter as tk
from tkinter import Label
from tkinter.ttk import Combobox
import random

master = tk.Tk()
master.geometry("400x350+400+50")
master.title("CLOCK")
master.attributes('-fullscreen', True)
master.configure(bg="black")
number_guess = random.randint(1, 10)
try_amount = 3

def guess():
    print(number_guess)
    global number_entered
    number_entered = Combobox(master, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    number_entered.set("choose")
    number_entered.grid(row=1, column=0)
    global b1
    b1 = tk.Button(master, text="Enter", command=check)
    b1.grid(row=1, column=1)
    
def check():
    global try_amount
    try_amount -= 1
    num = int(number_entered.get())
    b1.destroy()
    number_entered.destroy()
    if number_guess == num:
        l1 = Label(master, font=("Calibri", 90), bg="black", fg="white")
        l1.config(text="Number guessed :D ")
        l1.grid(row=0, column=1)
    else:
        if try_amount > 0:
            l1 = Label(master, font=("Calibri", 90), bg="black", fg="white")
            l1.config(text="Try Again :D ")
            l1.grid(row=0, column=1)
            guess()
        else:
            l1 = Label(master, font=("Calibri", 90), bg="black", fg="white")
            l1.config(text="Out of tries!")
            l1.grid(row=0, column=1)

guess()
master.mainloop()

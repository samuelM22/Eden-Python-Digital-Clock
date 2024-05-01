from tkinter import Tk
from tkinter import Label
import time

screen = Tk()
screen.title("Eden Digital Clock")

def my_clock():
    timeVar = time.strftime("%I:%M:%S:%p")
    eden_clock.config(text=timeVar)
    eden_clock.after(200, my_clock)

eden_clock = Label(screen, font=("calibre", 120), bg="black", fg="sky blue")
eden_clock.pack()
my_clock()



screen.mainloop()


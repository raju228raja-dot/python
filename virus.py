from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Virus")
window.geometry("300x200")

def virus():
    messagebox.showwarning("Virus", "Your computer is infected!")

button = Button(window, text="Scan for viruses", command=virus)
button.place(x=80, y=80)

window.mainloop()
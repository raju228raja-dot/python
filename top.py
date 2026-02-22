from tkinter import *

root = Tk()
root.title("Top Level Window")

def open_window():
    top = Toplevel(root)
    top.title("Top Level Window")
    top.geometry("200x100")

    l2 = Label(top, text="This is a top level window")
    l2.pack(pady=20)

l3 = Label(root, text="This is the main window")
l3.pack(pady=20)

button = Button(root, text="Open New Window", command=open_window)
button.pack(pady=20)

root.mainloop()
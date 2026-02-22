from tkinter import *
from PIL import Image, ImageTk

# 1. Setup the main window
window = Tk()
window.title("Tkinter Image")

# Note: Your screenshots show a geometry of 300x200, 
# but your labels are placed at y=360. 
# I've increased the height so you can see everything.
window.geometry("450x450") 

# 2. Load and prepare the image
# Make sure "background.jpg" is uploaded to your Trinket files!
upload = Image.open("download.png")
image = ImageTk.PhotoImage(upload)

# 3. Create and place the Image Label
label = Label(window, image=image, height=350, width=350)
label.place(x=50, y=0)

# 4. Create and place the Text Label
label2 = Label(
    window, 
    text="Welcome to Tkinter Image", 
    font=("Arial", 16), 
    bg="white"
)
label2.place(x=40, y=360)

# 5. Start the application
window.mainloop()
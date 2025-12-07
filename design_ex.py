# pip install tkinter, pillow
# Понякога имената на библиотеките не отговарят точно на импортите
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk


import tkinter as tk
from PIL import Image, ImageTk

# Create main window
root = tk.Tk()
root.title("Tkinter Demo")
root.geometry("626x500+650+300")

# Load chosen image
image_path = r"C:\Users\didka\Desktop\1763904772739.jpg"
image = Image.open(image_path)
image = image.resize((400, 300))
photo = ImageTk.PhotoImage(image)

# Display image
image_label = tk.Label(root, image=photo)
image_label.pack(pady=10)

# # Text field label
# masked_word = tk.Label(root, text="Woof! I am the best dog in the world!")
# masked_word.pack(pady=10)

# Entry field
entry = tk.Entry(root)
entry.pack(pady=10)

# # Button callback
def greet():
    name = entry.get()
    tk.messagebox.showinfo("Greetings", f"Hello, {name}!")

button = tk.Button(root, text="Ok", command=greet)
button.pack(pady=10)

root.mainloop()

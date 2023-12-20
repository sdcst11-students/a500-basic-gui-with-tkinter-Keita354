import tkinter as tk
from tkinter import *

window = tk.Tk()
window.title("Example")
window.geometry("280x145")

label1 = tk.Label(window, text="  A cuddly little puppy! This is from the same  \n   creators who brought you Keropi and Kero Kero  ", bg="#9be8e4")

dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto, borderwidth=0)

name = tk.Label(window, text="Poachacco!")

# Change to .grid method
label1.grid(row=2, column=0, columnspan=3, pady=(10, 0), padx=10, sticky="w")
dog.grid(row=1, column=1, pady=(0, 0), padx=10, sticky="w")
name.grid(row=1, column=2, pady=(0, 0), padx=10, sticky="w")




window.mainloop()

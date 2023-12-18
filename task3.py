import tkinter as tk
from tkinter import *
#importing ttk is required to use the tkinter.place() method
from tkinter import ttk



window = tk.Tk()
window.title("Example")
window.geometry("270x137")

label1 = tk.Label(window,text="  A cuddly little puppy! This is from the same  \n   creators who brought you Keropi and Kero Kero  ", bg="#9be8e4")

dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto, borderwidth=0,)

name = tk.Label(window, text="Poachacco!", )
#change to .grid method

label1.place(x=0,y=100)
dog.place(x=70, y=0)
name.place(x=135, y=40)

window.mainloop()
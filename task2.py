import tkinter as tk
from tkinter import *
#importing ttk is required to use the tkinter.place() method
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("475x165")

#convert to .place

dogphoto = PhotoImage(file="dog.png")
dog = tk.Label(window, image=dogphoto)
dog.place(x=8, y=-2)

title = tk.Label(window, text = "Client Database")
title.place(x=160, y=45)

search = tk.Button(window, text="Search by Name")
search.place(x=260, y=-3)

entry_search = tk.Entry(window)
entry_search.place(x=355, y=2)

head1 = tk.Label(window, text = "Name")
head1.place(x=29, y=95)

entry_1 = tk.Entry(window)
entry_1.place(x=3, y=115)

head2 = tk.Label(window, text = "Type")
head2.place(x=115, y=95)

entry_2 = tk.Entry(window)
entry_2.place(x=100, y=115)

head3 = tk.Label(window, text = "Breed")
head3.place(x=195, y=95)

entry_3 = tk.Entry(window)
entry_3.place(x=180, y=115)

head4 = tk.Label(window, text = "Owner")
head4.place(x=280, y=95)

entry_4 = tk.Entry(window)
entry_4.place(x=265, y=115)

head5 = tk.Label(window, text = "Birthdate")
head5.place(x=380, y=95)

entry_5 = tk.Entry(window)
entry_5.place(x=350, y=115)

save = tk.Button(window, text="Save Entry")
save.place(x=195, y=135)

prev = tk.Button(window, text="<Previous")
prev.place(x=2, y=135)

prev = tk.Button(window, text="<Previous")
prev.place(x=2, y=135)

nex = tk.Button(window, text="Next>")
nex.place(x=400, y=135)

window.mainloop()
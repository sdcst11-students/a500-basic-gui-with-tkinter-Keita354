import tkinter as tk



window = tk.Tk()
window.title("Tk")

entry1 = tk.Entry(window)
entry1.grid(row=0, column=0, padx=5, pady=5)

multiply_label = tk.Label(window, text="x")
multiply_label.grid(row=0, column=1, padx=5, pady=5)

entry2 = tk.Entry(window)
entry2.grid(row=0, column=2, padx=5, pady=5)

equal_button = tk.Button(window, text="=")
equal_button.grid(row=0, column=3, padx=5, pady=5)

out3 = tk.Entry(window)
out3.grid(row=0, column=4, padx=5, pady=5)





window.mainloop()
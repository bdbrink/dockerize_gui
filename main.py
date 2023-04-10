import tkinter as tk
from tkinter.messagebox import showinfo

root = tk.Tk()

def show_message():
    showinfo("hello world!")

btn = tk.Button(root, text="Click me", command=show_message)
btn.pack()

root.mainloop()
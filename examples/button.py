import tkinter as tk
from tkinter import ttk



root = tk.Tk()

def greet():
    print("Hello world")
greet_button = ttk.Button(root, text='Greet', command=greet, padding=(20, 20))
greet_button.pack()




root.mainloop()





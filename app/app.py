import tkinter as tk
from tkinter import ttk



root = tk.Tk()

# telinha...
ttk.Label(root, text='Hello world!', padding=(100, 80)).pack()


def greet():
    print("Hello world")


def name():
    print('rodrigo machado')

greet_button = ttk.Button(root, text='Greet', command=greet, padding=(40, 20))
greet_button.pack(side='left', fill='x')

quit_button = ttk.Button(root, text='Quit', command=root.destroy, padding=(40, 20))
quit_button.pack(side='right', fill='x')

root.mainloop()





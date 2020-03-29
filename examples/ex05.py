import tkinter as tk
from tkinter import ttk


root = tk.Tk()

main = ttk.Frame(root)
main.pack(side='left', fill='both', expand=True)

tk.Label(root, text='Label red',  bg='red').pack(side='top', expand=True, fill='both')
tk.Label(root, text='Label yellow', bg='yellow').pack(side='top', expand=True, fill='both')
tk.Label(root, text='Label green', bg='green').pack(side='left', expand=True, fill='both')
tk.Label(root, text='Label pink', bg='pink').pack(side='left', expand=True, fill='both')



root.mainloop()
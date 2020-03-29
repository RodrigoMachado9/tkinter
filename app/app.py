import tkinter as tk
from tkinter import ttk

root = tk.Tk()



def greet():
    print(f"Hello {user_name.get() or 'world'}!")


def name():
    print('rodrigo machado')

user_name = tk.StringVar()


name_label = ttk.Label(root, text="Name: ")                       # lbl name;
name_label.pack(side="left", padx=(0, 10))
name_entry = ttk.Entry(root, width=15, textvariable=user_name)     # lbl entry name;
name_entry .pack(side='left')
name_entry.focus()




# telinha....
ttk.Label(root, text='Telinha marota!', padding=(100, 80)).pack()                      # name { container } tela


greet_button = ttk.Button(root, text='Greet', command=greet, padding=(40, 20))
greet_button.pack(side='left', fill='y', expand=True)

quit_button = ttk.Button(root, text='Quit', command=root.destroy, padding=(40, 20))
quit_button.pack(side='left', fill='x', expand=True)

root.mainloop()





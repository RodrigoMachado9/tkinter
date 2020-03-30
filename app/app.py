import tkinter as tk
from tkinter import ttk, Frame


class Aplication(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.mount_application()
        self.pack()

    def lbl(self):
        name_label = ttk.Label(root, text="Name: ")  # lbl name;
        name_label.pack(side="left", padx=(0, 10))
        name_entry = ttk.Entry(root, width=15, textvariable=self.user_name)  # lbl entry name;
        name_entry.pack(side='left')
        name_entry.focus()

    def lbl_container_main(self):
        # telinha....
        ttk.Label(root, text='Home screen - enter parameters', padding=(100, 80)).pack()  # name { container } tela

    def btn(self):
        greet_button = ttk.Button(root, text='Greet', command=self.greet, padding=(40, 20))
        greet_button.pack(side='left', fill='y', expand=True)
        quit_button = ttk.Button(root, text='Quit', command=root.destroy, padding=(40, 20))
        quit_button.pack(side='left', fill='y', expand=True)

    def mount_application(self):
        self.user_name = tk.StringVar()
        self.lbl()
        self.lbl_container_main()
        self.btn()

    def greet(self):
        print(f"Hello {self.user_name.get() or 'world'}!")




root = tk.Tk()
root.title('Scientific initiation project ')
app = Aplication(master=root)
app.mainloop()
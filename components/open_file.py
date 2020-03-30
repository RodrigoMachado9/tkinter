"""
    1 - ( escolher arquivo de abertura): Ao abrir o programa ele chama a tela do nome da imagem
        a carregar (achei uma versão e exemplo que abre a tela de windows para escolha do arquivo)
"""


import tkinter as tk
from tkinter import ttk, Frame, Radiobutton, W


class MainScreen(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.mount_application()
        self.pack()

    def lbl(self):
        self.user_name = tk.StringVar()
        self.user_name.set('nome do ultimo arquivo')
        name_label = ttk.Label(root, text="Name:")  # lbl name;
        name_label.pack(side="left", padx=(0, 10))
        name_entry = ttk.Entry(root, width=23, textvariable=self.user_name)  # lbl entry name;
        name_entry.pack(side='left')
        name_entry.focus()

    def lbl_container_main(self):
        # telinha....
        txt_container = tk.Label(root, text='Main-screen -  ( please enter parameters )')
        txt_container.pack(side='top')

        main_container = ttk.Label(root, padding=(100, 100))  # name { container } tela
        main_container.pack()

    def btn(self):
        greet_button = ttk.Button(root, text='Open', command=self.greet, padding=(40, 20),  width=15)
        greet_button.pack(side='left', fill='y', expand=True)
        # greet_button.place(x=25, y=25)

        quit_button = ttk.Button(root, text='Quit', command=root.destroy, padding=(40, 20), width=15)
        quit_button.pack(side='left', fill='y', expand=True)


    def _options_for_radio_btn(self):
        MODES = [
            ("Treinamento", "1"),
            ("Classificação", "2")
        ]
        v = tk.StringVar()
        v.set("1")  # initialize

        for text, mode in MODES:
            b = Radiobutton(root, text=text, variable=v, value=mode)
            b.pack(anchor=W, padx=(0, 10))


    def mount_application(self):
        self.lbl()
        self.lbl_container_main()
        self._options_for_radio_btn()
        self.btn()

    def greet(self):
        print(f"Hello {self.user_name.get() or 'world'}!")


root = tk.Tk()
root.title('Scientific initiation project ')
# root.geometry('600x600')
app = MainScreen(master=root)
app.mainloop()
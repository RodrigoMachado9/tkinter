# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 19:50:51 2019

@author: JOÃOVAGNER
"""
# !/usr/bin/python3
import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


def mensage_help():
    arquivo = open('arquivo.txt', 'r')
    unica_string = arquivo.read()
    arquivo.close()
    messagebox.showinfo("Say Hello", unica_string)


'''
showerror()
showwarning()
showinfo()
'''

# cria a janela
window_parametros = tkinter.Tk()
window_parametros.title("Parametros")
window_parametros.geometry("250x250")

root = tk.Tk()
dirNome = filedialog.askdirectory(parent=root, initialdir="/", title='Selecione a pasta')

# cria o botão
B1 = tkinter.Button(window_parametros, text="Help", command=mensage_help)
B1.place(x=35, y=50)
B1.pack(side='top')
# cria o label
label_widget = tkinter.Label(window_parametros, text="Digite o nome da imagem a ser carregada")
label_widget.pack(side='top')
# cria o box texto
entry_widget = tkinter.Entry(window_parametros)
entry_widget.insert(0, "nome do arquivo")
entry_widget.pack(side='top')
# cria os radio button
v = tkinter.IntVar()
v.set(1)  # need to use v.set and v.get to
# set and get the value of this variable
radiobutton_widget1 = tkinter.Radiobutton(window_parametros,
                                          text="Area Sadia",
                                          variable=v, value=1)
radiobutton_widget2 = tkinter.Radiobutton(window_parametros,
                                          text="Area lesionada",
                                          variable=v, value=2)
radiobutton_widget1.pack(side='left')
radiobutton_widget2.pack(side='left')
# kernel de atendimento
window_parametros.mainloop()
print('valor:')
print(v.get())  # ok
print('digitou:')
print(entry_widget.get())

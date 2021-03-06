
import tkinter as tk

window = tk.Tk()


def increase_value():
    value = int(lbl_value["text"])
    if value == 10:
        print('2222222222222222')
    lbl_value["text"] = f"{value + 1}"


def decrease_value():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease_value)
btn_decrease.grid(row=0, column=0, sticky="nsew")


lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)


btn_increase = tk.Button(master=window, text="+", command=increase_value)
btn_increase.grid(row=0, column=2, sticky="nsew")



window.mainloop()
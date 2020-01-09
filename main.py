#
# "main"
#
#git
# 
# # Created by Sergey Yaksanov at 09.01.2020
# Copyright © 2019 Yakser. All rights reserved.

import tkinter
import random
import periodic_table


def check():

    if entry.get() == periodic[rand_num]:
        new_num()
        lbl_num.config(text=str(rand_num))



master = tkinter.Tk()
master.title("Periodic table guessing game")
master.geometry("250x250")
periodic = periodic_table.get_periodic_table()


def new_num():
    global rand_num
    rand_num = random.randint(1, 112)


rand_num = random.randint(1, 112)

lbl_num = tkinter.Label(text=str(rand_num))
lbl_num.grid(column=1, row=0)

lbl_el = tkinter.Label(text='Element:')
lbl_el.grid(column=0, row=1)

entry = tkinter.Entry()
entry.grid(column=1, row=1)

btn_ok = tkinter.Button(text='Ok', command=check)
btn_ok.grid(column=2, row=1)


# QUIT BTN
btn_quit = tkinter.Button(text='Exit', command=quit, width=10)
btn_quit.place(x=85, y=225)

master.mainloop()


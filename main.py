import tkinter
import random
import periodic_table


def check():
    global STREAK
    if entry.get() == periodic[rand_num]:

        lbl_status.config(text='Correct', fg='green')
    else:
        lbl_status.config(text='Incorrect', fg='red')
        STREAK += 1
        if STREAK == 5:
            quit()

        a_n = 0
        for i in periodic:
            if periodic[i] == entry.get():
                a_n = i
        if a_n == 0:
            lbl_hints.config(text='This element does not exists')
            return

        if a_n < rand_num:
            lbl_hints.config(text='Correct element is to the right')
        else:
            lbl_hints.config(text='Correct element is to the left')


def new_num():
    global rand_num
    rand_num = random.randint(1, 112)
    lbl_num.config(text=str(rand_num))
    lbl_ans.config(text='')
    entry.delete(0, 'end')


def get_ans():
    lbl_ans.config(text=periodic[rand_num], fg='green')


master = tkinter.Tk()
master.title("Periodic table guessing game")
master.geometry("250x200")
periodic = periodic_table.get_periodic_table()
STREAK = 0
rand_num = random.randint(1, 112)

lbl_num = tkinter.Label(text=str(rand_num))
lbl_num.grid(column=1, row=0)

lbl_el = tkinter.Label(text='Element:')
lbl_el.grid(column=0, row=1)

entry = tkinter.Entry(width=5)
entry.grid(column=1, row=1, padx=5)

btn_submit = tkinter.Button(text='Submit', command=check)
btn_submit.grid(column=2, row=1, padx=5)

btn_gen = tkinter.Button(text='Generate new', command=new_num)
btn_gen.grid(column=0, row=4, pady=5)

btn_ans = tkinter.Button(text='Answer', command=get_ans)
btn_ans.grid(column=2, row=4)
lbl_ans = tkinter.Label(text='')
lbl_ans.grid(column=1, row=5)

lbl_status = tkinter.Label(text='')
lbl_status.grid(column=1, row=2)

lbl_hints = tkinter.Label(text='')
lbl_hints.grid(column=0, row=3, columnspan=3)

# QUIT BTN
btn_quit = tkinter.Button(text='Exit', command=quit, width=10)
btn_quit.grid(column=1, row=6)

master.mainloop()

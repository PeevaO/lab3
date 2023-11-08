from tkinter import *
import string
import random
def clicked():
    btn.destroy()
    lbl.destroy()
    y = str(tx.get())
    randLetter1 = random.choice(string.ascii_uppercase)
    randLetter2 = random.choice(string.ascii_uppercase)
    randLetter3 = random.choice(string.ascii_uppercase)
    randLetter4 = random.choice(string.ascii_uppercase)
    sum = str(int(y[3] + y[4] + y[5]) + int(y[0] + y[1] + y[2]))
    if len(sum)<4:
        sum = '0' + sum
    y = y[3] + y[4] + y[5] + randLetter1 + randLetter2 + '-' + y[0] + y[1] + y[2] + randLetter3 + randLetter4 + ' ' + sum
    lb = Label(window, text=y, font=("Times new Roman", 30))
    lb.grid(column=1, row=0)
    tx.destroy()

window = Tk()
window.title("Добро пожаловать в самое прекрасное приложение!")
window.geometry('1100x550')
lbl = Label(window, text="Введите DEC-число из 6 знаков.", font=("Times new Roman", 30))
lbl.grid(column=0, row=0)
tx = Entry(window, width=10)
tx.grid(column=2, row=0)
btn = Button(window, text="Получить ключ!", bg="black", fg="white", command=clicked)
btn.grid(column=3, row=0)
window.mainloop()
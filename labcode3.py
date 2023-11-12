from tkinter import *
from PIL import ImageTk, Image
import string
import random
def clicked():
    btn.destroy()
    lbl.destroy()
    yy = str(tx.get())
    tx.destroy()
    randLetter1 = random.choice(string.ascii_uppercase)
    randLetter2 = random.choice(string.ascii_uppercase)
    randLetter3 = random.choice(string.ascii_uppercase)
    randLetter4 = random.choice(string.ascii_uppercase)
    sum = str(int(yy[3] + yy[4] + yy[5]) + int(yy[0] + yy[1] + yy[2]))
    if len(sum)<4:
        sum = '0' + sum
    yy = yy[3] + yy[4] + yy[5] + randLetter1 + randLetter2 + '-' + yy[0] + yy[1] + yy[2] + randLetter3 + randLetter4 + ' ' + sum

    bg = PhotoImage(file="terraria1.png")
    pic = Label(window, image=bg)
    pic.place(x=0, y=0, relwidth=1, relheight=1)
    lb = Label(window, text=yy, font=("Times new Roman", 30))
    lb.pack(pady=50)
    window.mainloop()

window = Tk()
window.title("Добро пожаловать в самое прекрасное приложение!")
window.geometry('1280x720')
lbl = Label(window, text="Введите DEC-число из 6 знаков.", font=("Times new Roman", 30))
lbl.grid(column=0, row=0)
tx = Entry(window, width=10)
tx.grid(column=2, row=0)
btn = Button(window, text="Получить ключ!", bg="black", fg="white", command=clicked)
btn.grid(column=3, row=0)
window.mainloop()

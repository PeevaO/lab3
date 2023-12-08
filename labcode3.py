from tkinter import Tk, PhotoImage
from tkinter.ttk import Label, Entry, Button
import string
import random

HEIGHT = 720
WIDTH = 1280
WIDTH_ENTER = 6
NUM_SYMBOLS = 6


def clicked():
    entered_num = str(entry.get())
    label_1page.destroy()
    validate(entered_num)


def validate(input_num):
    txt = 'Попробуйте еще раз.\nНеобходимо ввести DEC-число из 6 знаков.'
    label_2page = Label(window, text=txt, font=("Times new Roman", 25))
    label_2page.grid(column=0, row=0)

    if input_num.isdigit() and (len(input_num) == NUM_SYMBOLS):
        create_window(input_num, label_2page)
    window.mainloop()


def create_window(number, page):
    page.destroy()
    button.destroy()
    entry.destroy()
    txt = generate_key(number)
    picture = PhotoImage(file="terraria1.png")
    background = Label(window, image=picture)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    label_3page = Label(window, text=txt, font=("Times new Roman", 30))
    label_3page.grid(column=1, row=3, padx=30, pady=0)
    window.mainloop()


def generate_key(num):
    random_Letter1 = random.choice(string.ascii_uppercase)
    random_Letter2 = random.choice(string.ascii_uppercase)
    random_Letter3 = random.choice(string.ascii_uppercase)
    random_Letter4 = random.choice(string.ascii_uppercase)
    sum = str(int(num[3:]) + int(num[:3]))
    if len(sum) < 4:
        sum = '0' + sum
    key = (f'{num[3:]}{random_Letter1}{random_Letter2}-{num[:3]}{random_Letter3}{random_Letter4} {sum}')
    return key


window = Tk()
window.title("Добро пожаловать в самое прекрасное приложение!")
window.geometry(f'{WIDTH}x{HEIGHT}')
label_1page = Label(window, text="Введите DEC-число из 6 знаков.", font=("Times new Roman", 25))
label_1page.grid(column=0, row=0)
entry = Entry(window, width=WIDTH_ENTER)
entry.grid(column=0, row=2)
button = Button(window, text="Получить ключ!", command=clicked)
button.grid(column=0, row=3)
window.mainloop()

from tkinter import *
from PIL import ImageTk, Image
import string
import random
def clicked():
    window.geometry('1280x720')
    button.destroy()
    label_1page.destroy()
    input_num = str(entry.get())
    entry.destroy()
    random_Letter1 = random.choice(string.ascii_uppercase)
    random_Letter2 = random.choice(string.ascii_uppercase)
    random_Letter3 = random.choice(string.ascii_uppercase)
    random_Letter4 = random.choice(string.ascii_uppercase)
    sum = str(int(input_num[3:]) + int(input_num[:3]))
    if len(sum) < 4:
        sum = '0' + sum
    key = input_num[3:] + random_Letter1 + random_Letter2 + '-' + input_num[:3] + random_Letter3 + random_Letter4 + ' ' + sum

    picture = PhotoImage(file="terraria1.png")
    background = Label(window, image=picture)
    background.place(x=0, y=0, relwidth=1, relheight=1)
    label_2page = Label(window, text=key, font=("Times new Roman", 30))
    label_2page.pack(pady=50)
    window.mainloop()

window = Tk()
window.title("Добро пожаловать в самое прекрасное приложение!")
window.geometry('460x320')
label_1page = Label(window, text="Введите DEC-число из 6 знаков.", font=("Times new Roman", 25))
label_1page.grid(column=0, row=0)
entry = Entry(window, width=15)
entry.grid(column=0, row=2)
button = Button(window, text="Получить ключ!", bg="black", fg="white", command=clicked)
button.grid(column=0, row=3)
window.mainloop()

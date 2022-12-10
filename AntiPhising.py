from tkinter import *
import tkinter.messagebox as tkmb
import csv
from main import *

HOST = 'https://parsesite.ru/ru/cost/'

root = Tk()

def btn_click():
    text = Input.get()
    a = text.rpartition('/')[-1]
    info_error = f'Вы указали неверный URL, либо данный URL не признан сервисом parsesite.ru, как защищённым.'
    info_truth = f'Данный URL был проверен с помощью сервиса parsesite.ru.\nДля полного ознакомления можете перейти по ссылке: {HOST+a}'
    if text in open('sites.csv').read():
        tkmb.showinfo(title='Название', message=info_truth)
    else:
        tkmb.showerror(title='Название', message=info_error)

def ObnovlenieSpiska():
    tkmb.showinfo(title='Название', message= f'Ожидайте следующее всплывающее окно, проходит полное обновление данных')
    main()
    tkmb.showinfo(title='Название', message= f'Обновление прошло успешно.')

root['bg'] = '#fafafa'
root.title('AntiPhishing')
root.wm_attributes('-alpha', 1)
root.geometry('300x250')
root.resizable(width=False, height=False)

canvas = Canvas(root, height=300, width=250)
canvas.pack()

frame = Frame(root, bg='white')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Введите URL страницы', bg='white', font=40)
title.pack()

btn = Button(frame, text='Проверить', bg='white', command=btn_click)
btn.pack()

btn = Button(frame, text='Обновить список', bg='white', command=ObnovlenieSpiska)
btn.pack()

Input = Entry(frame, bg='white')
Input.pack()
root.mainloop()

from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Окно #1")
root.geometry("600x1200")


main_frame = Frame(root)
names = ["№1 Планиметрия", "№2 Векторы ", "№3 Стереометрия ", "№4 Простая теория вероятности ", "№5 Сложная вероятность ", "№6 Уравнения ", "№7 Вычисления и преобразования ", "№8 Производная и первообразная ", "№9 Прикладная задача ", "№10 Текстовая задача ", "№11 Графики функций ","№12 Анализ функций ", "№13 Уравнения ", "№14 Стереометрия ", "№15 Неравенства ", "№16 Экономическая задача ", "№17 Планиметрия ", "№18 Задача с параметром ", "№19 Числа и их свойства "]
var = IntVar()# по сути эти две строки нужно записать цикл и создать массив где все 0
var.set(0)#а потом менять 0 на то что будет натыкано в итоге

for i in range(len(names)):
    frame = Frame(root, borderwidth=3, relief=SOLID, padding=[1, 2])
    exercises = Label(frame, text=names[i], font=("Arial", 10, 'bold'))
    kolZadani = Spinbox(frame, from_=0, to=100, textvariable=var)
    exercises.pack(side=LEFT)
    kolZadani.pack(side=RIGHT)
    frame.pack(anchor="nw", fill=X, padx=10, pady=5)

ready=Button(root, text="Готово", command=root.destroy)
ready.pack(anchor="se", padx=10, pady=50)

root.mainloop()

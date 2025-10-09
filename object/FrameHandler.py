import random
from tkinter import *
from tkinter.ttk import *
from object.Problem import Problem

class FrameHandler:
    def __init__(self, root: Tk):
        self.root = root

        self.problems = [] # Здесь хранятся Problem'ы
        self.frame_problems = [] # здесь хранятся Frame'ы
        self.variant_counts = []

        self.main_frame = self.main_init()

    def main_init(self):
        main_frame = Frame(self.root)
        names = ["№1 Планиметрия", "№2 Векторы ", "№3 Стереометрия ", "№4 Простая теория вероятности ",
                 "№5 Сложная вероятность ", "№6 Уравнения ", "№7 Вычисления и преобразования ",
                 "№8 Производная и первообразная ", "№9 Прикладная задача ", "№10 Текстовая задача ",
                 "№11 Графики функций ", "№12 Анализ функций ", "№13 Уравнения ", "№14 Стереометрия ",
                 "№15 Неравенства ", "№16 Экономическая задача ", "№17 Планиметрия ", "№18 Задача с параметром ",
                 "№19 Числа и их свойства "]

        for i in range(len(names)):
            self.variant_counts.append(IntVar())
            self.variant_counts[i].set(0)
            frame = Frame(main_frame, borderwidth=3, relief=SOLID, padding=[1, 2])
            exercises = Label(frame, text=names[i], font=("Arial", 10, 'bold'))
            kol_problems = Spinbox(frame, from_=0, to=100, textvariable=self.variant_counts[i])
            exercises.pack(side=LEFT)
            kol_problems.pack(side=RIGHT)
            frame.pack(anchor="nw", fill=X, padx=10, pady=5)

        ready = Button(main_frame, text="Готово", command=self.generate_on_click)
        ready.pack(anchor="se", padx=10, pady=50)
        return main_frame

    def show_main(self):
        self.main_frame.pack()

    def forget_main(self):
        self.main_frame.pack_forget()

    def generate_on_click(self):
        variant_counts = [i.get() for i in self.variant_counts] # записиваешь данные из SpinBox'ов

        for type_task in range(len(variant_counts)):
            for i in range(variant_counts[type_task]):
                self.problems.append(Problem(f'{(type_task + 1):02}_{random.randint(1, 1):02}_{random.randint(1, 1):03}'))
                self.frame_problems.append("") # Сюда добавляй Frame

        for i in self.problems:
            print(i._ID)

    def problem_init(self):
        pass
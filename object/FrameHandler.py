import random
from tkinter import *
from tkinter.ttk import *
from Problem import Problem

class FrameHandler:
    def __init__(self, root: Tk):
        self.root = root
        self.main_frame = self.main_init()

        self.problems = [] # Здесь хранятся Problem'ы
        self.frame_problems = [] # здесь хранятся Frame'ы

    def main_init(self):
        main_frame = Frame(self.root)
        names = ["Планиметрия ", "Векторы ", "Стереометрия ", "Вероятность ", "Вероятност ", "Уравнения ", "Выражения ",
                 "Графики функций ", "Прикладная задача ", "Текстовая задача "]

        for i in range(len(names)): # заданий же 19 должно быть...
            frame = Frame(main_frame, borderwidth=3, relief=SOLID, padding=[1, 2])
            ext = Label(frame, text=names[i], font=("Arial", 10, 'bold'))
            sp = Spinbox(frame, from_=0, to=100)
            ext.pack(side=LEFT)
            sp.pack(side=RIGHT)
            frame.pack(anchor="nw", fill=X, padx=10, pady=5)

        return main_frame

    def show_main(self):
        self.main_frame.pack()

    def forget_main(self):
        self.main_frame.pack_forget()

    def generate_on_click(self):
        variant_counts = [] # записиваешь данные из SpinBox'ов

        for type_task in range(len(variant_counts)):
            for i in range(variant_counts[type_task]):
                self.problems.append(Problem(f'{type_task:02}_{random.randint(1, 1):02}_{random.randint(1, 1):03}'))
                self.frame_problems.append("") # Сюда добавляй Frame

    def problem_init(self):
        pass
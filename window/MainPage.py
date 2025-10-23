from tkinter import *
from tkinter import ttk

class MainPage(ttk.Frame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.tasks_count = []
        self.controller = controller
        names = ["№1 Планиметрия", "№2 Векторы ", "№3 Стереометрия ", "№4 Простая теория вероятности ",
                 "№5 Сложная вероятность ", "№6 Уравнения ", "№7 Вычисления и преобразования ",
                 "№8 Производная и первообразная ", "№9 Прикладная задача ", "№10 Текстовая задача ",
                 "№11 Графики функций ", "№12 Анализ функций ", "№13 Уравнения ", "№14 Стереометрия ",
                 "№15 Неравенства ", "№16 Экономическая задача ", "№17 Планиметрия ", "№18 Задача с параметром ",
                 "№19 Числа и их свойства "]

        for i in range(len(names)):
            self.tasks_count.append(IntVar())
            self.tasks_count[i].set(0)
            frame = ttk.Frame(self, borderwidth=3, relief=SOLID, padding=[1, 2])
            exercises = Label(frame, text=names[i], font=("Arial", 10, 'bold'))
            kol_problems = Spinbox(frame, from_=0, to=100, textvariable=self.tasks_count[i])
            exercises.pack(side=LEFT)
            kol_problems.pack(side=RIGHT)
            frame.pack(anchor="nw", fill=X, padx=10, pady=5)

        ready = Button(self, text="Готово", command=self.ready_on_click)
        ready.pack(anchor="se", padx=10, pady=50)

    def ready_on_click(self):
        self.controller.generate_problems_on_click()

    def get_tasks_count(self):
        result = [i.get() for i in self.tasks_count]
        return result
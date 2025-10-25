import tkinter as tk
from tkinter import ttk
from object.Task import Task

class TestTaskPage(ttk.Frame):
    def __init__(self, notebook, controller, task_id):
        self.notebook = notebook
        super().__init__(self.notebook)

        self.task = Task(task_id)
        self.controller = controller

        self.style = ttk.Style()
        self.setup_tab_styles()

        self.create_tab()#создаем все табы, оно у меня не заработало на классах, поэтому все в таск запихну

    def setup_tab_styles(self):
        # Создаем общий стиль для всех вкладок с цветами
        self.style.configure('TNotebook.Tab',
                             padding=[15, 5],
                             background='lightblue')  # общий цвет для всех вкладок

    def create_tab(self):#создание содержимого
        self.zadanie_frame = ttk.Frame(self)
        self.zadanie_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.zadanie = tk.Text(self.zadanie_frame, font=('Arial', 12), height=15, wrap='word')  # делаем текст задачи
        self.zadanie.pack(fill='both', expand=True)
        self.zadanie.insert('1.0', "Hello world!")
        self.zadanie.config(state='disabled')

        self.answer_frame = ttk.Frame(self)
        self.answer_frame.pack(fill='x', padx=10, pady=10)

        self.otvet_ukaz = ttk.Label(self.answer_frame, text="Ответ:", font=('Arial', 12))  # "Ответ:"
        self.otvet_ukaz.pack(side='left', padx=(0, 10))

        self.answer = ttk.Entry(self.answer_frame, font=('Arial', 12), width=40)  # поле ввода ответа
        self.answer.pack(side='left', fill='x', expand=True, padx=(0, 10))

        self.otvet = ttk.Button(self.answer_frame, text="Ответить")
        self.otvet.pack(side='right')

    def rate(self):
        print(123)
        self.task.rate(self.answer.get())
        # ... дальше расписывай

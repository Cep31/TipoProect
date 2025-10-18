import tkinter as tk
from tkinter import ttk
from object.Task import Task

answers1=[]

class TaskPage(tk.Frame):
    def __init__(self, root, controller, tasks_id):
        super().__init__(root)
        # Task - это данные задания
        self.tasks_id = tasks_id
        self.tasks = []
        self.controller = controller
        for task in tasks_id:
            self.tasks.append(Task(task))
            self.root = root
            self.root.title("Задачи")
            self.root.geometry("800x1200")

            self.style = ttk.Style()
            self.setup_tab_styles()

            self.notebook = ttk.Notebook(root)
            self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

            self.create_tab_1()#создаем все табы, оно у меня не заработало на классах, поэтому все в таск запихну
            self.create_last_tab()

    def setup_tab_styles(self):
        # Создаем общий стиль для всех вкладок с цветами
        self.style.configure('TNotebook.Tab',
                             padding=[15, 5],
                             background='lightblue')  # общий цвет для всех вкладок

    def create_tab_1(self):#создание содержимого
            exercises1 = ["какая-то задача из первого", "другая задача из первого", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
            for i in range():
                tab = ttk.Frame(self.notebook)

                self.notebook.add(tab, text={i + 1})

                zadanie_frame = ttk.Frame(tab)
                zadanie_frame.pack(fill='both', expand=True, padx=10, pady=10)

                zadanie = tk.Text(zadanie_frame, font=('Arial', 12), height=15, wrap='word')  # делаем текст задачи
                zadanie.pack(fill='both', expand=True)
                zadanie.insert('1.0', exercises1[i])
                zadanie.config(state='disabled')

                answer_frame = ttk.Frame(tab)
                answer_frame.pack(fill='x', padx=10, pady=10)

                otvet_ukaz = ttk.Label(answer_frame, text="Ответ:", font=('Arial', 12))  # "Ответ:"
                otvet_ukaz.pack(side='left', padx=(0, 10))

                answer = ttk.Entry(answer_frame, font=('Arial', 12), width=40)  # поле ввода ответа
                answer.pack(side='left', fill='x', expand=True, padx=(0, 10))

                otvet = ttk.Button(answer_frame, text="Ответить",
                                   command=lambda idx=i, ans=answer: self.get_answer(idx, ans))  # ответ
                otvet.pack(side='right')
    def get_answer(self, task_index, answer):#получаем отвтет
        user_answer = answer.get()

        if not user_answer:
            # result_label.config(text="Введите ответ!")
            return
        answers1.append(user_answer)
    def create_last_tab(self):
        tab = ttk.Frame(self.notebook)

        self.notebook.add(tab, text={"Закончить"})

        last_frame = ttk.Frame(tab)
        last_frame.pack(fill='both', expand=True, padx=10, pady=10)

        zaver=ttk.Button(last_frame, text="Хотите закончить?", command=lambda: self.show_tocho())
        zaver.pack(side='left', padx=(0, 10))

    def show_tocho(selfl, rootl):#создаем новое окно
        selfl.root = rootl
        selfl.root.title("")
        selfl.root.geometry("200x300")

        frame = ttk.Frame(rootl)
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        label=ttk.Label(frame, text="Вы точно хотите завершить?", font=('Arial', 12))
        label.pack(side='top', padx=(0, 10))

        da=ttk.Button(frame, text="завершить")#уничтожить страницу в которой задания и создать с решениями
        da.pack(side='right', padx=10, pady=10)

        net=ttk.Button(frame, text="подумаю еще", command=lambda: selfl.drop_last_tab())#уничтожить страницу в которой задания и создать с решениями
        net.pack(side='left', padx=10, pady=10)

    def drop_last_tab(selfl, rootl):#уничтожает окно с завершить
        rootl.destroy()


# root = tk.Tk()
# app = ex1Notebook(root)
# root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from object.Task import Task

answers=[[],[],[],[],[],[],[],[],[],[],[],[]]#делаю матрицу в которой будут ответы пользователя на задачи

class TaskPage(tk.Frame):
    def __init__(self, root, controller, tasks_id):
        super().__init__(root)
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

        self.create_tab_1()  # создаем все табы, оно у меня не заработало на классах, поэтому все в таск запихну
        self.create_last_tab()

    def setup_tab_styles(self):
        # Создаем общий стиль для всех вкладок с цветами
        self.style.configure('TNotebook.Tab',
                             padding=[15, 5],
                             background='lightblue')  # общий цвет для всех вкладок

    def create_tab_1(self):#создание содержимого
            exercises1 = ["какая-то задача из первого", "другая задача из первого", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
            answer1=[]
            for i in range(2):
                tab = ttk.Frame(self.notebook)

                self.notebook.add(tab, text={i + 1})

                zadanie_frame = ttk.Frame(tab)
                zadanie_frame.pack(fill='both', expand=True, padx=10, pady=10)

                gp = Task()#я постарался разобраться как фуекцию вызвать чтоб фото взять, че-то сделал
                zadanie = gp.get_photo()
                image_label = ttk.Label(zadanie_frame, image=zadanie)
                image_label.pack()

                answer_frame = ttk.Frame(tab)
                answer_frame.pack(fill='x', padx=10, pady=10)

                otvet_ukaz = ttk.Label(answer_frame, text="Ответ:", font=('Arial', 12))  # "Ответ:"
                otvet_ukaz.pack(side='left', padx=(0, 10))

                answer = ttk.Entry(answer_frame, font=('Arial', 12), width=40)  # поле ввода ответа
                answer.pack(side='left', fill='x', expand=True, padx=(0, 10))

                otvet = ttk.Button(answer_frame, text="Ответить",
                                   command=lambda idx=i, ans=answer: self.get_answer1(idx, ans))  # ответ
                otvet.pack(side='right')
    def get_answer1(self, task_index, answer):#получаем отвтет
        user_answer = answer.get()

        if not user_answer:
            # result_label.config(text="Введите ответ!")
            return
        answers[0].append(user_answer)

    def create_last_tab(self):
        tab = ttk.Frame(self.notebook)

        self.notebook.add(tab, text="Закончить")

        last_frame = ttk.Frame(tab)
        last_frame.pack(fill='both', expand=True, padx=10, pady=10)

        #zaver=ttk.Button(last_frame, text="Хотите закончить?", command=lambda: self.show_tocho())
        #zaver.pack(side='left', padx=(0, 10))



# root = tk.Tk()
# app = ex1Notebook(root)
# root.mainloop()

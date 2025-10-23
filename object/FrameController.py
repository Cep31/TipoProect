import random
from tkinter import *
from tkinter import ttk

from window.FinishPage import FinishPage
from window.MainPage import MainPage
from window.TaskPage import TaskPage

class FrameController:
    def __init__(self, root: Tk):
        self.root = root

        self.tasks = [] # Здесь хранятся ID

        self.main_page = MainPage(self.root, self)
        self.main_page.pack()

        self.tasks = []
        self.tasks_nb = ttk.Notebook(root)
        self.finish_page = FinishPage(self)

    def generate_problems_on_click(self):
        tasks_count = self.main_page.get_tasks_count()
        counter = 1

        for type_task in tasks_count:
            for i in range(type_task):
                id = f'{(type_task + 1):02}_{random.randint(1, 1):02}_{random.randint(1, 1):03}'
                task = TaskPage(self.tasks_nb, self, id)
                self.tasks.append(task)
                self.tasks_nb.add(task, text=str(counter))
                counter += 1

        last_tab = ttk.Frame(self.tasks_nb)

        self.tasks_nb.add(last_tab, text="Закончить")

        last_frame = ttk.Frame(last_tab)
        last_frame.pack(fill='both', expand=True, padx=10, pady=10)

        zaver = ttk.Button(last_frame, text="Хотите закончить?", command=self.finish_page.show)
        zaver.pack(side='left', padx=(0, 10))

        self.show_tasks()

    def rate_all(self):
        for i in self.tasks:
            i.rate()

    def show_main(self):
        self.tasks_nb.pack_forget()
        self.root.geometry("410x900")
        self.main_page.pack()

    def show_tasks(self):
        self.main_page.pack_forget()
        self.root.geometry("800x1200")
        self.tasks_nb.pack(fill='both', expand=True, padx=10, pady=10)

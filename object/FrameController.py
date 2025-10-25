import random
from tkinter import *
from tkinter import ttk

from object.ScrollableNotebook import ScrollableNotebook
from window.DetailedTaskPage import DetailedTaskPage
from window.FinishPage import FinishPage
from window.MainPage import MainPage
from window.TestTaskPage import TestTaskPage
from object.Task import Task

class FrameController:
    def __init__(self, root: Tk):
        self.root = root

        self.main_page = MainPage(self.root, self)
        self.main_page.pack()

        self.tasks = []
        self.tasks_nb = ScrollableNotebook(root, visible_tabs=15)
        self.finish_page = FinishPage(self)

    def generate_problems_on_click(self):
        tasks_count = self.main_page.get_tasks_count()
        counter = 1
        tasks_id = []

        for i in range(len(tasks_count)):
            for j in range(tasks_count[i]):
                task_id = f'{(i + 1):02}_{random.randint(1, 1):02}_{random.randint(1, 1):03}'
                while task_id in tasks_id:
                    task_id = f'{(i + 1):02}_{random.randint(1, 1):02}_{random.randint(1, 999):03}'
                tasks_id.append(task_id)

                task = Task(task_id)
                if task.get_type() == "test":
                    task_page = TestTaskPage(self.tasks_nb, self, id)
                elif task.get_type() == "detailed":
                    task_page = DetailedTaskPage(self.tasks_nb, self, id)
                else:
                    raise EXCEPTION
                self.tasks.append(task_page)
                self.tasks_nb.add(task_page, text=str(counter))
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
        self.root.geometry("410x950")
        self.main_page.pack()

    def show_tasks(self):
        self.main_page.pack_forget()
        self.root.geometry("800x1000")
        self.tasks_nb.pack(fill='both', expand=True, padx=10, pady=10)

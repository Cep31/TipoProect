import random
from tkinter import *
from tkinter import ttk

from object.ScrollableNotebook import ScrollableNotebook
from window.DetailedTaskPage import DetailedTaskPage
from window.FinishPage import FinishPage
from window.MainPage import MainPage
from window.TaskPage import TaskPage
from object.Task import Task

class FrameController:
    def __init__(self, root: Tk):
        self.root = root

        self.main_page = MainPage(root, self)
        self.task_page = TaskPage(root, self)

        self.show_main()

    def generate_problems_on_click(self):
        tasks_count = self.main_page.get_tasks_count()
        tasks_id = []

        for i in range(len(tasks_count)):
            for j in range(tasks_count[i]):
                task_id = f'{(i + 1):02}_{random.randint(1, 1):02}_{random.randint(1, 3):03}'
                while task_id in tasks_id:
                   task_id = f'{(i + 1):02}_{random.randint(1, 1):02}_{random.randint(1, 3):03}'
                tasks_id.append(task_id)
                self.task_page.add_tab(Task(task_id))
        self.task_page.add_finish_tab()

        self.show_tasks()

    def rate(self):
        self.task_page.rate()

    def show_main(self):
        self.task_page.pack_forget()
        self.root.geometry("410x950")
        self.main_page.pack()

    def show_tasks(self):
        self.main_page.pack_forget()
        self.root.geometry("800x1000")
        self.task_page.pack(fill='both', expand=True, padx=10, pady=10)

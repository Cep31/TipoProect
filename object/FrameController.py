import random
from tkinter import *
from window.MainPage import MainPage
from window.TaskPage import TaskPage

class FrameHandler:
    def __init__(self, root: Tk):
        self.root = root

        self.tasks = [] # Здесь хранятся ID

        self.task_page: TaskPage
        self.main_page = MainPage(self.root, self)
        self.main_page.pack()

    def generate_problems_on_click(self):
        tasks_count = self.main_page.get_tasks_count()

        for type_task in tasks_count:
            for i in range(type_task):
                id = f'{(type_task + 1):02}_{random.randint(1, 1):02}_{random.randint(1, 1):03}'
                self.tasks.append(id)

        for i in self.tasks:
            print(i)
        self.task_page = TaskPage(self.root, self, self.tasks)
        self.main_page.pack_forget()

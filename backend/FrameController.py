import random
from tkinter import *
from tkinter import ttk

from constants import MAX_VARIANT
from backend.ScrollableNotebook import ScrollableNotebook
from pages.DetailedTaskPage import DetailedTaskPage
from pages.FinishPage import FinishPage
from pages.MainPage import MainPage
from pages.TaskPage import TaskPage
from backend.Task import Task

class FrameController:
    def __init__(self, root: Tk):
        self.root = root

        self.main_page = MainPage(root, self)
        self.task_page = TaskPage(root, self)

        self.show_main()

    # генерация заданий
    def generate_problems_on_click(self):
        tasks_count = self.main_page.get_tasks_count()

        for i in range(len(tasks_count)):
            task_numbers = random.choices(list(range(1, MAX_VARIANT+1)), k=tasks_count[i])
            for task_number in task_numbers:
                task = Task(i+1, 1, task_number)

                # добавление задания на след страницу
                self.task_page.add_tab(task)

        # финальный tab на след страницу
        self.task_page.add_finish_tab()
        self.show_tasks()

    def root_resize(self, width, height):
        self.root.geometry(f"{width}x{height}")

    def show_main(self):
        self.task_page.pack_forget()
        self.root_resize(550, 820)
        self.main_page.pack()

    def show_tasks(self):
        self.main_page.pack_forget()
        self.root_resize(1000, 1000)
        self.task_page.pack(fill='both', expand=True, padx=10, pady=10)

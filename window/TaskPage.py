import customtkinter as ctk

from front.DetailedTab import DetailedTab
from front.TestTab import TestTab
from object.ScrollableNotebook import ScrollableNotebook
from object.Task import Task

class TaskPage(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root

        self.tasks = []
        self.controller = controller

        self.tasks_notebook = ScrollableNotebook(self, visible_tabs=15)
        self.tasks_notebook.pack(fill='both', expand=True, padx=10, pady=10)
        self.tabs = []
        self.counter = 1

    def add_tab(self, task: Task):
        if task.get_type() == "task":
            tab = TestTab(self.root, task)
        elif task.get_type() == "detailed":
            tab = DetailedTab(self.root, task)
        else:
            tab = TestTab(self.root, Task("01_01_001"))

        self.tabs.append(tab)
        self.tasks_notebook.add(tab, text=str(self.counter))
        self.counter += 1



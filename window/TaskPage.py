import customtkinter as ctk
from tkinter import ttk

from front.DetailedTab import DetailedTab
from front.RatedTestTab import RatedTestTab
from front.TestTab import TestTab
from object.ScrollableNotebook import ScrollableNotebook
from object.Task import Task


class TaskPage(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root

        self.tasks = []
        self.controller = controller

        style = ttk.Style()
        style.configure("Custom.TNotebook.Tab", padding=[30, 10])

        self.tasks_notebook = ScrollableNotebook(self, visible_tabs=15, style="Custom.TNotebook")
        self.tasks_notebook.pack(fill='both', expand=True, padx=10, pady=10)
        self.tabs = []
        self.counter = 1



    def add_tab(self, task: Task):
        if task.get_type() == "test":
            tab = TestTab(self.root, task)
        elif task.get_type() == "detailed":
            tab = DetailedTab(self.root, task)
        else:
            tab = TestTab(self.root, Task("01_01_001"))


        self.tabs.append(tab)
        self.tasks_notebook.add(tab, text=str(self.counter))
        self.counter += 1

    def add_finish_tab(self):
        tab = ctk.CTkFrame(self.root) # сюда суй таб "завершить"
        text = ctk.CTkLabel(tab, text="АБАБАБАБ")
        text.pack()

        finish = ctk.CTkButton(
            tab,
            text="Завершить",
            font=ctk.CTkFont(size=12, weight="bold"),
            height=35,
            width=100,
            fg_color=("#3B8ED0", "#1F6AA5"),
            hover_color=("#36719F", "#144870"),
            command=lambda: self.rate()
        )
        finish.pack(padx=(5, 5), pady=10)  # кнопка "Ответить"

        self.tasks_notebook.add(tab, text="завершить")

    def rate(self):
        self.tasks_notebook.pack_forget()
        self.tasks_notebook = ScrollableNotebook(self, visible_tabs=15, style="Custom.TNotebook")
        self.tasks_notebook.pack(fill='both', expand=True, padx=10, pady=10)

        for i in range(len(self.tabs)):
            answer = self.tabs[i].get_answer()
            task = self.tabs[i].task
            self.tabs[i] = RatedTestTab(self.root, task, answer)
            self.tasks_notebook.add(self.tabs[i], text=str(i+1))

import customtkinter as ctk
from tkinter import ttk

from front.FinalPage import FinalPage
from front.DetailedTab import DetailedTab
from front.RatedDetailedTab import RatedDetailedTab
from front.RatedTestTab import RatedTestTab
from front.TestTab import TestTab
from object.ScrollableNotebook import ScrollableNotebook
from object.Task import Task


class TaskPage(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.root = root

        self.controller = controller

        style = ttk.Style()
        style.configure("Custom.TNotebook.Tab", padding=[30, 10])

        self.tasks_notebook = ScrollableNotebook(self, visible_tabs=15, style="Custom.TNotebook")
        self.tasks_notebook.pack(fill='both', expand=True, padx=10, pady=10)
        self.tabs = []
        self.counter = 1
        self.scores = []

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
        text = """
        Вы заканчиваете решать вариант
        Все ваши ответы сохранены, в том числе и вторая часть
        Вернутся к решению варианта вы больше НЕ СМОЖЕТЕ
        Вы уверены, что вы хотите завершить?
        """
        text = ctk.CTkLabel(tab, text=text, pady=20, font=ctk.CTkFont(size=30, weight="bold"))
        text.pack()

        finish = ctk.CTkButton(
            tab,
            text="Завершить",
            font=ctk.CTkFont(size=25, weight="bold"),
            height=75,
            width=200,
            fg_color=("#3B8ED0", "#1F6AA5"),
            hover_color=("#36719F", "#144870"),
            command=lambda: self.rate()
        )
        finish.pack(padx=(5, 5), pady=10)  # кнопка "Ответить"

        self.tasks_notebook.add(tab, text="Завершить")

    def add_rate_tab(self):
        max_scores = []
        for i in self.tabs:
            max_scores.append(i.task.get_max_mark())

        tab = FinalPage(self, self.scores, max_scores)
        self.tasks_notebook.add(tab, text="Результат")

    def rate(self):
        self.controller.root_resize(1000, 800)

        self.tasks_notebook.pack_forget()
        self.tasks_notebook = ScrollableNotebook(self, visible_tabs=15, style="Custom.TNotebook")
        self.tasks_notebook.pack(fill='both', expand=True, padx=10, pady=10)

        for i in range(len(self.tabs)):
            tab = self.tabs[i]
            answer = tab.get_answer()
            task = tab.task
            if tab.task.get_type() == "test":
                self.tabs[i] = RatedTestTab(self.root, task, answer)
            elif tab.task.get_type() == "detailed":
                self.tabs[i] = RatedDetailedTab(self.root, task, answer)

            self.scores.append(self.tabs[i].score)

            self.tasks_notebook.add(self.tabs[i], text=str(i + 1))

        self.add_rate_tab()

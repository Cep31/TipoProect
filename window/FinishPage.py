from tkinter import *
from tkinter.ttk import *

class FinishPage:
    def __init__(self, controller):
        self.window: Tk
        self.controller = controller

    def show(self):
        self.window = Tk()
        self.window.title = "Вы уверены?"
        self.window.geometry("200x300")

        frame = Frame(self.window)
        frame.pack(fill='both', expand=True, padx=10, pady=10)

        label = Label(frame, text="Вы точно хотите завершить?", font=('Arial', 12))
        label.pack(side='top', padx=(0, 10))

        finish = Button(frame, text="завершить", command=self.finish)#уничтожить страницу в которой задания и создать с решениями
        finish.pack(side='right', padx=10, pady=10)

        not_finish = Button(frame, text="подумаю еще", command=self.window.destroy)#уничтожить страницу в которой задания и создать с решениями
        not_finish.pack(side='left', padx=10, pady=10)

    def finish(self):
        self.controller.rate_all()
        self.window.destroy()
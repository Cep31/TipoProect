import customtkinter as ctk
from PIL import Image
from backend.Task import Task


class TestTab(ctk.CTkFrame):
    def __init__(self, parent, task: Task):
        super().__init__(parent, corner_radius=10, fg_color="transparent")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.task = task

        self.create_tab_ex1()

    def create_tab_ex1(self):
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.zadanie_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.zadanie_frame.pack(fill='both', expand=True, pady=(0, 10))

        self.task_image = ctk.CTkLabel(
            self.zadanie_frame,
            text="Фото не найдено",
            font=ctk.CTkFont(size=14),
            text_color=("gray50", "gray70"),
            fg_color=("gray85", "gray25"), corner_radius=8, height=200
        )
        self.task_image.pack(fill='both', expand=True, padx=20, pady=10)
        self.load_image()
        self.task_image.configure(state='disabled')

        self.answer_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.answer_frame.pack(fill='x', padx=10, pady=10)

        self.otvet_ukaz = ctk.CTkLabel(self.answer_frame, text="Ответ:", font=ctk.CTkFont(size=12, weight="bold"), width=60)#Ответ:
        self.otvet_ukaz.pack(side='left', padx=(10, 5), pady=10)#Ответ:

        self.answer = ctk.CTkEntry(self.answer_frame, font=ctk.CTkFont(size=12), placeholder_text="Введите ваш ответ...", height=35)
        self.answer.pack(side='left', fill='x', expand=True, padx=5, pady=10)#поле ввода ответа

    def load_image(self):
        path = self.task.get_path()
        image = Image.open(path)
        image.thumbnail((1000, 9999), Image.Resampling.LANCZOS)

        ctk_image = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=image.size
        )
        self.task_image.configure(image=ctk_image, text="", fg_color="transparent")

    def get_answer(self):
        answer = self.answer.get()
        if answer == '':
            return None
        return answer

# root = ctk.CTk()
# root.title("Задача №1")
# root.geometry("800x1200")
#
# app = TaskPage1(root)
# app.pack(fill='both', expand=True, padx=10, pady=10)
#
# root.mainloop()
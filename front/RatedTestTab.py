import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage

from object.Task import Task


class RatedTestTab(ctk.CTkFrame):
    def __init__(self, root, task: Task, answer):
        super().__init__(root)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.answer = answer
        self.score = task.rate(answer)
        self.task = task

        self.current_task_index = 0
        self.current_image = None

        self.create_tab_1()

    def create_tab_1(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        image_frame = ctk.CTkFrame(main_frame)
        image_frame.pack(side="left", fill="both", expand=True)

        self.task_image = ctk.CTkLabel(
            image_frame,
            text="Фото не найдено",
            font=ctk.CTkFont(size=14),
            text_color=("gray50", "gray70"),
            fg_color=("gray85", "gray25"), corner_radius=8, height=200
        )
        self.task_image.pack(fill='both', expand=True, padx=20, pady=10)
        self.load_image()
        self.task_image.configure(state='disabled')

        AI_frame = ctk.CTkFrame(main_frame)
        AI_frame.pack(side="right", fill="both", expand=True, padx=(5,5))

        self.answer_task = ctk.CTkLabel(
            AI_frame,
            text="Фото не найдено",
            font=ctk.CTkFont(size=14),
            text_color=("gray50", "gray70"),
            fg_color=("gray85", "gray25"),
            corner_radius=8,
            height=200
        )
        self.load_image_explanation()
        self.answer_task.pack(fill="both", expand=True, pady=10)
        self.answer_task.configure(state="disabled")

        itog_frame = ctk.CTkFrame(image_frame, height=80)#выделяем итоговый фрейм
        itog_frame.pack(side="bottom", fill="x", padx=(10, 10), pady=10)

        answer_frame = ctk.CTkFrame(itog_frame, fg_color="transparent")
        answer_frame.pack(side="left", padx=20, pady=10)

        ctk.CTkLabel(answer_frame, text=f"Ваш ответ:   {self.answer}", font=ctk.CTkFont(size=10, weight="bold")).pack(anchor="w")#ответ пользователя

        score_frame = ctk.CTkFrame(itog_frame, fg_color="transparent")
        score_frame.pack(side="right", padx=20, pady=5)

        ctk.CTkLabel(score_frame, text=f"Ваши баллы за это задание:   {self.score}/{self.task.get_max_mark()}", font=ctk.CTkFont(size=10, weight="bold")).pack(side="left", padx = 20, pady = 10)#баллы за задание

    def load_image_explanation(self):
        path = self.task.get_explanation_path()
        image = Image.open(path)
        image.thumbnail((400, 300), Image.Resampling.LANCZOS)

        ctk_image = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=image.size
        )
        self.answer_task.configure(image=ctk_image, text="", fg_color="transparent")

    def load_image(self):
        path = self.task.get_path()
        image = Image.open(path)
        image.thumbnail((400, 300), Image.Resampling.LANCZOS)

        ctk_image = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=image.size
        )
        self.task_image.configure(image=ctk_image, text="", fg_color="transparent")

# root = ctk.CTk()
# root.geometry("800x1000")
#
# app = RatedTestTab(-1, 2, Task("01_01_001"), root)
# root.mainloop()
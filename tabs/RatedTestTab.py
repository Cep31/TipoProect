import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage

from backend.Task import Task


class RatedTestTab(ctk.CTkFrame):
    def __init__(self, root, task: Task, answer):
        super().__init__(root)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.answer = answer
        self.score = task.rate_test(answer)
        self.task = task

        self.current_task_index = 0
        self.current_image = None

        self.create_tab_1()

    def create_tab_1(self):
        # Основной фрейм
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Фрейм с заданием
        task_card = ctk.CTkFrame(
            main_container,
            fg_color=("gray90", "gray15"),
            corner_radius=12,
            border_width=1,
            border_color=("gray70", "gray30")
        )
        task_card.pack(fill="both", expand=True, pady=(0, 15))

        # Заголовок задание
        ctk.CTkLabel(
            task_card,
            text=f"Задание №{self.task.first_type}",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=("gray20", "gray80")
        ).pack(anchor="w", padx=20, pady=(15, 5))

        # Фрейм с условием и решением
        content_container = ctk.CTkFrame(task_card, fg_color="transparent")
        content_container.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Левый фрейм с условием
        condition_frame = ctk.CTkFrame(
            content_container,
            fg_color=("gray95", "gray10"),
            corner_radius=10,
            border_width=1,
            border_color=("gray85", "gray20")
        )
        condition_frame.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

        # условие
        ctk.CTkLabel(
            condition_frame,
            text="Условие",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("gray40", "gray60")
        ).pack(anchor="w", padx=15, pady=(15, 10))
        # Изображение условия
        self.task_image = ctk.CTkLabel(
            condition_frame,
            text="Фото не найдено",
            font=ctk.CTkFont(size=13),
            fg_color=("gray85", "gray25"),
            corner_radius=8,
            height=200
        )
        self.task_image.pack(padx=15, pady=(0, 15), fill="both", expand=True)
        self.load_image()
        self.task_image.configure(state='disabled')

        # Правый фрейм решения
        solution_frame = ctk.CTkFrame(
            content_container,
            fg_color=("gray95", "gray10"),
            corner_radius=10,
            border_width=1,
            border_color=("gray85", "gray20")
        )
        solution_frame.pack(side="right", fill="both", expand=True, padx=(10, 0), pady=10)

        # Заголовок решения
        solution_header = ctk.CTkFrame(solution_frame, fg_color="transparent")
        solution_header.pack(fill="x", padx=15, pady=(15, 10))

        ctk.CTkLabel(
            solution_header,
            text="Решение",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("gray40", "gray60")
        ).pack(side="left")

        # Индикатор статуса
        self.status_label = ctk.CTkLabel(
            solution_header,
            text="• Проверено",
            font=ctk.CTkFont(size=12),
            text_color="#27AE60"
        )
        self.status_label.pack(side="right")

        # Изображение решения
        self.answer_task = ctk.CTkLabel(
            solution_frame,
            text="Фото не найдено",
            font=ctk.CTkFont(size=13),
            fg_color=("gray85", "gray25"),
            corner_radius=8,
            height=150
        )
        self.answer_task.pack(padx=15, pady=(0, 15), fill="both", expand=True)
        self.load_image_explanation()
        self.answer_task.configure(state="disabled")
        # Фрейм снизу с ответом пользователя и баллами
        bottom_panel = ctk.CTkFrame(
            main_container,
            fg_color=("gray90", "gray15"),
            corner_radius=12,
            border_width=1,
            border_color=("gray70", "gray30")
        )
        bottom_panel.pack(fill="x", pady=(10, 0))

        bottom_content = ctk.CTkFrame(bottom_panel, fg_color="transparent")
        bottom_content.pack(fill="both", expand=True, padx=20, pady=15)

        # Разделяем на левую и правую части
        bottom_content.grid_columnconfigure(0, weight=1)
        bottom_content.grid_columnconfigure(1, weight=0)

        # Ваш ответ
        answer_frame = ctk.CTkFrame(bottom_content, fg_color="transparent")
        answer_frame.grid(row=0, column=0, sticky="w")


        ctk.CTkLabel(
            answer_frame,
            text=f"Ваш ответ: {self.answer}",
            font=ctk.CTkFont(size=15, weight="normal"),
            text_color=("gray20", "gray80")
        ).pack(side="left")

        ctk.CTkLabel(
            answer_frame,
            text=f"Правильный ответ: {self.task.get_right_answer()}",
            font=ctk.CTkFont(size=15, weight="normal"),
            text_color=("gray20", "gray80")
        ).pack(side="right", anchor="e", padx=50)

        # Баллы за задание
        score_frame = ctk.CTkFrame(bottom_content, fg_color="transparent")
        score_frame.grid(row=0, column=1, sticky="e")

        max_mark = self.task.get_max_mark()
        progress = self.score / max(max_mark, 1)

        # Цвет баллов в зависимости от результата
        score_color = "#27AE60" if progress >= 0.5 else "#E74C3C"


        score_container = ctk.CTkFrame(score_frame, fg_color="transparent")
        score_container.pack()

        ctk.CTkLabel(
            score_container,
            text="Баллы за это задание:",
            font=ctk.CTkFont(size=14),
            text_color=("gray50", "gray50")
        ).pack(side="left", padx=(0, 5))

        self.score_label = ctk.CTkLabel(
            score_container,
            text=f"{self.score}/{max_mark}",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=score_color
        )
        self.score_label.pack(side="left")

    def load_image_explanation(self):
        try:
            path = self.task.get_explanation_path()
            if path and path != "Ошибка загрузки изображения":
                image = Image.open(path)

                # Оптимизация размера изображения (уменьшенный максимальный размер)
                max_width, max_height = 350, 400  # Уменьшенные размеры
                width, height = image.size

                if width > max_width or height > max_height:
                    ratio = min(max_width / width, max_height / height)
                    new_size = (int(width * ratio), int(height * ratio))
                    image = image.resize(new_size, Image.Resampling.LANCZOS)

                ctk_image = ctk.CTkImage(
                    light_image=image,
                    dark_image=image,
                    size=image.size
                )
                self.answer_task.configure(image=ctk_image, text="", fg_color="transparent")
            else:
                self.answer_task.configure(text="Ошибка загрузки изображения", fg_color=("gray85", "gray25"))
        except Exception as e:
            self.answer_task.configure(
                text=f"Ошибка загрузки изображения\n{str(e)}",
                font=ctk.CTkFont(size=12),
                text_color="#E74C3C",
                fg_color=("gray85", "gray25")
            )

    def load_image(self):
        try:
            path = self.task.get_path()
            if path and path != "Ошибка загрузки изображения":
                image = Image.open(path)

                # изменение размера изображения
                max_width, max_height = 450, 500
                width, height = image.size

                if width > max_width or height > max_height:
                    ratio = min(max_width / width, max_height / height)
                    new_size = (int(width * ratio), int(height * ratio))
                    image = image.resize(new_size, Image.Resampling.LANCZOS)

                ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=image.size)
                self.task_image.configure(image=ctk_image, text="", fg_color="transparent")
            else:
                self.task_image.configure(
                    text="Ошибка загрузки изображения",
                    fg_color=("gray85", "gray25"))
        except Exception as e:
            self.task_image.configure(
                text=f"Ошибка загрузки\n{str(e)}",
                font=ctk.CTkFont(size=12),
                text_color="#E74C3C",
                fg_color=("gray85", "gray25"))
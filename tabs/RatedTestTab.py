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
        self.max_score = self.task.get_max_mark()

        self.current_task_index = 0
        self.current_image = None

        self.create_tab_1()

    def create_tab_1(self):
        # Основной контейнер
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=10, pady=10)

        # Заголовок задания
        header_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        header_frame.pack(fill="x", pady=(0, 10))

        # Блок с условием и решением
        content_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        content_frame.pack(fill="both", expand=True)

        # Левая панель - Условие задачи
        condition_frame = ctk.CTkFrame(content_frame, corner_radius=10)
        condition_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

        ctk.CTkLabel(
            condition_frame,
            text="Условие задачи:",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("gray70", "gray30")
        ).pack(anchor="w", padx=15, pady=(10, 5))

        # Изображение задания
        self.task_image = ctk.CTkLabel(
            condition_frame,
            text="Изображение условия",
            font=ctk.CTkFont(size=12),
            text_color=("gray50", "gray70"),
            fg_color=("gray90", "gray20"),
            corner_radius=8,
            height=180
        )
        self.task_image.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        self.load_image()

        # Правая панель - Ответ
        answer_frame = ctk.CTkFrame(content_frame, corner_radius=10)
        answer_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

        ctk.CTkLabel(
            answer_frame,
            text="Ответ",
            font=ctk.CTkFont(size=14, weight="bold"),
            text_color=("gray70", "gray30")
        ).pack(anchor="w", padx=15, pady=(10, 5))

        # Изображение решения
        self.answer_task = ctk.CTkLabel(
            answer_frame,
            text="Изображение решения",
            font=ctk.CTkFont(size=12),
            text_color=("gray50", "gray70"),
            fg_color=("gray90", "gray20"),
            corner_radius=8,
            height=100
        )
        self.answer_task.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        self.load_image_explanation()

        # Нижняя панель с информацией
        bottom_panel = ctk.CTkFrame(main_container, fg_color=("gray95", "gray15"), corner_radius=8)
        bottom_panel.pack(fill="x", pady=(10, 0))

        # Левая часть - максимальный балл
        left_info = ctk.CTkFrame(bottom_panel, fg_color="transparent")
        left_info.pack(side="left", padx=20, pady=10)

        ctk.CTkLabel(
            left_info,
            text=f"Максимальный балл: {self.max_score}",
            font=ctk.CTkFont(size=12, weight="bold")
        ).pack(anchor="w")

        # Центральная часть - ответ пользователя
        center_info = ctk.CTkFrame(bottom_panel, fg_color="transparent")
        center_info.pack(side="left", padx=40, pady=10)

        ctk.CTkLabel(
            center_info,
            text=f"Ваш ответ: {self.answer}",
            font=ctk.CTkFont(size=12, weight="bold")
        ).pack(anchor="w")

        # Правая часть - полученные баллы
        right_info = ctk.CTkFrame(bottom_panel, fg_color="transparent")
        right_info.pack(side="right", padx=20, pady=10)

        ctk.CTkLabel(
            right_info,
            text=f"Баллы: {self.score}/{self.max_score}",
            font=ctk.CTkFont(size=12, weight="bold")
        ).pack(anchor="e")

        # Панель кнопок
        button_frame = ctk.CTkFrame(main_container, fg_color="transparent")
        button_frame.pack(fill="x", pady=(15, 5))

        # Левая кнопка
        prev_button = ctk.CTkButton(
            button_frame,
            text="Предыдущее задание",
            font=ctk.CTkFont(size=12),
            height=32,
            corner_radius=6
        )
        prev_button.pack(side="left", padx=(0, 10))

    def load_image_explanation(self):
        try:
            path = self.task.get_explanation_path()
            image = Image.open(path)
            image.thumbnail((300, 9999), Image.Resampling.LANCZOS)

            ctk_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=image.size
            )
            self.answer_task.configure(image=ctk_image, text="", fg_color="transparent")
        except:
            self.answer_task.configure(text="Изображение решения не найдено")


    def load_image(self):
        try:
            path = self.task.get_path()
            image = Image.open(path)
            image.thumbnail((300, 9999), Image.Resampling.LANCZOS)

            ctk_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=image.size
            )
            self.task_image.configure(image=ctk_image, text="", fg_color="transparent")
        except:
            self.task_image.configure(text="Изображение условия не найдено")
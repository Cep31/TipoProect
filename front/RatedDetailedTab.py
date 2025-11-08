import customtkinter as ctk
from PIL import Image

from object.Task import Task


class RatedDetailedTab(ctk.CTkFrame):
    def __init__(self, root, task: Task, answers_paths):
        super().__init__(root)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = root
        self.task = task
        self.answer_text = task.rate_detailed(answers_paths)

        self.create_frame()

    def create_frame(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        content_frame = ctk.CTkFrame(main_frame)  # фрейм с содержимым
        content_frame.pack(fill="both", expand=True, pady=(0, 10))

        # Левая часть - изображение задания
        zadanie_image = ctk.CTkLabel(content_frame, text="изображение задания", font=ctk.CTkFont(size=14),
                                   fg_color=("gray90", "gray20"), corner_radius=8)
        zadanie_image.pack(side="left", fill="both", expand=True, padx=(0, 5), pady=10)

        self.load_image(zadanie_image, self.task.get_path())

        # Правая часть - текстовое окно с ответом
        text_frame = ctk.CTkFrame(content_frame, fg_color=("gray85", "gray25"), corner_radius=8)
        text_frame.pack(side="right", fill="both", expand=True, padx=(5, 0), pady=10)

        # Заголовок текстового окна
        text_title = ctk.CTkLabel(text_frame, text="Ответ:",
                                font=ctk.CTkFont(size=16, weight="bold"))
        text_title.pack(anchor="w", padx=10, pady=(10, 5))

        # Текстовое поле с ответом и скроллбаром
        text_widget = ctk.CTkTextbox(text_frame, wrap="word", font=ctk.CTkFont(size=14),
                                   fg_color=("gray80", "gray30"), border_width=1,
                                   border_color=("gray70", "gray40"), scrollbar_button_color=("gray70", "gray50"),
                                   scrollbar_button_hover_color=("gray60", "gray40"))
        text_widget.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        text_widget.insert("1.0", self.answer_text)
        text_widget.configure(state="disabled")  # делаем текстовое поле только для чтения

        bottom_frame = ctk.CTkFrame(main_frame, height=80)
        bottom_frame.pack(side="bottom", fill="x", pady=10)
        bottom_frame.pack_propagate(False)

        #score_label = ctk.CTkLabel(bottom_frame, text=f"Ваши баллы: {self.score}/{self.max_score}",
        #                         font=ctk.CTkFont(size=16, weight="bold"))
        #score_label.pack(side="left", padx=20, pady=10)  # количество баллов

    def load_image(self, image_label, image_path):
        try:
            image = Image.open(image_path)
            image.thumbnail((450, 9999), Image.Resampling.LANCZOS)
            ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=image.size)
            image_label.configure(image=ctk_image, text="")
        except Exception as e:
            image_label.configure(text="Ошибка загрузки", image="")
import threading

import customtkinter as ctk
from PIL import Image

from front.Appeal import Appeal
from object.Autocheck import check
from object.Task import Task


class RatedDetailedTab(ctk.CTkFrame):
    def __init__(self, root, task: Task, answers_paths):
        super().__init__(root)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = root
        self.task = task
        self.score = 0

        self.create_frame()
        self.thread_answer(task.get_path(), answers_paths)

    def create_frame(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        content_frame = ctk.CTkFrame(main_frame)  # фрейм с содержимым
        content_frame.pack(fill="both", expand=True, pady=(0, 10))

        ctk.CTkLabel(
            content_frame,
            text="Условие",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("gray70", "gray30")
        ).pack(pady=(5, 10))

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
        self.text_widget = ctk.CTkTextbox(text_frame, wrap="word", font=ctk.CTkFont(size=14),
                                   fg_color=("gray80", "gray30"), border_width=1,
                                   border_color=("gray70", "gray40"), scrollbar_button_color=("gray70", "gray50"),
                                   scrollbar_button_hover_color=("gray60", "gray40"))
        self.text_widget.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        self.text_widget.insert("1.0", "")
        self.text_widget.configure(state="disabled")  # делаем текстовое поле только для чтения

        bottom_frame = ctk.CTkFrame(main_frame, height=80)
        bottom_frame.pack(side="bottom", fill="x", pady=10)
        bottom_frame.pack_propagate(False)

        self.score_label = ctk.CTkLabel(
            bottom_frame,
            text=f"Ваши баллы: {self.score}/{self.task.get_max_mark()}",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.score_label.pack(side="left", padx=20, pady=10)

        # кнопка апелляции
        appeal_button = ctk.CTkButton(
            bottom_frame,
            text="Подать апелляцию",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#E74C3C",
            hover_color="#C0392B",
            command=self.open_appeal_window
        )
        appeal_button.pack(side="right", padx=20, pady=10)

    def load_image(self, image_label, image_path):
        try:
            image = Image.open(image_path)
            image.thumbnail((450, 9999), Image.Resampling.LANCZOS)
            ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=image.size)
            image_label.configure(image=ctk_image, text="")
        except Exception as e:
            image_label.configure(text="Ошибка загрузки", image="")

    def thread_answer(self, cond_path, answer_pathes):
        self.text_widget.configure(state="normal")
        self.text_widget.delete("1.0", "end")
        self.text_widget.insert("1.0", "Проверка... Подождите.")
        self.text_widget.configure(state="disabled")

        def worker():
            # отдельный потоке
            answer = check(cond_path, answer_pathes, self.task.get_task_number())
            # возвращаем результат в основной поток
            self.root.after(0, self.display_answer, answer)

        threading.Thread(target=worker, daemon=True).start()

    def display_answer(self, answer):
        self.text_widget.configure(state="normal")
        self.text_widget.delete("1.0", "end")
        self.text_widget.insert("1.0", answer)
        self.text_widget.configure(state="disabled")

    def edit_score(self, score):
        self.score = score
        self.score_label.configure(text=f"Ваши баллы: {score}/{self.task.get_max_mark()}")



    def open_appeal_window(self):
        Appeal(self, self.score, self.task.get_max_mark())

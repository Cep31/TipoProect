import threading

import customtkinter as ctk
from PIL import Image

from tabs.Appeal import Appeal
from backend.Autocheck import check
from backend.Task import Task


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
        # Основной контейнер
        main_container = ctk.CTkFrame(self, fg_color="transparent")
        main_container.pack(fill="both", expand=True, padx=20, pady=20)

        # Картинка с условием
        condition_card = ctk.CTkFrame(
            main_container,
            fg_color=("gray90", "gray15"),
            corner_radius=12,
            border_width=1,
            border_color=("gray70", "gray30")
        )
        condition_card.pack(fill="both", expand=True, pady=(0, 15))

        # Заголовок условия
        ctk.CTkLabel(
            condition_card,
            text=f"Задание №{self.task.number}",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=("gray20", "gray80")
        ).pack(anchor="w", padx=20, pady=(15, 5))

        ctk.CTkLabel(
            condition_card,
            text="Условие",
            font=ctk.CTkFont(size=14, weight="normal"),
            text_color=("gray50", "gray50")
        ).pack(anchor="w", padx=20, pady=(0, 15))

        # Основной контент
        content_container = ctk.CTkFrame(condition_card, fg_color="transparent")
        content_container.pack(fill="both", expand=True, padx=15, pady=(0, 15))

        # Изображение задания
        zadanie_frame = ctk.CTkFrame(
            content_container,
            fg_color=("gray95", "gray10"),
            corner_radius=10,
            border_width=1,
            border_color=("gray85", "gray20")
        )
        zadanie_frame.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=10)

        zadanie_image = ctk.CTkLabel(
            zadanie_frame,
            text="Загрузка изображения...",
            font=ctk.CTkFont(size=13),
            fg_color="transparent",
            corner_radius=10
        )
        zadanie_image.pack(padx=15, pady=15, fill="both", expand=True)

        # Правая часть - ответ
        answer_frame = ctk.CTkFrame(
            content_container,
            fg_color=("gray95", "gray10"),
            corner_radius=10,
            border_width=1,
            border_color=("gray85", "gray20")
        )
        answer_frame.pack(side="right", fill="both", expand=True, padx=(10, 0), pady=10)

        # Заголовок ответа с иконкой
        answer_header = ctk.CTkFrame(answer_frame, fg_color="transparent")
        answer_header.pack(fill="x", padx=15, pady=(15, 10))

        ctk.CTkLabel(
            answer_header,
            text="Ответ",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("gray30", "gray70")
        ).pack(side="left")

        # Индикатор проверки
        self.status_label = ctk.CTkLabel(
            answer_header,
            text="• Проверяется",
            font=ctk.CTkFont(size=12),
            text_color="#F39C12"
        )
        self.status_label.pack(side="right")

        # Текстовое поле с ответом
        self.text_widget = ctk.CTkTextbox(
            answer_frame,
            wrap="word",
            font=ctk.CTkFont(size=14),
            fg_color=("gray85", "gray15"),
            border_width=1,
            border_color=("gray75", "gray25"),
            corner_radius=8,
            scrollbar_button_color=("gray70", "gray50"),
            scrollbar_button_hover_color=("gray60", "gray40")
        )
        self.text_widget.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        self.text_widget.insert("1.0", "Загрузка...")
        self.text_widget.configure(state="disabled", height=200)

        # Нижняя панель с баллами и кнопками
        bottom_panel = ctk.CTkFrame(
            main_container,
            fg_color=("gray90", "gray15"),
            corner_radius=12,
            border_width=1,
            border_color=("gray70", "gray30")
        )
        bottom_panel.pack(fill="x", pady=(10, 0))
        bottom_panel.grid_columnconfigure(1, weight=1)

        # Баллы
        score_frame = ctk.CTkFrame(bottom_panel, fg_color="transparent")
        score_frame.grid(row=0, column=0, padx=20, pady=15, sticky="w")

        ctk.CTkLabel(
            score_frame,
            text="Ваши баллы:",
            font=ctk.CTkFont(size=13),
            text_color=("gray50", "gray50")
        ).pack(anchor="w")

        self.score_label = ctk.CTkLabel(
            score_frame,
            text=f"{self.score}/{self.task.get_max_mark()}",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=("#27AE60", "#2ECC71")
        )
        self.score_label.pack(anchor="w", pady=(5, 0))

# Прогресс-бар
        self.progress_bar = ctk.CTkProgressBar(
            bottom_panel,
            height=6,
            corner_radius=3,
            progress_color="#27AE60",
            fg_color=("gray80", "gray25")
        )
        self.progress_bar.grid(row=0, column=1, padx=30, pady=15, sticky="ew")
        self.progress_bar.set(self.score / max(self.task.get_max_mark(), 1))

        # Кнопка апелляции
        button_frame = ctk.CTkFrame(bottom_panel, fg_color="transparent")
        button_frame.grid(row=0, column=2, padx=20, pady=15, sticky="e")

        self.appeal_button = ctk.CTkButton(
            button_frame,
            text="Подать апелляцию",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#E74C3C",
            hover_color="#C0392B",
            corner_radius=8,
            height=40,
            width=160,
            command=self.open_appeal_window
        )
        self.appeal_button.pack()

        # Загрузка изображения
        self.load_image(zadanie_image, self.task.get_path())

    def load_image(self, image_label, image_path):
        try:
            image = Image.open(image_path)
            # Сохраняем пропорции, но ограничиваем максимальный размер
            max_width, max_height = 550, 600
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
            image_label.configure(image=ctk_image, text="")
        except Exception as e:
            image_label.configure(
                text=f"Ошибка загрузки изображения\n{str(e)}",
                font=ctk.CTkFont(size=10),
                text_color="#E74C3C"
            )

    def thread_answer(self, cond_path, answer_pathes):
        self.text_widget.configure(state="normal")
        self.text_widget.delete("1.0", "end")
        self.text_widget.insert("1.0", "Выполняется проверка задания...")
        self.text_widget.configure(state="disabled")
        self.status_label.configure(text="• Проверяется", text_color="#F39C12")
        #self.appeal_button.configure(state="disabled")

        def worker():
            answer = check(cond_path, answer_pathes, self.task.first_type)
            self.root.after(0, self.display_answer, answer[:-1])

        threading.Thread(target=worker, daemon=True).start()

    def display_answer(self, answer):
        self.text_widget.configure(state="normal")
        self.text_widget.delete("1.0", "end")
        if answer[-1].isdigit():
            self.edit_score(int(answer[-1]))
        else:
            print("Ответ получен в неправильном формате(нет числа баллов в конце сообщения)")

        # Форматирование ответа
        lines = str(answer).split('\n')
        formatted_answer = ""
        for line in lines:
            if line.strip().startswith(('•', '-', '✓', '✗')):
                formatted_answer += f"  {line}\n"
            else:
                formatted_answer += f"{line}\n"

        self.text_widget.insert("1.0", formatted_answer)
        self.text_widget.configure(state="disabled")
        self.status_label.configure(text="• Проверено", text_color="#27AE60")
        #self.appeal_button.configure(state="normal")

    # ИЗМЕНИТЬ КОЛ-ВО БАЛЛОВ ЗА ЗАДАНИЕ
    def edit_score(self, score):
        self.score = score
        max_mark = self.task.get_max_mark()
        self.score_label.configure(text=f"{score}/{max_mark}")

        # Обновляем прогресс-бар
        progress = score / max(max_mark, 1)
        self.progress_bar.set(progress)

        # Меняем цвет прогресс-бара в зависимости от результата
        if progress >= 0.8:
            self.progress_bar.configure(progress_color="#27AE60")
        elif progress >= 0.5:
            self.progress_bar.configure(progress_color="#F39C12")
        else:
            self.progress_bar.configure(progress_color="#E74C3C")



    def open_appeal_window(self):
        Appeal(self, self.score, self.task.get_max_mark())
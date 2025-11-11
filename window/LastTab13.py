import customtkinter as ctk
from PIL import Image


class LastTab13(ctk.CTk):
    def __init__(self, task_number, score, zadanie_image_path, answer_text, max_score):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.task_number = task_number
        self.score = score
        self.zadanie_image_path = zadanie_image_path
        self.answer_text = answer_text
        self.max_score = max_score
        self.appeals = []  # массив для хранения апелляций

        self.title(f"Задание {task_number}")
        self.geometry("800x1200")

        self.create_frame()

    def create_frame(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        content_frame = ctk.CTkFrame(main_frame)  # фрейм с содержимым
        content_frame.pack(fill="both", expand=True, pady=(0, 10))

        # Левая часть - контейнер для условия
        left_container = ctk.CTkFrame(content_frame, fg_color="transparent")
        left_container.pack(side="left", fill="both", expand=True, padx=(0, 5))

        # "Условие"
        condition_label = ctk.CTkLabel(
            left_container,
            text="Условие",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("gray70", "gray30")
        )
        condition_label.pack(pady=(0, 10))

        # Изображение задания
        zadanie_image = ctk.CTkLabel(
            left_container,
            text="изображение задания",
            font=ctk.CTkFont(size=14),
            fg_color=("gray90", "gray20"),
            corner_radius=8
        )
        zadanie_image.pack(fill="both", expand=True, pady=(0, 10))

        if self.zadanie_image_path:
            self.load_image(zadanie_image, self.zadanie_image_path)

        # Правая часть - контейнер для ответа
        right_container = ctk.CTkFrame(content_frame, fg_color="transparent")
        right_container.pack(side="right", fill="both", expand=True, padx=(5, 0))

        # "Ответ"
        answer_label = ctk.CTkLabel(
            right_container,
            text="Ответ от ИИ",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color=("gray70", "gray30")
        )
        answer_label.pack(pady=(0, 10))

        # Текстовое окно с ответом
        text_frame = ctk.CTkFrame(right_container, fg_color=("gray85", "gray25"), corner_radius=8)
        text_frame.pack(fill="both", expand=True, pady=(0, 10))

        # Решение
        text_title = ctk.CTkLabel(
            text_frame,
            text="Решение:",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        text_title.pack(anchor="w", padx=10, pady=(10, 5))

        # Поле с ответом и скроллбаром
        text_widget = ctk.CTkTextbox(
            text_frame,
            wrap="word",
            font=ctk.CTkFont(size=14),
            fg_color=("gray80", "gray30"),
            border_width=1,
            border_color=("gray70", "gray40"),
            scrollbar_button_color=("gray70", "gray50"),
            scrollbar_button_hover_color=("gray60", "gray40")
        )
        text_widget.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        text_widget.insert("1.0", self.answer_text)
        text_widget.configure(state="disabled")  # делаем текстовое поле только для чтения

        bottom_frame = ctk.CTkFrame(main_frame, height=80)
        bottom_frame.pack(side="bottom", fill="x", pady=10)
        bottom_frame.pack_propagate(False)

        # баллы
        score_label = ctk.CTkLabel(
            bottom_frame,
            text=f"Ваши баллы: {self.score}/{self.max_score}",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        score_label.pack(side="left", padx=20, pady=10)

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

    def open_appeal_window(self):  # окно для подачи апелляции
        appeal_window = ctk.CTkToplevel(self)
        appeal_window.title("Подача апелляции")
        appeal_window.geometry("500x300")
        appeal_window.resizable(False, False)
        appeal_window.transient(self)
        appeal_window.grab_set()

        # делаем окно по центру
        appeal_window.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - appeal_window.winfo_width()) // 2
        y = self.winfo_y() + (self.winfo_height() - appeal_window.winfo_height()) // 2
        appeal_window.geometry(f"+{x}+{y}")

        main_appeal_frame = ctk.CTkFrame(appeal_window)
        main_appeal_frame.pack(fill="both", expand=True, padx=20, pady=20)

        instruction_label = ctk.CTkLabel(
            main_appeal_frame,
            text="Если вы не согласны с оценкой, введите баллы,\nкоторые вы заслужили:",
            font=ctk.CTkFont(size=16, weight="bold"),
            justify="center"
        )
        instruction_label.pack(pady=(20, 30))

        input_frame = ctk.CTkFrame(main_appeal_frame, fg_color="transparent")
        input_frame.pack(fill="x", pady=20)

        # Введите баллы
        score_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text=f"Введите баллы (0-{self.max_score})",
            font=ctk.CTkFont(size=14),
            width=200,
            height=35
        )
        score_entry.pack(side="left", padx=(0, 10))

        # кнопка подачи апелляции
        submit_appeal_button = ctk.CTkButton(
            input_frame,
            text="Подать апелляцию",
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="#27AE60",
            hover_color="#219955",
            width=150,
            height=35,
            command=lambda: self.submit_appeal(score_entry.get(), appeal_window)
        )
        submit_appeal_button.pack(side="right")

        current_score_label = ctk.CTkLabel(
            main_appeal_frame,
            text=f"Текущие баллы: {self.score}/{self.max_score}",
            font=ctk.CTkFont(size=14),
            text_color=("gray60", "gray40")
        )
        current_score_label.pack(pady=(20, 0))

        score_entry.focus()

    def submit_appeal(self, appeal_score, appeal_window):  # пробуем принять аппеляцию
        try:
            appeal_score = int(appeal_score)
            if 0 <= appeal_score <= self.max_score:
                appeal_data = {  # сохраняем апелляцию в массив
                    'task_number': self.task_number,
                    'current_score': self.score,
                    'appeal_score': appeal_score,
                    'max_score': self.max_score
                }
                self.appeals.append(appeal_data)

                print(f"Апелляция подана: {appeal_data}")
                print(f"Все апелляции: {self.appeals}")

                appeal_window.destroy()

                self.show_success_message()
            else:
                self.show_error_message(f"Баллы должны быть от 0 до {self.max_score}")
        except ValueError:
            self.show_error_message("Пожалуйста, введите целое число")

    def show_success_message(self):  # сообщение об успешной подаче апелляции
        success_window = ctk.CTkToplevel(self)
        success_window.title("Успешно")
        success_window.geometry("300x150")
        success_window.resizable(False, False)
        success_window.transient(self)
        success_window.grab_set()

        # делаем окно поп центру
        success_window.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - success_window.winfo_width()) // 2
        y = self.winfo_y() + (self.winfo_height() - success_window.winfo_height()) // 2
        success_window.geometry(f"+{x}+{y}")

        ctk.CTkLabel(
            success_window,
            text="Апелляция успешно подана!",
            font=ctk.CTkFont(size=16, weight="bold"),
            text_color="#27AE60"
        ).pack(expand=True, pady=20)

    def show_error_message(self, message):  # если пользователь написал больше макс баллов
        error_window = ctk.CTkToplevel(self)
        error_window.title("Ошибка")
        error_window.geometry("400x150")
        error_window.resizable(False, False)
        error_window.transient(self)
        error_window.grab_set()

        error_window.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - error_window.winfo_width()) // 2
        y = self.winfo_y() + (self.winfo_height() - error_window.winfo_height()) // 2
        error_window.geometry(f"+{x}+{y}")

        ctk.CTkLabel(
            error_window,
            text=message,
            font=ctk.CTkFont(size=14),
            text_color="#E74C3C"
        ).pack(expand=True, pady=20)

        ctk.CTkButton(error_window, text="OK", command=error_window.destroy).pack(pady=10)

    def load_image(self, image_label, image_path):
        try:
            image = Image.open(image_path)
            image.thumbnail((350, 250), Image.Resampling.LANCZOS)
            ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=image.size)
            image_label.configure(image=ctk_image, text="")
        except Exception as e:
            image_label.configure(text="Ошибка загрузки", image="")


task_number = 1
score = 2
zadanie_image_path = ""  # путь к изображению задания
answer_text = """Для решения данного уравнения необходимо применить метод замены переменной.

Пусть t = x², тогда уравнение примет вид:
t² - 5t + 6 = 0

Решаем квадратное уравнение:
D = 25 - 24 = 1
t₁ = (5 + 1)/2 = 3
t₂ = (5 - 1)/2 = 2

Возвращаемся к исходной переменной:
x² = 3 или x² = 2
x = ±√3 или x = ±√2

Ответ: x ∈ {-√3, -√2, √2, √3}"""

max_score = 3

app = LastTab13(task_number, score, zadanie_image_path, answer_text, max_score)
app.mainloop()

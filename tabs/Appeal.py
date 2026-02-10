import customtkinter as ctk
from PIL import Image


class Appeal(ctk.CTkToplevel):
    def __init__(self, root, score, max_score):
        super().__init__(root)
        self.root = root

        self.score = score
        self.max_score = max_score
        self.appeals = []  # массив для хранения апелляций

        self.open_appeal_window()

    def open_appeal_window(self):  # окно для подачи апелляции
        self.title("Подача апелляции")
        self.geometry("500x300")
        self.resizable(False, False)
        self.transient(self.root)
        self.grab_set()

        # делаем окно по центру
        self.update_idletasks()
        x = self.winfo_x() + (self.winfo_width() - self.winfo_width()) // 2
        y = self.winfo_y() + (self.winfo_height() - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")

        main_appeal_frame = ctk.CTkFrame(self)
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
            command=lambda: self.submit_appeal(score_entry.get(), self)
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
                self.root.edit_score(appeal_score)
                self.show_success_message()
                appeal_window.destroy()
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

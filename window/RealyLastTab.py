import customtkinter as ctk


class LastTab:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")

        self.window = ctk.CTk()
        self.window.title("Подтверждение выхода")
        self.window.geometry("800x1000")

        self.create_last_tab()

    def create_last_tab(self):
        self.label = ctk.CTkLabel(
            self.window,
            text="Хотите завершить прямо сейчас?\nВсе ответы, которые вы записали, будут сохранены и проверены",
            font=("Arial", 20, "bold"),
            text_color="#2E8B57",
            justify="center"
        )
        self.label.pack(expand=True)

        self.button = ctk.CTkButton(
            self.window,
            text="Подтвердить",
            command=self.window.destroy,
            font=("Arial", 20, "bold"),
            fg_color="#2E8B57",
            height=60,
            width=300
        )
        self.button.pack(pady=50)

    def run(self):
        self.window.mainloop()

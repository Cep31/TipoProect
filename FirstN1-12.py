import customtkinter as ctk


class TaskPage1(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=10, fg_color="transparent")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_tab_ex1()

    def create_tab_ex1(self):
        main_frame = ctk.CTkFrame(self, corner_radius=15)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        self.zadanie_frame = ctk.CTkFrame(main_frame, corner_radius=10)
        self.zadanie_frame.pack(fill='both', expand=True, pady=(0, 10))

        self.zadanie = ctk.CTkTextbox(self.zadanie_frame, font=ctk.CTkFont(size=12), height=200, wrap='word', scrollbar_button_color=("#3B8ED0", "#1F6AA5"), border_width=1, border_color=("#3E454A", "#949A9F"))
        self.zadanie.pack(fill='both', expand=True, padx=10, pady=10)#фото задания
        self.zadanie.insert('1.0', "фото задания")
        self.zadanie.configure(state='disabled')

        self.answer_frame = ctk.CTkFrame(main_frame, corner_radius=10)
        self.answer_frame.pack(fill='x', padx=10, pady=10)

        self.otvet_ukaz = ctk.CTkLabel(self.answer_frame, text="Ответ:", font=ctk.CTkFont(size=12, weight="bold"), width=60)#Ответ:
        self.otvet_ukaz.pack(side='left', padx=(10, 5), pady=10)#Ответ:

        self.answer = ctk.CTkEntry(self.answer_frame, font=ctk.CTkFont(size=12), placeholder_text="Введите ваш ответ...", height=35)
        self.answer.pack(side='left', fill='x', expand=True, padx=5, pady=10)#поле ввода ответа

        self.otvet = ctk.CTkButton( self.answer_frame, text="Ответить", font=ctk.CTkFont(size=12, weight="bold"), height=35, width=100, fg_color=("#3B8ED0", "#1F6AA5"), hover_color=("#36719F", "#144870"))
        self.otvet.pack(side='right', padx=(5, 10), pady=10)#кнопка "Ответить"
        #надо сделать извлечение с помощью твоего Task

root = ctk.CTk()
root.title("Задача №1")
root.geometry("800x1200")

app = TaskPage1(root)
app.pack(fill='both', expand=True, padx=10, pady=10)

root.mainloop()
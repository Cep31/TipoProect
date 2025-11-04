import customtkinter as ctk

class LastFirstTab(ctk.CTk):
    def __init__(self, tasks, answers, scores):
        super().__init__()

        ctk.set_appearance_mode("dark")#делаем красоту
        ctk.set_default_color_theme("blue")

        self.tasks = tasks
        self.answers = answers
        self.scores = scores

        self.geometry("800x1200")

        self.create_first_tab()

    def create_first_tab(self):
        main_frame = ctk.CTkScrollableFrame(self, corner_radius=10)#фрейм со скролбаром
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        title = ctk.CTkLabel(main_frame, text="Ваш результат:", font=ctk.CTkFont(size=20, weight="bold"))#Ваш результат
        title.pack(pady=(0, 25))

        self.create_task_rows(main_frame)#создаем строки заданий

        separator = ctk.CTkFrame(main_frame, height=3, fg_color=("gray60", "gray40"))#красивый разделитель
        separator.pack(fill="x", pady=25)

        self.create_itog(main_frame)#статистика и итоги

    def create_task_rows(self, parent):#создаем строки с задание ответ результат
        header_frame = ctk.CTkFrame(parent, corner_radius=8, fg_color=("gray70", "gray30"))#аголовки столбцов
        header_frame.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(header_frame, text="№ Задания:",
                     font=ctk.CTkFont(size=14, weight="bold"),
                     width=100).pack(side="left", padx=15, pady=10)

        ctk.CTkLabel(header_frame, text="Ответ",
                     font=ctk.CTkFont(size=14, weight="bold"),
                     width=200).pack(side="left", padx=10, pady=10)

        ctk.CTkLabel(header_frame, text="Баллы за задания",
                     font=ctk.CTkFont(size=14, weight="bold"),
                     width=100).pack(side="right", padx=15, pady=10)

        for i in range(len(self.tasks)):#заполняем строки
            self.create_task_row(parent, i)

    def create_task_row(self, parent, index):#заполнение строк
        row_frame = ctk.CTkFrame(parent, corner_radius=6)
        row_frame.pack(fill="x", pady=2)

        if index % 2 == 0:#делаем супер красоту
            fg_color = ("gray92", "gray18")
        else:
            fg_color = ("gray85", "gray22")

        row_frame.configure(fg_color=fg_color)

        task = ctk.CTkLabel(row_frame, text=f"№ {self.tasks[index]}", font=ctk.CTkFont(size=13, weight="bold"), width=80)
        task.pack(side="left", padx=(15, 10), pady=8)#номер задания, надо решить как сделать так что-бы было понятно и номер задания и столько сколькоэтих заданий

        answer = ctk.CTkLabel(row_frame, text=str(self.answers[index]), font=ctk.CTkFont(size=13), width=180, anchor="w")
        answer.pack(side="left", padx=122, pady=8)#ответ пользователя

        score = self.scores[index]#цветные балы
        if score > 0 and score < 3:
            score_color = "#ebd700"
        elif score == 3:
            score_color = "#28A745"
        else:
            score_color = "#DC3545"

        score = ctk.CTkLabel(row_frame, text=f"{score}   Баллов", font=ctk.CTkFont(size=13, weight="bold"), text_color=score_color, width=60)
        score.pack(side="right",padx = 55, pady=8)


    def create_itog(self, parent):#создает строку с Ваш результат
        itog_frame = ctk.CTkFrame(parent, corner_radius=12)
        itog_frame.pack(fill="x", pady=10)

        total_score = sum(self.scores)
        completed_tasks = sum(1 for score in self.scores if score > 0)
        total_tasks = len(self.scores)

        total_row = ctk.CTkFrame(itog_frame, fg_color="transparent")#создаем строку с итоговыми результатами
        total_row.pack(fill="x", pady=8)

        ctk.CTkLabel(total_row, text="ОБЩИЙ РЕЗУЛЬТАТ:",
                     font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=20)

        ctk.CTkLabel(total_row, text=f"{total_score} баллов",
                     font=ctk.CTkFont(size=16, weight="bold"),
                     text_color="#28A745").pack(side="right", padx=50)


tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
answers = ["OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV", "OTV"]
scores = [0, 3, 1, 3, 2, 0, 1, 2, 3, 1, 0, 0, 1, 0, 3, 0, 3, 1, 3, 2, 0, 1, 2, 3, 1, 0, 0, 1, 0, 3]

app2 = LastFirstTab(tasks, answers, scores)
app2.mainloop()
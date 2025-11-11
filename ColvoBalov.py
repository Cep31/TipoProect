import customtkinter as ctk


class LastFirstTab(ctk.CTk):
    def __init__(self, root, scores, max_scores):
        super().__init__(root)

        ctk.set_appearance_mode("dark") #делаем красоту
        ctk.set_default_color_theme("blue")

        self.scores = scores
        self.max_scores = max_scores#новый массив с максимальными баллами

        self.geometry("800x1200")

        self.create_first_tab()

    def create_first_tab(self):
        main_frame = ctk.CTkScrollableFrame(self, corner_radius=10)#фрейм со скролбаром
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        title = ctk.CTkLabel(main_frame, text="Ваш результат:",
                             font=ctk.CTkFont(size=20, weight="bold"))#Ваш результат
        title.pack(pady=(0, 25))

        self.create_task_rows(main_frame)#создаем строки заданий

        separator = ctk.CTkFrame(main_frame, height=3, fg_color=("gray60", "gray40"))#красивый разделитель
        separator.pack(fill="x", pady=25)

        self.create_itog(main_frame)#статистика и итоги

    def create_task_rows(self, parent):#создаем строки с заданием результат
        header_frame = ctk.CTkFrame(parent, corner_radius=8, fg_color=("gray70", "gray30"))#заголовки столбцов
        header_frame.pack(fill="x", pady=(0, 10))

        ctk.CTkLabel(header_frame, text="Задания:",
                     font=ctk.CTkFont(size=14, weight="bold"),
                     width=100).pack(side="left", padx=15, pady=10)

        ctk.CTkLabel(header_frame, text="Баллы за задания",
                     font=ctk.CTkFont(size=14, weight="bold"),
                     width=200).pack(side="right", padx=15, pady=10)

        for i in range(len(self.scores)):#заполняем строки
            self.create_task_row(parent, i)

    def create_task_row(self, parent, index):#заполнение строк
        row_frame = ctk.CTkFrame(parent, corner_radius=6)
        row_frame.pack(fill="x", pady=2)

        if index % 2 == 0:#делаем супер красоту
            fg_color = ("gray92", "gray18")
        else:
            fg_color = ("gray85", "gray22")

        row_frame.configure(fg_color=fg_color)

        tasks=[]
        for i in range(len(self.scores)):
            tasks.append(i)
        task = ctk.CTkLabel(row_frame, text=f"Задание {tasks[index]+1}", font=ctk.CTkFont(size=13, weight="bold"),
                            width=80)
        task.pack(side="left", padx=(15, 10), pady=8)  # номер задания

        #форматируем баллы в формате "балл / максимальный балл"
        score_text = f"{self.scores[index]} / {self.max_scores[index]}"

        score = self.scores[index]  # цветные баллы
        max_score = self.max_scores[index]

        #определяем цвет в зависимости от процента выполнения
        percentage = score / max_score if max_score > 0 else 0

        if percentage == 1:#максимальный балл
            score_color = "#28A745"
        elif percentage >= 0.5:#больше половины
            score_color = "#ebd700"
        elif percentage > 0:#есть баллы, но меньше половины
            score_color = "#FF9800"
        else:#0 баллов
            score_color = "#DC3545"

        score_label = ctk.CTkLabel(row_frame, text=score_text,
                                   font=ctk.CTkFont(size=13, weight="bold"),
                                   text_color=score_color, width=100)
        score_label.pack(side="right", padx=55, pady=8)

    def create_itog(self, parent):#создает строку с Ваш результат
        itog_frame = ctk.CTkFrame(parent, corner_radius=12)
        itog_frame.pack(fill="x", pady=10)

        total_score = sum(self.scores)
        total_max_score = sum(self.max_scores)
        completed_tasks = sum(1 for score in self.scores if score > 0)
        total_tasks = len(self.scores)

        total_row = ctk.CTkFrame(itog_frame, fg_color="transparent")#создаем строку с итоговыми результатами
        total_row.pack(fill="x", pady=8)

        ctk.CTkLabel(total_row, text="ОБЩИЙ РЕЗУЛЬТАТ:",
                     font=ctk.CTkFont(size=16, weight="bold")).pack(side="left", padx=20)

        #Форматируем общий результат
        total_text = f"{total_score} / {total_max_score} баллов"
        ctk.CTkLabel(total_row, text=total_text,
                     font=ctk.CTkFont(size=16, weight="bold"),
                     text_color="#28A745").pack(side="right", padx=50)


scores = [0, 3, 1, 3, 2, 0, 1, 2, 3, 1, 0, 0, 1, 0, 3, 0, 3, 1, 3, 2, 0, 1, 2, 3, 1, 0, 0, 1, 0, 3]
max_scores = [3, 4, 3, 4, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,
              3]

#app = LastFirstTab(scores, max_scores)
#app.mainloop()


import customtkinter as ctk
from PIL import Image


class LastN1Tab(ctk.CTk):
    def __init__(self, tasks, AI_answer, answers, scores, task_images, max_ex1):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.tasks = tasks
        self.AI_answer = AI_answer
        self.answers = answers
        self.scores = scores
        self.task_images = task_images
        self.max_ex1 = max_ex1

        self.current_task_index = 0
        self.current_image = None

        self.title("Задание №1")
        self.geometry("800x1200")

        self.create_tab_1()

    def create_tab_1(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        image_frame = ctk.CTkFrame(main_frame)
        image_frame.pack(side="left", fill="both", expand=True)

        self.image_ex = ctk.CTkLabel(image_frame, text="Изображение задания", font=ctk.CTkFont(size=14), fg_color=("gray90", "gray20"), corner_radius=8)
        self.image_ex.pack(fill="both", expand=True, padx=10, pady=10)#картинка задания


        AI_frame = ctk.CTkFrame(main_frame)
        AI_frame.pack(side="right", fill="both", expand=True, padx=(5,5))

        self.AI_textbox = ctk.CTkTextbox(AI_frame, wrap="word", font=ctk.CTkFont(size=12), scrollbar_button_color=("#3B8ED0", "#1F6AA5"))
        self.AI_textbox.insert("1.0", self.AI_answer[0])
        self.AI_textbox.pack(fill="both", expand=True, pady=10)
        self.AI_textbox.configure(state="disabled")

        itog_frame = ctk.CTkFrame(image_frame, height=80)#выделяем итоговый фрейм
        itog_frame.pack(side="bottom", fill="x", padx=(10, 10), pady=10)

        answer_frame = ctk.CTkFrame(itog_frame, fg_color="transparent")
        answer_frame.pack(side="left", padx=20, pady=10)

        ctk.CTkLabel(answer_frame, text=f"Ваш ответ:   {answers[0]}", font=ctk.CTkFont(size=20, weight="bold")).pack(anchor="w")#ответ пользователя

        score_frame = ctk.CTkFrame(itog_frame, fg_color="transparent")
        score_frame.pack(side="right", padx=20, pady=5)

        ctk.CTkLabel(score_frame, text=f"Ваши баллы за это задание:   {scores[0]}/{max_ex1}", font=ctk.CTkFont(size=20, weight="bold")).pack(side="left", padx = 20, pady = 10)#баллы за задание


    def load_image(self, image_path):#загружаем изображение и я сразу исправил ошибку если вдруг не загрузится изображение
        try:
            image = Image.open(image_path)
            image.thumbnail((500, 400), Image.Resampling.LANCZOS)

            ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=image.size)

            self.current_image = ctk_image
            self.image_ex.configure(image=self.current_image, text="")

        except Exception as e:
            self.image_ex.configure(text=f"Ошибка загрузки: {str(e)}", image="")


tasks = [1]
AI_answer = ["Тут ответ ИИ на задание"]
answers = ["-1"]
scores = [2]
task_images = [""]#путь к изображению, у меня не заработало
max_ex1 = 3

app = LastN1Tab(tasks, AI_answer, answers, scores, task_images, max_ex1)
app.mainloop()
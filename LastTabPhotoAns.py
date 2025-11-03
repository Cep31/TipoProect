import customtkinter as ctk
from PIL import Image

class LastTabPhoto(ctk.CTk):
    def __init__(self, task_number, score, user_answer, zadanie_image_path, answer_image_path, max_score):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.task_number = task_number
        self.score = score
        self.user_answer = user_answer
        self.zadanie_image_path = zadanie_image_path
        self.answer_image_path = answer_image_path
        self.max_score = max_score

        self.title(f"Задание {task_number}")
        self.geometry("800x1200")

        self.create_frame()

    def create_frame(self):
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        images_frame = ctk.CTkFrame(main_frame)#фрейм с изображениями
        images_frame.pack(fill="both", expand=True, pady=(0, 10))

        zadanie_image = ctk.CTkLabel(images_frame, text="изображение задания", font=ctk.CTkFont(size=14), fg_color=("gray90", "gray20"), corner_radius=8)
        zadanie_image.pack(side="left", fill="both", expand=True, padx=(0, 5), pady=10)#картинка с заданием

        if self.zadanie_image_path:
            self.load_image(zadanie_image, self.zadanie_image_path)

        answer_image = ctk.CTkLabel(images_frame, text="изображение ответа", font=ctk.CTkFont(size=14), fg_color=("gray85", "gray25"), corner_radius=8)
        answer_image.pack(side="right", fill="both", expand=True, padx=(5, 0), pady=10)#картинка с ответом

        if self.answer_image_path:
            self.load_image(answer_image, self.answer_image_path)

        bottom_frame = ctk.CTkFrame(main_frame, height=80)
        bottom_frame.pack(side="bottom", fill="x", pady=10)
        bottom_frame.pack_propagate(False)

        answer_label = ctk.CTkLabel(bottom_frame, text=f"Ответ: {self.user_answer}", font=ctk.CTkFont(size=16, weight="bold"))
        answer_label.pack(side="left", padx=20, pady=10)#ответ пользователя

        score_label = ctk.CTkLabel(bottom_frame, text=f"Баллы: {self.score}/{self.max_score}", font=ctk.CTkFont(size=16, weight="bold"))
        score_label.pack(side="right", padx=20, pady=10)#количество баллов

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
user_answer = "-1"
zadanie_image_path = ""  #путь к изображению задания
answer_image_path = ""  #путь ко второму изображению
max_score = 3

app = LastTabPhoto(task_number, score, user_answer, zadanie_image_path, answer_image_path, max_score)
app.mainloop()
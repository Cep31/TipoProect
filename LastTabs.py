import customtkinter as ctk
from PIL import Image

class LastWindow(ctk.CTk):
    def __init__(self, scores, tasks, AI_answer, task_images, max_ex13):
        super().__init__()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.tasks = tasks
        self.AI_answer = AI_answer
        self.scores = scores
        self.task_images = task_images
        self.max_ex13 = max_ex13

        self.current_task_index = 0
        self.current_image = None

        self.title("LastWindow")
        self.geometry("800x1200")

        self.create_notebook_13()


    def create_notebook_13(self):
        self.notebook = ctk.CTkTabview(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        #цвета
        color_scheme = {
            0: ("#DC3545", "#FFFFFF"),  #красный
            1: ("#FFC107", "#000000"),  #желтый
            2: ("#FFC107", "#000000"),  #желтый
            3: ("#28A745", "#FFFFFF"),  #зеленый
        }

        #создаем и заполняем табы
        for i, score in enumerate(self.scores): #берем индексы и занчения
            tab_name = f"Task {i + 1}"
            tab = self.notebook.add(tab_name)

            bg_color, text_color = color_scheme.get(score)

            tab_button = self.notebook._segmented_button._buttons_dict[tab_name]#настраиваем внешний вид таба
            tab_button.configure(fg_color=bg_color, hover_color=bg_color, text_color=text_color, border_color=bg_color)
            original_configure = tab_button.configure

            def permanent_configure(**kwargs):#запрещаем изменение fg_color и hover_color
                if 'fg_color' in kwargs:
                    kwargs['fg_color'] = bg_color
                if 'hover_color' in kwargs:
                    kwargs['hover_color'] = bg_color
                if 'text_color' in kwargs:
                    kwargs['text_color'] = text_color
                return original_configure(**kwargs)

            tab_button.configure = permanent_configure

            self.create_content_13(tab, i, score, bg_color, text_color)#заполняем табы

    def create_content_13(self, tab, index, score, bg_color, text_color):
        main_frame = ctk.CTkFrame(tab)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        content_frame = ctk.CTkFrame(main_frame, fg_color="transparent")#фрейм для красоты
        content_frame.pack(fill="both", expand=True, pady=(0, 10))

        image_frame = ctk.CTkFrame(content_frame)#фрейм для изображения
        image_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))

        #получаем данные для текущего таба
        task_num = self.tasks[index] if index < len(self.tasks) else index + 1
        AI_answer_text = self.AI_answer[index] if index < len(self.AI_answer) else "ERROR ОШИБКА ПРОВЕРКА, ИЗВИНИТЕ"
        user_score = self.scores[index] if index < len(self.scores) else 0
        image_path = self.task_images[index] if index < len(self.task_images) else None

        image_label = ctk.CTkLabel(image_frame, text=f"Изображение задания {task_num}", font=ctk.CTkFont(size=14), fg_color=("gray90", "gray20"), corner_radius=8)
        image_label.pack(fill="both", expand=True, padx=10, pady=10)#пока не работает изображение это

        #загружаем изображение если есть потом надо сделать error неудалось загрузить изображение, извините
        if image_path:
            self.load_image(image_label, image_path)

        AI_frame = ctk.CTkFrame(content_frame)#фрейм для AI ответа
        AI_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

        AI_textbox = ctk.CTkTextbox(AI_frame, wrap="word", font=ctk.CTkFont(size=12), scrollbar_button_color=("#3B8ED0", "#1F6AA5"))
        AI_textbox.pack(fill="both", expand=True, padx=10, pady=10)#текстовое поле с ответом ИИ
        AI_textbox.insert("1.0", AI_answer_text)
        AI_textbox.configure(state="disabled")

        itog_frame = ctk.CTkFrame(main_frame, height=80)#ответ пользователя и баллы
        itog_frame.pack(side="bottom", fill="x", pady=10)
        itog_frame.pack_propagate(False)

        answer_frame = ctk.CTkFrame(itog_frame, fg_color="transparent")#ответ пользователя
        answer_frame.pack(side="left", padx=20, pady=10)

        score_frame = ctk.CTkFrame(itog_frame, fg_color="transparent")#баллы за задание
        score_frame.pack(padx=(20, 300), pady=10)

        ctk.CTkLabel(score_frame, text=f"Баллы: {user_score}/{self.max_ex13}", font=ctk.CTkFont(size=16, weight="bold"), text_color=self.get_score_color(user_score)).pack(anchor="e")

    def get_score_color(self, score):#возвращает цвет текста в зависимости от баллов
        if score == 0:
            return "#DC3545"  # Красный
        elif score in [1, 2]:
            return "#FFC107"  # Желтый
        elif score >= 3:
            return "#28A745"  # Зеленый

    def load_image(self, image_label, image_path):#ЗАГРУЖАЕМ изображение
        try:
            image = Image.open(image_path)
            image.thumbnail((400, 300), Image.Resampling.LANCZOS)

            ctk_image = ctk.CTkImage(light_image=image,  dark_image=image, size=image.size)

            image_label.configure(image=ctk_image, text="")

        except Exception as e:
            image_label.configure(text=f"Ошибка загрузки: {str(e)}", image="")


#данные для табов 1-12
scores = [0, 1, 2, 3, 3, 2, 1, 0]
tasks = [1, 2, 3, 4, 5, 6, 7, 8]
AI_answer = ["Ответ ИИ 1", "Ответ ИИ 2", "Ответ ИИ 3", "Ответ ИИ 4", "Ответ ИИ 5", "Ответ ИИ 6", "Ответ ИИ 7","Ответ ИИ 8"]
task_images = ["", "", "", "", "", "", "", ""]  # пути к изображениям
max_ex13 = 3

app = LastWindow(scores, tasks, AI_answer, task_images, max_ex13)
app.mainloop()
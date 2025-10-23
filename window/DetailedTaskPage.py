import tkinter as tk
from tkinter import ttk
from object.Task import Task
import os
from PIL import Image
from tkinter import filedialog
from PIL import ImageTk
from tkinter import messagebox

class DetailedTaskPage(ttk.Frame):
    def __init__(self, notebook, controller, task_id):
        self.notebook = notebook
        super().__init__(self.notebook, padding=20)

        #self.task = Task(task_id)
        self.controller = controller

        self.style = ttk.Style()
        self.setup_tab_styles()

        self.image_answers = []

        self.create_tab()#создаем все табы, оно у меня не заработало на классах, поэтому все в таск запихну

    def setup_tab_styles(self):
        # Создаем общий стиль для всех вкладок с цветами
        self.style.configure('TNotebook.Tab',
                             padding=[15, 5],
                             background='lightblue')  # общий цвет для всех вкладок

    def rate(self):
        print(123)
        self.task.rate()
        # ... дальше расписывай

    #дальше бога нет, или танцы с бубном для задач 13-19 с загрузкой фото
    #pip install Pillow
    def create_tab(self):
        self.pack(fill='both', expand=True)

        zadanie_frame = ttk.Frame(self, padding=20)
        zadanie_frame.pack(fill='both', expand=True)

        zadanie_label = ttk.Label(zadanie_frame, text="<zadanie zadaniizaanie/.,kphsipfjpsodjvjkajvpkihb'kihspjovjspvipnwipvnpwijvipwnnihweifiowejfiwefioweo]iwehfgwejwejbvweuob]uovbwuevenioweuvbbweoubvuweibvbowuevuiwebbovubweighwe0ingwqho", font="Arial 14")
        zadanie_label.pack(fill='both', expand=True)#задание, вместо этой фигни фото

        answer_frame = ttk.Frame(self)
        answer_frame.pack(fill='x', padx=10, pady=10)
        upload_photo_otveta = ttk.Button(answer_frame, text="Выбрать фото", command=self.upload_photo)
        upload_photo_otveta.pack(anchor='w', pady=10)

        self.image_frame = ttk.LabelFrame(answer_frame, text="Предпросмотр", padding=10)#отображение фото
        self.image_frame.pack(fill='both', expand=True, pady=10)

        self.image_label = ttk.Label(self.image_frame, text="Фото не выбрано", font=('Arial', 12), foreground='gray')#пока пользовательского фото не тбудет это
        self.image_label.pack(expand=True)

        info_frame = ttk.Frame(answer_frame)
        info_frame.pack(fill='x', pady=10)

        self.info_label = ttk.Label(info_frame, text="", font=('Arial', 10))
        self.info_label.pack()

        clear_btn = ttk.Button(answer_frame, text="Очистить", command=self.clear_photo)#кнопка очистки
        clear_btn.pack(anchor='w', pady=5)

    def upload_photo(self):  #запрашиваем фото
        file_types = [('Изображения', '*.jpg *.jpeg *.png *.gif *.bmp *.tiff'), ('JPEG', '*.jpg *.jpeg'),
                      ('PNG', '*.png'), ('Все файлы', '*.*')]

        file_path = filedialog.askopenfilename(title="Выберите фото", filetypes=file_types)

        if file_path:
            self.load_image(file_path)

    def load_image(self, file_path): #загружаем фото
        try:
            image = Image.open(file_path)
            #self.image_path = file_path
            self.image_answers.append(image)
            file_size = os.path.getsize(file_path) / 1024  # в КБ
            file_name = os.path.basename(file_path)
            image_size = image.size
            info_text = (f"Файл: {file_name}\n"
                         f"Размер: {file_size:.1f} КБ\n"
                         f"Разрешение: {image_size[0]}x{image_size[1]}")
            self.info_label.config(text=info_text)
            max_size = (400, 300)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)
            self.current_image = ImageTk.PhotoImage(self.image_answers[0]) # сделай несколько изображений либо удаляй предосмотр
            self.image_label.config(image=self.current_image, text="")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение:\n{str(e)}")

    def clear_photo(self): #уничтожаем фото
        self.current_image = None
        self.image_answers = []
        self.image_label.config(image='', text="Фото не выбрано")
        self.info_label.config(text="")


import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from object.Task import Task
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk #pip install Pillow
import os

answers=[[],[],[],[],[],[],[],[],[],[],[],[]]#делаю матрицу в которой будут ответы пользователя на задачи

class TaskPage(tk.Frame):
    def __init__(self, root, controller, tasks_id):
        super().__init__(root)
        self.controller = controller
        for task in tasks_id:
            self.tasks.append(Task(task))
        self.root = root
        self.root.title("Задачи")
        self.root.geometry("800x1200")

        self.style = ttk.Style()
        self.setup_tab_styles()

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)

        self.create_tab_1()  # создаем все табы, оно у меня не заработало на классах, поэтому все в таск запихну

        self.root.resizable(True, True)
        self.current_image = None#картинки пользователя
        self.image_path = None
        self.create_tab_13()

        self.create_last_tab()

    def setup_tab_styles(self):
        # Создаем общий стиль для всех вкладок с цветами
        self.style.configure('TNotebook.Tab',
                             padding=[15, 5],
                             background='lightblue')  # общий цвет для всех вкладок

    def create_tab_1(self):#создание содержимого
            exercises1 = ["какая-то задача из первого", "другая задача из первого", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]
            answer1=[]
            for i in range(2):
                tab = ttk.Frame(self.notebook)

                self.notebook.add(tab, text={i + 1})

                zadanie_frame = ttk.Frame(tab)
                zadanie_frame.pack(fill='both', expand=True, padx=10, pady=10)

                image_label = ttk.Label(zadanie_frame, image=tasks[i])#тут фото, надо вместо tasks сделать название фото
                image_label.pack()

                answer_frame = ttk.Frame(tab)
                answer_frame.pack(fill='x', padx=10, pady=10)

                otvet_ukaz = ttk.Label(answer_frame, text="Ответ:", font=('Arial', 12))  # "Ответ:"
                otvet_ukaz.pack(side='left', padx=(0, 10))

                answer = ttk.Entry(answer_frame, font=('Arial', 12), width=40)  # поле ввода ответа
                answer.pack(side='left', fill='x', expand=True, padx=(0, 10))

                otvet = ttk.Button(answer_frame, text="Ответить",
                                   command=lambda idx=i, ans=answer: self.get_answer1(idx, ans))  # ответ
                otvet.pack(side='right')
    def get_answer1(self, task_index, answer):#получаем отвтет
        user_answer = answer.get()

        if not user_answer:
            # result_label.config(text="Введите ответ!")
            return
        answers[0].append(user_answer)

    #дальше бога нет, или танцы с бубном для задач 13-19 с загрузкой фото
    #pip install Pillow
    def create_tab_13(self):
        tab = ttk.Frame(self.root, padding=20)
        tab.pack(fill='both', expand=True)

        zadanie_frame = ttk.Frame(tab, padding=20)
        zadanie_frame.pack(fill='both', expand=True)

        zadanie_label = ttk.Label(zadanie_frame, text="<zadanie zadaniizaanie/.,kphsipfjpsodjvjkajvpkihb'kihspjovjspvipnwipvnpwijvipwnnihweifiowejfiwefioweo]iwehfgwejwejbvweuob]uovbwuevenioweuvbbweoubvuweibvbowuevuiwebbovubweighwe0ingwqho", font="Arial 14")
        zadanie_label.pack(fill='both', expand=True)#задание, вместо этой фигни фото

        answer_frame = ttk.Frame(tab)
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
            self.image_path = file_path
            file_size = os.path.getsize(file_path) / 1024  # в КБ
            file_name = os.path.basename(file_path)
            image_size = image.size
            info_text = (f"Файл: {file_name}\n"
                         f"Размер: {file_size:.1f} КБ\n"
                         f"Разрешение: {image_size[0]}x{image_size[1]}")
            self.info_label.config(text=info_text)
            max_size = (400, 300)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)
            self.current_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.current_image, text="")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение:\n{str(e)}")

    def clear_photo(self): #уничтожаем фото
        self.current_image = None
        self.image_path = None
        self.image_label.config(image='', text="Фото не выбрано")
        self.info_label.config(text="")


    def create_last_tab(self):
        tab = ttk.Frame(self.notebook)

        self.notebook.add(tab, text="Закончить")

        last_frame = ttk.Frame(tab)
        last_frame.pack(fill='both', expand=True, padx=10, pady=10)

        #zaver=ttk.Button(last_frame, text="Хотите закончить?", command=lambda: self.show_tocho())
        #zaver.pack(side='left', padx=(0, 10))



# root = tk.Tk()
# app = ex1Notebook(root)
# root.mainloop()

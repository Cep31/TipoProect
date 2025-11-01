import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import os


class TaskPage13(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, corner_radius=10, fg_color="transparent")

        ctk.set_appearance_mode("dark")#делаем красоту
        ctk.set_default_color_theme("blue")

        self.image_answers = []  #хранениt все картинrb пользователя
        self.current_image_index = -1  #индекс текущей картинки
        self.image_answers_id =[]#хранит путь к фото пользователя
        self.current_image = None  #текущяя картинка

        self.create_tab_13()

    def create_tab_13(self):
        tab = ctk.CTkFrame(self, corner_radius=15)
        tab.pack(fill='both', expand=True, padx=20, pady=20)

        zadanie_frame = ctk.CTkFrame(tab, corner_radius=10)#фрейм для задания
        zadanie_frame.pack(fill='both', expand=True, pady=(0, 10))

        zadanie_text = ("<zadanie zadaniizaanie/.,kphsipfjpsodjvjkajvpkihb'kihspjovjspvipnwipvnpwijvipwnnihweifiowejfiwefioweoiwehfgwejwejbvweuob]uovbwuevenioweuvbbweoubvuweibvbowuevuiwebbovubweighwe0ingwqho")#сюда фтото задания
        zadanie = ctk.CTkTextbox(zadanie_frame, font=ctk.CTkFont(size=14), wrap="word", height=400, border_width=1, border_color=("#3E454A", "#949A9F"))#тут менять рахмер задания
        zadanie.pack(fill='both', expand=True, padx=10, pady=10)
        zadanie.insert("1.0", zadanie_text)
        zadanie.configure(state="disabled")

        answer_frame = ctk.CTkFrame(tab, corner_radius=10)#фрейм для картинки пользователя
        answer_frame.pack(fill='both', expand=True, pady=10)

        control_frame = ctk.CTkFrame(answer_frame, fg_color="transparent")#фрейм для кнопок переключенич между картинками
        control_frame.pack(fill='x', padx=10, pady=10)

        upload_photo = ctk.CTkButton(control_frame, text="📷 Загрузить фото", command=self.upload_photo, font=ctk.CTkFont(size=14, weight="bold"), corner_radius=8, fg_color=("#3B8ED0", "#1F6AA5"), hover_color=("#36719F", "#144870"))
        upload_photo.pack(side='left', padx=(0, 10))#кнопка зашрузки картинки

        self.prev = ctk.CTkButton(control_frame, text="◀ Предыдущее", command=self.show_previous_image, font=ctk.CTkFont(size=12), corner_radius=6, state="disabled")
        self.prev.pack(side='left', padx=(0, 5))#кнопка предыдущего изображения

        self.next = ctk.CTkButton(control_frame, text="Следующее ▶", command=self.show_next_image, font=ctk.CTkFont(size=12), corner_radius=6, state="disabled")
        self.next.pack(side='left', padx=(0, 10))#кнопка следующего изображения

        self.nomer_inage = ctk.CTkLabel(control_frame, text="Фото: 0/0", font=ctk.CTkFont(size=12), text_color=("gray50", "gray70"))
        self.nomer_inage.pack(side='left', padx=10)#информациея о порядковом номере текущей картинке

        self.image_frame = ctk.CTkFrame(answer_frame, corner_radius=10)#фрейм для предпросмотра изображения
        self.image_frame.pack(fill='both', expand=True, padx=10, pady=(0, 10))

        preview_label = ctk.CTkLabel(self.image_frame, text="Предпросмотр изображения", font=ctk.CTkFont(size=16, weight="bold"))
        preview_label.pack(pady=(10, 5))

        self.image_label = ctk.CTkLabel(self.image_frame, text="Фото не выбрано\n\nНажмите 'Загрузить фото' для добавления изображений", font=ctk.CTkFont(size=14), text_color=("gray50", "gray70"), fg_color=("gray85", "gray25"), corner_radius=8, height=200)
        self.image_label.pack(fill='both', expand=True, padx=20, pady=10)#пока нет картинки есть это

        info_frame = ctk.CTkFrame(answer_frame, corner_radius=8, fg_color=("gray90", "gray20"))#фрейм для информации о файле
        info_frame.pack(fill='x', padx=10, pady=10)

        self.image_info = ctk.CTkLabel(info_frame, text="", font=ctk.CTkFont(size=12), justify="left", height=40)
        self.image_info.pack(fill='x', padx=10, pady=5)#информация о картинке

        clear_frame = ctk.CTkFrame(answer_frame, fg_color="transparent")#фрейм для кнопок очистки
        clear_frame.pack(fill='x', padx=10, pady=5)

        clear_current = ctk.CTkButton(clear_frame, text="🗑️ Удалить текущее", command=self.clear_current_image, font=ctk.CTkFont(size=12), corner_radius=6, fg_color=("#D35B5B", "#8B3A3A"), hover_color=("#B74A4A", "#6B2C2C"), state="disabled")
        clear_current.pack(side='left', padx=(0, 10))
        self.clear_current = clear_current#кнопка очистки текущего изображения

        clear_all = ctk.CTkButton(clear_frame, text="🗑️ Очистить все", command=self.clear_all_images, font=ctk.CTkFont(size=12), corner_radius=6, fg_color=("#D35B5B", "#8B3A3A"), hover_color=("#B74A4A", "#6B2C2C"), state="disabled")
        clear_all.pack(side='left')
        self.clear_all = clear_all#кнопка очистки всех изображений

    def upload_photo(self):#запрашиваем картинку у  пользователя
        file_types = [
            ('Изображения', '*.jpg *.jpeg *.png *.gif *.bmp *.tiff'),
            ('JPEG', '*.jpg *.jpeg'),
            ('PNG', '*.png'),
            ('Все файлы', '*.*')
        ]

        file_paths = filedialog.askopenfilenames(
            title="Выберите фото",
            filetypes=file_types
        )

        if file_paths:
            for file_path in file_paths:
                self.load_image(file_path)

            if self.image_answers:#показываем первое изображение после загрузки
                self.current_image_index = 0
                self.show_current_image()

    def load_image(self, file_path):#добавляем картинку в масив
        try:
            image = Image.open(file_path)
            file_info = {
                'image': image,
                'path': file_path,
                'name': os.path.basename(file_path),
                'size': os.path.getsize(file_path) / 1024,  # в КБ
                'resolution': image.size
            }
            self.image_answers.append(file_info)
            file_info_answers = {
                'path': file_path
            }
            self.image_answers_id.append(file_info_answers)

            self.update_controls_state()#активируем кнопки управления

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось загрузить изображение {os.path.basename(file_path)}:\n{str(e)}")

    def show_current_image(self):#показываем картинку на экране польхователя
        if 0 <= self.current_image_index < len(self.image_answers):
            file_info = self.image_answers[self.current_image_index]

            # Обновляем информацию о файле
            info_text = (f"Файл: {file_info['name']}\n"
                         f"Размер: {file_info['size']:.1f} КБ\n"
                         f"Разрешение: {file_info['resolution'][0]}x{file_info['resolution'][1]}\n"
                         f"Изображение {self.current_image_index + 1} из {len(self.image_answers)}")
            self.image_info.configure(text=info_text)

            # Создаем превью изображения
            image = file_info['image'].copy() # Создаем копию для изменения размера
            max_size = (12000, 300)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)

            # Конвертируем для CustomTkinter
            ctk_image = ctk.CTkImage(
                light_image=image,
                dark_image=image,
                size=image.size
            )

            # Сохраняем ссылку и обновляем метку
            self.current_image = ctk_image
            self.image_label.configure(image=self.current_image, text="", fg_color="transparent"
            )

            # Обновляем счетчик
            self.nomer_inage.configure(text=f"Фото: {self.current_image_index + 1}/{len(self.image_answers)}")

            # Обновляем состояние кнопок навигации
            self.update_navigation_buttons()

    def show_previous_image(self):#переключение на предыдущую картинку
        if self.current_image_index > 0:
            self.current_image_index -= 1
            self.show_current_image()

    def show_next_image(self):#переключение на следущую картинку
        if self.current_image_index < len(self.image_answers) - 1:
            self.current_image_index += 1
            self.show_current_image()

    def clear_current_image(self):#удаляем текущюю картинку
        if 0 <= self.current_image_index < len(self.image_answers):
            del self.image_answers[self.current_image_index]

            if not self.image_answers:#я эту фигню, тут как бы коректируются индексы картинок
                self.current_image_index = -1
                self.show_no_images()
            elif self.current_image_index >= len(self.image_answers):
                self.current_image_index = len(self.image_answers) - 1
                self.show_current_image()
            else:
                self.show_current_image()

            self.update_controls_state()#юлокаем если надо кнопку переключения

    def clear_all_images(self):#уничтожаем все картинки пользователя
        self.image_answers = []
        self.current_image_index = -1
        self.show_no_images()
        self.update_controls_state()

    def show_no_images(self):#отображаем что мы унмчтожили все картинки и надо загрухить новые
        self.image_label.configure(image="", text="Фото не выбрано\n\nНажмите 'Загрузить фото' для добавления изображений", fg_color=("gray85", "gray25"))
        self.image_info.configure(text="")
        self.nomer_inage.configure(text="Фото: 0/0")

    def update_controls_state(self):#контролируем состояние кнопок
        has_images = len(self.image_answers) > 0

        state = "normal" if has_images else "disabled"
        self.clear_current.configure(state=state)
        self.clear_all.configure(state=state)
        self.prev.configure(state=state)
        self.next.configure(state=state)

        if has_images and self.current_image_index == -1:#если есть изображения, но не показано ни одного - показываем первое
            self.current_image_index = 0
            self.show_current_image()

    def update_navigation_buttons(self):#обновляем если надо состояние кнопок
        self.prev.configure(state="normal" if self.current_image_index > 0 else "disabled")#следущее
        self.next.configure(state="normal" if self.current_image_index < len(self.image_answers) - 1 else "disabled")#предыдущее


# Пример использования
if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Задача №13")
    root.geometry("800x1200")

    app = TaskPage13(root)
    app.pack(fill='both', expand=True, padx=10, pady=10)

    root.mainloop()



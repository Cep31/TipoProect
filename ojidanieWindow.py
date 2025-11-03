import customtkinter as ctk
import time
import threading


class WaitingWindow:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("Ожидайте")
        self.root.geometry("600x400")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_waiting_window()
        self.start_parrot_animation()

    def create_waiting_window(self):
        main_frame = ctk.CTkFrame(self.root, corner_radius=15)
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)

        title_label = ctk.CTkLabel(main_frame, text="Ожидайте...",#заголовок
                                   font=('Arial', 24, 'bold'))
        title_label.pack(pady=20)

        self.animation_frame = ctk.CTkFrame(main_frame, height=200)#фрейм для попугая
        self.animation_frame.pack(fill='both', expand=True, padx=20, pady=10)
        self.animation_frame.pack_propagate(False)

        self.animation_text = ctk.CTkTextbox(self.animation_frame, font=('Courier New', 12), state='disabled', fg_color='black', text_color='white')
        self.animation_text.pack(fill='both', expand=True, padx=10, pady=10)#поле для анимации

        self.progress = ctk.CTkProgressBar(main_frame)#прогрессбар
        self.progress.pack(fill='x', padx=20, pady=10)
        self.progress.set(0)

    def start_parrot_animation(self):#запускаем анимацию в отдельном потоке
        self.animation_thread = threading.Thread(target=self.animate_parrot)
        self.animation_thread.daemon = True
        self.animation_thread.start()

    def animate_parrot(self):
        #кадры анимации попугая
        parrot_frames = [
            """
               \\
                \\
                 \\
             ____\\
            /---  \\
           | @    | 
            \\_____/
            /    /
            """,
            """
               \\
                \\
                 \\
             ____\\
            /---  \\
           | @    | 
            \\_____/
             /   /
            """,
            """
               \\
                \\
                 \\
             ____\\
            /---  \\
           | @    | 
            \\_____/
              / /
            """,
            """
               \\
                \\
                 \\
             ____\\
            /---  \\
           | @    | 
            \\_____/
               /\\
            """
        ]

        frame_counter = 0
        while True:
            #выбираем текущий кадр
            current_frame = parrot_frames[frame_counter % len(parrot_frames)]

            #добавляем мигающий текст
            dots = "." * ((frame_counter // 2) % 4)
            status_text = f"Идет проверка{dots}\n\n{current_frame}"

            #обновляем текстовое поле в основном потоке
            self.root.after(0, self.update_animation, status_text)

            #обновляем прогресс бар
            progress_value = (frame_counter % 100) / 100.0
            self.root.after(0, self.update_progress, progress_value)

            frame_counter += 1
            time.sleep(0.2)

    def update_animation(self, text):
        self.animation_text.configure(state='normal')
        self.animation_text.delete('1.0', 'end')
        self.animation_text.insert('1.0', text)
        self.animation_text.configure(state='disabled')

    def update_progress(self, value):
        self.progress.set(value)

    def run(self):
        self.root.mainloop()




app = WaitingWindow()
app.run()
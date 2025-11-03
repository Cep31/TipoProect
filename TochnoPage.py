import customtkinter as ctk


class YesNoDialog:
    def __init__(self, title="  "):
        self.root = ctk.CTk()
        self.root.title(title)
        self.root.geometry("400x200")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.show_tochno()

    def show_tochno(self):
        frame = ctk.CTkFrame(self.root, corner_radius=15)
        frame.pack(fill='both', expand=True, padx=20, pady=20)

        self.label = ctk.CTkLabel(frame, text="Точно хотите завершить?", font=('Arial', 16))
        self.label.pack(pady=20)

        button_frame = ctk.CTkFrame(frame, fg_color="transparent")
        button_frame.pack(pady=10)

        self.yes = ctk.CTkButton(button_frame, text="Да", font=('Arial', 14, 'bold'),
                                 fg_color='#28a745', hover_color='#218838', width=100,
                                 command=self.da)
        self.yes.pack(side='left', padx=10)

        self.no = ctk.CTkButton(button_frame, text="Нет", font=('Arial', 14, 'bold'),
                                fg_color='#dc3545', hover_color='#c82333', width=100,
                                command=self.net)
        self.no.pack(side='left', padx=10)

        self.root.bind('<Return>', lambda event: self.da())
        self.root.bind('<Escape>', lambda event: self.net())

    def da(self):
        self.root.destroy()

    def net(self):
        self.root.destroy()


dialog = YesNoDialog()
dialog.root.mainloop()
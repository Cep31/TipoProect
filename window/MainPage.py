import customtkinter as ctk


class ScrollableFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class MainPage(ctk.CTkFrame):
    def __init__(self, root, controller):
        super().__init__(root)
        self.controller = controller
        self.tasks_count = []
        self.entry_widgets = []  #для хранения ссылок на виджеты ввода

        self.task = ctk.CTkLabel(self, text="Выберите количество задач по каждому типу:", font=("Arial", 16, "bold"), text_color="#2E8B57")
        self.task.pack(pady=(10, 20))

        self.scrollable_frame = ScrollableFrame(self, width=550, height=500, fg_color="transparent", scrollbar_button_color="#2E8B57", scrollbar_button_hover_color="#3CB371")
        self.scrollable_frame.pack(fill="both", expand=True, padx=10, pady=10)

        names = ["№1 Планиметрия", "№2 Векторы", "№3 Стереометрия", "№4 Простая теория вероятности",
                 "№5 Сложная вероятность", "№6 Уравнения", "№7 Вычисления и преобразования",
                 "№8 Производная и первообразная", "№9 Прикладная задача", "№10 Текстовая задача",
                 "№11 Графики функций", "№12 Анализ функций", "№13 Уравнения", "№14 Стереометрия",
                 "№15 Неравенства", "№16 Экономическая задача", "№17 Планиметрия", "№18 Задача с параметром",
                 "№19 Числа и их свойства"]

        for i in range(len(names)):  #заполняем массив
            self.tasks_count.append(0)

            main_frame = ctk.CTkFrame(self.scrollable_frame, border_width=2, border_color="#3E3E3E", corner_radius=8)

            ex_name = ctk.CTkLabel(main_frame, text=names[i], font=("Arial", 12, "bold"), anchor="w")

            control_frame = ctk.CTkFrame(main_frame, fg_color="transparent")

            minus = ctk.CTkButton(control_frame, text="-", width=30, height=30, font=("Arial", 14, "bold"), fg_color="#FF6B6B", hover_color="#FF5252", command=lambda idx=i: self.decrement_value(idx))

            entry = ctk.CTkEntry(control_frame, width=50, height=30, justify="center", font=("Arial", 12), border_color="#3E3E3E")
            entry.insert(0, "0")
            self.entry_widgets.append(entry)

            plus = ctk.CTkButton(control_frame, text="+", width=30, height=30, font=("Arial", 14, "bold"), fg_color="#4ECDC4", hover_color="#45B7AF", command=lambda idx=i: self.increment_value(idx))

            minus.pack(side="left", padx=(0, 5))
            entry.pack(side="left", padx=5)
            plus.pack(side="left", padx=(5, 0))

            ex_name.pack(side="left", padx=(10, 20), pady=8, fill="x", expand=True)
            control_frame.pack(side="right", padx=(0, 10), pady=8)
            main_frame.pack(anchor="nw", fill="x", padx=5, pady=5)

        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(fill="x", padx=15, pady=10)

        gotov = ctk.CTkButton(button_frame, text="Готово", command=self.ready_on_click, font=("Arial", 14, "bold"), fg_color="#2E8B57", hover_color="#3CB371", height=40, corner_radius=8)
        gotov.pack(anchor="se", pady=10)

    def increment_value(self, index):
        current = self.tasks_count[index]
        if current < 100:
            self.tasks_count[index] = current + 1
            self.entry_widgets[index].delete(0, "end")
            self.entry_widgets[index].insert(0, str(current + 1))

    def decrement_value(self, index):
        current = self.tasks_count[index]
        if current > 0:
            self.tasks_count[index] = current - 1
            self.entry_widgets[index].delete(0, "end")
            self.entry_widgets[index].insert(0, str(current - 1))

    def update_from_entry(self, index):#прямой ввод
        try:
            value = self.entry_widgets[index].get()
            if value == "":
                value = "0"
            num_value = int(value)
            if num_value < 0:
                num_value = 0
            elif num_value > 100:
                num_value = 100
                self.entry_widgets[index].delete(0, "end")
                self.entry_widgets[index].insert(0, "100")

            self.tasks_count[index] = num_value
        except ValueError:
            self.entry_widgets[index].delete(0, "end")
            self.entry_widgets[index].insert(0, "0")
            self.tasks_count[index] = 0

    def ready_on_click(self):
        self.controller.generate_problems_on_click()
        for i in range(len(self.entry_widgets)):
            self.update_from_entry(i)#тут дестрой писать

    def get_tasks_count(self):
        return self.tasks_count

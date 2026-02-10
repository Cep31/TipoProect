import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

class ScrollableNotebook(ttk.Notebook):
    def __init__(self, master=None, visible_tabs=5, **kwargs):
        super().__init__(master, **kwargs)
        self._first_visible_tab = 0
        self.visible_tabs = visible_tabs
        self.bind("<Button-4>", self._on_mousewheel_up)
        self.bind("<Button-5>", self._on_mousewheel_down)
        self.bind("<MouseWheel>", self._on_mousewheel)

        self.setup_black_style()

    def setup_black_style(self):
        style = ttk.Style()

        # устанавливаем тему, которая поддерживает настройку
        style.theme_use('default')
        style.configure("Custom.TNotebook.Tab")
        # стиль для Notebook и Tab
        style.configure(
        "Black.TNotebook",
            background="gray17",
            borderwidth=0,
            tabmargins=[0, 0, 0, 0]
        )

        style.configure("Black.TNotebook.Tab",
                        background="black",
                        foreground="white",
                        borderwidth=0,
                        relief="flat",
                        padding=[30, 10],
                        margin=10,
                        font=("Arial", 12, "bold"),
                        focuscolor="none")

        style.map("Black.TNotebook.Tab",
                  background=[("selected", _from_rgb((115, 127, 192))),
                              ("active", _from_rgb((60, 80, 190))),
                              ("!selected", _from_rgb((60, 80, 190)))],
                  foreground=[("selected", "white"),
                              ("active", "white"),
                              ("!selected", "white")],
                  relief=[("selected", "raised"),
                          ("active", "raised"),
                          ("!selected", "flat")])

        # применяем стиль
        self.configure(style="Black.TNotebook")

    def _on_mousewheel(self, event):
        if event.delta > 0:
            self._scroll_left()
        else:
            self._scroll_right()

    def _on_mousewheel_up(self, event):
        self._scroll_left()

    def _on_mousewheel_down(self, event):
        self._scroll_right()

    def _scroll_left(self):
        if self._first_visible_tab > 0:
            self._first_visible_tab -= 1
            self.show_tabs()

    def _scroll_right(self):
        if self._first_visible_tab < len(self.tabs()) - 1:
            self._first_visible_tab += 1
            self.show_tabs()

    def show_tabs(self):
        # показывает только часть вкладок
        all_tabs = self.tabs()
        for i, tab_id in enumerate(all_tabs):
            if i < self._first_visible_tab or i >= self._first_visible_tab + self.visible_tabs:
                self.hide(tab_id)
            else:
                self.add(tab_id, text=self.tab(tab_id, "text"))


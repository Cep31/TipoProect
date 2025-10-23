import tkinter as tk
from tkinter import ttk

class ScrollableNotebook(ttk.Notebook):
    def __init__(self, master=None, visible_tabs=5, **kwargs):
        super().__init__(master, **kwargs)
        self._first_visible_tab = 0
        self.visible_tabs = visible_tabs
        self.bind("<Button-4>", self._on_mousewheel_up)
        self.bind("<Button-5>", self._on_mousewheel_down)
        self.bind("<MouseWheel>", self._on_mousewheel)

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
            self._show_tabs()

    def _scroll_right(self):
        if self._first_visible_tab < len(self.tabs()) - 1:
            self._first_visible_tab += 1
            self._show_tabs()

    def _show_tabs(self):
        # показывает только часть вкладок
        all_tabs = self.tabs()
        for i, tab_id in enumerate(all_tabs):
            if i < self._first_visible_tab or i >= self._first_visible_tab + self.visible_tabs:
                self.hide(tab_id)
            else:
                self.add(tab_id, text=self.tab(tab_id, "text"))


# root = tk.Tk()
# root.geometry("500x300")
#
# notebook = ScrollableNotebook(root)
# notebook.pack(expand=True, fill="both")
#
# for i in range(12):
#     frame = tk.Frame(notebook, bg=f"#{(i*2):02x}{(255-i*10):02x}{(i*15)%255:02x}")
#     tk.Label(frame, text=f"страница {i+1}", bg=frame["bg"]).pack(expand=True)
#     notebook.add(frame, text=f"вкладка {i+1}")
#
# root.mainloop()

from tkinter import *
from backend.FrameController import FrameController

import customtkinter as ctk

root = ctk.CTk()
root.geometry("800x950")
root.resizable(width=False, height=False)

frameHandler = FrameController(root)

root.mainloop()
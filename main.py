from tkinter import *
from object.FrameController import FrameController
from object.Autocheck import Autocheck
import customtkinter as ctk

root = ctk.CTk()
root.geometry("800x950")
root.resizable(width=False, height=False)

frameHandler = FrameController(root)

root.mainloop()
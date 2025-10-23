from tkinter import *
from object.FrameController import FrameController
from object.Autocheck import Autocheck

root = Tk()
root.geometry("410x900")

frameHandler = FrameController(root)

root.mainloop()
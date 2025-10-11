import re # нахера оно тебе?
from tkinter import *
from tkinter.ttk import *
from object.FrameHandler import FrameHandler

root = Tk()
root.geometry("410x900")

frameHandler = FrameHandler(root)
frameHandler.show_main()
# frameHandler.forget_main() скрыть главную страницу

root.mainloop()
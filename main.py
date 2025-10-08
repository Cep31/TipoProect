import re # нахера оно тебе?
from tkinter import *
from tkinter.ttk import *
from object.FrameHandler import FrameHandler

root = Tk()
root.geometry("300x700")

frameHandler = FrameHandler(root)
frameHandler.main_init()
frameHandler.show_main()
# frameHandler.forget_main() скрыть главную страницу

root.mainloop()
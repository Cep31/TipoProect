from object.Problem import Problem
import tkinter as tk

root = tk.Tk()
root.title("123")
root.geometry('600x600')

problem = Problem("01_02_001")
photo = problem.get_photo()
photo.subsample(1, 1)
label = tk.Label(root)
label.image = photo
label['image'] = photo
label.pack()

root.mainloop()
import re
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.geometry("300x700")

frame1 = Frame(root, borderwidth=3, relief=SOLID, padding=[1,2])
ext1 = Label(frame1, text="Планиметрия ", font=("Arial",10, 'bold'))
sp1 = Spinbox(frame1, from_=0, to=100)
ext1.pack(side=LEFT)
sp1.pack(side=RIGHT)
frame1.pack(anchor="nw", fill=X, padx=10, pady=5)

frame2 = Frame(root, borderwidth=3, relief=SOLID, padding=[1,2])
ext2 = Label(frame2, text="Векторы ", font=("Arial",10, 'bold'))
sp2 = Spinbox(frame2, from_=0, to=100)
ext2.pack(side=LEFT)
sp2.pack(side=RIGHT)
frame2.pack(anchor="nw", fill=X, padx=10, pady=5)

frame3 = Frame(root, borderwidth=3, relief=SOLID, padding=[1,2])
ext3 = Label(frame3, text="Стереометрия ", font=("Arial",10, 'bold'))
sp3 = Spinbox(frame3, from_=0, to=100)
ext3.pack(side=LEFT)
sp3.pack(side=RIGHT)
frame3.pack(anchor="nw", fill=X, padx=10, pady=10)

frame4 = Frame(root, borderwidth=3, relief=SOLID, padding=[1,2])
ext4 = Label(frame4, text="Вероятность ", font=("Arial",10, 'bold'))
sp4 = Spinbox(frame4, from_=0, to=100)
ext4.pack(side=LEFT)
sp4.pack(side=RIGHT)
frame4.pack(anchor="nw", fill=X, padx=10, pady=10)

frame5 = Frame(root, borderwidth=3, relief=SOLID, padding=[1,2])
ext5 = Label(frame5, text="Вероятност ", font=("Arial",10, 'bold'))
sp5 = Spinbox(frame5, from_=0, to=100)
ext5.pack(side=LEFT)
sp5.pack(side=RIGHT)
frame5.pack(anchor="nw", fill=X, padx=10, pady=10)

frame6 = Frame(root, borderwidth=3, relief=SOLID, padding=[1,2])
ext6 = Label(frame6, text="Уравнения ", font=("Arial",10, 'bold'))
sp6 = Spinbox(frame6, from_=0, to=100)
ext6.pack(side=LEFT)
sp6.pack(side=RIGHT)
frame6.pack(anchor="nw", fill=X, padx=10, pady=10)

frame7 = Frame(root, borderwidth=3, relief=SOLID, padding=[1,2])
ext7 = Label(frame7, text="Выражения ", font=("Arial",10, 'bold'))
sp7 = Spinbox(frame7, from_=0, to=100)
ext7.pack(side=LEFT)
sp7.pack(side=RIGHT)
frame7.pack(anchor="nw", fill=X, padx=10, pady=10)

frame8 = Frame(root, borderwidth=3, relief=SOLID, padding=[1,2])
ext8 = Label(frame8, text="Графики функций ", font=("Arial",10, 'bold'))
sp8 = Spinbox(frame8, from_=0, to=100)
ext8.pack(side=LEFT)
sp8.pack(side=RIGHT)
frame8.pack(anchor="nw", fill=X, padx=10, pady=10)

frame9 = Frame(root, borderwidth=3, relief=SOLID, padding=[1,2])
ext9 = Label(frame9, text="Прикладная задача ", font=("Arial",10, 'bold'))
sp9 = Spinbox(frame9, from_=0, to=100)
ext9.pack(side=LEFT)
sp9.pack(side=RIGHT)
frame9.pack(anchor="nw", fill=X, padx=10, pady=10)

frame10 = Frame(root, borderwidth=3, relief=SOLID, padding=[1,2])
ext10 = Label(frame10, text="Текстовая задача ", font=("Arial",10, 'bold'))
sp10 = Spinbox(frame10, from_=0, to=100)
ext10.pack(side=LEFT)
sp10.pack(side=RIGHT)
frame10.pack(anchor="nw", fill=X, padx=10, pady=10)




root.mainloop()
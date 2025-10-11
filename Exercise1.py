from tkinter import *
from tkinter.ttk import *

# под снос

def Wcollor(res):
    if res == 3:#типо макс балл
        col = "green"
    elif res == 0:
        col = "red"
    else:
        col = "yellow"
    return col


Wiex1 = Tk()
Wiex1.title("Задание 1")
Wiex1.geometry("800x500")
back = Style()
collor = Wcollor(3)
back.configure("TFrame", background=collor)

notebook = Notebook(Wiex1)
notebook.pack(expand=True, fill="both")
for i in range(2):#берем из того масива нулями и с вар
    frame = Frame(notebook, width=800, height=300)
    frame.pack(expand=YES, fill=X)
    notebook.add(frame, text=("задание:", i+1))

    Zadanie = Label(frame, text="Тут задание", font=("Arial", 20))#Задание
    Zadanie.pack(anchor="nw", expand=True, fill=X)

    answer = Entry(frame)#поле ввода ответа
    answer.pack(anchor="nw", expand=True, pady=10)

    otvet = Button(frame, text="Ответить")#кнопка ответить, сюда надо с помощью answer.get() в функции записать ответ и проверить его
    otvet.pack(anchor="se", padx=5, pady=5)

Wiex1.mainloop()
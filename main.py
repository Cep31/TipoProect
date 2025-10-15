from tkinter import *
from object.FrameController import FrameHandler
from object.Autocheck import Autocheck

root = Tk()
root.geometry("410x900")

frameHandler = FrameHandler(root)

def get_response():
    response = Autocheck.check("123_test", ["answer.jpg"])
    return response

# with ThreadPoolExecutor() as executor:
#     future = executor.submit(get_response)
#     return_value = future.result()

#print(return_value)

root.mainloop()
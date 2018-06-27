from tkinter import *


def say_hello():
    print("hello")


window = Tk()
window.title('first title')
btn = Button(window, text='ok', command=say_hello)
btn.pack()
window.mainloop()


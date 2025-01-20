from tkinter import *

def button_clicked():
    label.configure(text=input1.get())

window = Tk()
window.minsize(400, 300)
window.title("Hello World")

input1 = Entry(window)
label = Label(window, text="Enter your name: ")
button = Button(window, text="submit", command=button_clicked)
label.pack()
input1.pack()
button.pack()


















window.mainloop()
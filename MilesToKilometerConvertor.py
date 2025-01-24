from tkinter import *\

def calc():
    kilometer = float(miles_input.get()) * 1.60934
    kms = str(kilometer)
    kilometer_label.config(text=f"{kms}km")

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=200, height=100)

miles_input = Entry(window, width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(window, text=f"Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(window, text=f"is equal to")
is_equal_label.grid(column=0, row=1)

kilometer_label = Label(window, text=f" km")
kilometer_label.grid(column=2, row=1)

btn = Button(text="Submit", command=calc)
btn.grid(column=1, row=2)



window.mainloop()
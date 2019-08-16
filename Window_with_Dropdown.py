from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome! What is your favorite food?")

window.geometry('350x200')

combo = Combobox(window)

combo['values'] = ('Pizza', 'Burgers','Tacos')

combo.current(1)  # set the selected item

combo.grid(column=0, row=0)

window.mainloop()

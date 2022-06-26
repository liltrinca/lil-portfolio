from tkinter import *
from tkinter import ttk
import turtle


root = Tk()

form = ttk.Frame(root, padding = 20, borderwidth = 5)
form.grid()


ttk.Label(form, text = 'Status Updater', padding = 15).grid(column = 1, row = 0)
ttk.Entry(form).grid(column = 0, row = 1)
ttk.Label(form, text = 'to').grid(column = 1, row = 1)
ttk.Entry(form).grid(column = 2, row = 1)
ttk.Entry(form).grid(column = 1, row = 2)
ttk.Button(form, text = 'Update').grid(column = 1, row = 3)

root.mainloop()
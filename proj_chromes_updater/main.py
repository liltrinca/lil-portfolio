from tkinter import *
from tkinter import ttk


def update():
    a = first_entry.get()
    b = last_entry.get()
    print(a, b)


# Root screen
root = Tk()

# StringVar()
first_chrome = StringVar(root)
last_chrome = StringVar(root)
user = StringVar(root)

# Creating form grid layout
form = ttk.Frame(root, padding=20, borderwidth=5)
form.grid()

# Widget Creation
status_label = ttk.Label(form, text='Status Updater', padding=15)
first_entry = ttk.Entry(form, textvariable=first_chrome)
to_label = ttk.Label(form, text='to')
last_entry = ttk.Entry(form, textvariable=last_chrome)
user_entry = ttk.Entry(form, textvariable=user)
update_button = ttk.Button(form, text='Update', command=lambda: update())

# Widget Layout
status_label.grid(column=1, row=0)
first_entry.grid(column=0, row=1)
to_label.grid(column=1, row=1)
last_entry.grid(column=2, row=1)
user_entry.grid(column=1, row=2)
update_button.grid(column=1, row=3)

# End of screen
root.mainloop()
from tkinter import *
from tkinter import ttk


def update():
    start_chrome = int(first_entry.get())
    end_chrome = int(last_entry.get())
    chromes_list = [x for x in range(start_chrome, end_chrome + 1)]
    print(chromes_list)


# Root screen
root = Tk()

# StringVar()
first_chrome_str = StringVar(root)
last_chrome_str = StringVar(root)
user = StringVar(root)

# Creating form grid layout
form = ttk.Frame(root, padding=20, borderwidth=5)
form.grid()

# Widget Creation
status_label = ttk.Label(form, text='Status Updater', padding=15)
first_entry = ttk.Entry(form, textvariable=first_chrome_str)
to_label = ttk.Label(form, text='to')
last_entry = ttk.Entry(form, textvariable=last_chrome_str)
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
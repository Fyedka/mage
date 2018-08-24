from tkinter import *

# Let's get the broad layout of the sections done first.

master = Tk()


def rowweight(index, weight):
    # Adjust weight(s) of row(s).
    assert(len(index) == len(weight))
    for i, w in zip(index, weight):
        master.grid_rowconfigure(i, weight=w)


def colweight(index, weight):
    # Adjust weight(s) of column(s).
    assert(len(index) == len(weight))
    for i, w in zip(index, weight):
        master.grid_columnconfigure(i, weight=w)


master.title("Crystal's Mage Database")

top_toolbar = Frame(master, bg="green", height=1, width=1)
top_toolbar.grid(row=1, column=1, columnspan=4, sticky=E+W+N+S)

leftbox = Frame(master, bg="red", height=1, width=1)
leftbox.grid(row=2, column=1, rowspan=2, sticky=N+S+E+W)

midbox = Frame(master, bg="white", height=1, width=1)
midbox.grid(row=2, column=2, rowspan=2, sticky=N+S+E+W)

righttopbox = Frame(master, bg="black", height=1, width=1)
righttopbox.grid(row=2, column=3, sticky=N+S+E+W)

rightbottombox = Frame(master, bg="purple", height=1, width=1)
rightbottombox.grid(row=3, column=3, sticky=N+S+E+W)

bottombox = Frame(master, bg="orange", height=1, width=1)
bottombox.grid(row=4, column=1, columnspan=4, sticky=N+S+E+W)

master.grid_rowconfigure(1, weight=1)
master.grid_rowconfigure(2, weight=4)
master.grid_rowconfigure(3, weight=4)
master.grid_rowconfigure(4, weight=1)

master.grid_columnconfigure(1, weight=1)
master.grid_columnconfigure(2, weight=2)
master.grid_columnconfigure(3, weight=1)

master.mainloop()

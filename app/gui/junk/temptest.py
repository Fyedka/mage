from tkinter import *
from tkinter import ttk

### FUNCTION DEFINITIONS ###
def rowweight(index, weight):
    # Adjust weight(s) of row(s).
    if type(index) == int:  # Singleton case
        assert(type(weight) == int)
        master.grid_rowconfigure(index, weight=weight)
    else:  # Range case
        assert(len(index) == len(weight))
        for i, w in zip(index, weight):
            master.grid_rowconfigure(i, weight=w)


def colweight(index, weight):
    # Adjust weight(s) of column(s).
    if type(index) == int:  # Singleton case
        assert(type(weight) == int)
        master.grid_columnconfigure(index, weight=weight)
    else:  # Range case
        assert(len(index) == len(weight))
        for i, w in zip(index, weight):
            master.grid_columnconfigure(i, weight=w)


### BUILDING THE GUI LAYOUT AND WIDGETS ###
# Create window that frames all our pieces
master = Tk()
master.title("Test Database")

### Broad layout into frames first ###
rowweight(range(1, 5), [10, 40, 40, 10])
colweight(range(1, 4), [25, 75, 25])
top_toolbar = Frame(master, bg="green", height=50, width=1)
top_toolbar.grid(row=1, column=1, columnspan=4, sticky=E+W+N+S)
leftbox = Frame(master, height=1, width=1)
leftbox.grid(row=2, column=1, rowspan=2, sticky=N+S+E+W)
midbox = Frame(master, bg="white", height=1, width=1)
midbox.grid(row=2, column=2, rowspan=2, sticky=N+S+E+W)
righttopbox = Frame(master, bg="black", height=1, width=1)
righttopbox.grid(row=2, column=3, sticky=N+S+E+W)
rightbottombox = Frame(master, bg="purple", height=1, width=1)
rightbottombox.grid(row=3, column=3, sticky=N+S+E+W)
bottombox = Frame(master, bg="orange", height=1, width=1)
bottombox.grid(row=4, column=1, columnspan=4, sticky=N+S+E+W)

master.mainloop()

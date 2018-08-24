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
rowweight(range(1, 5), [10, 40, 40, 10])
colweight(range(1, 4), [25, 75, 25])

### Broad layout into frames first -- color-coded for ease of debugging ###
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


### Create list of sections/categories at left edge ###
entity_type_list = ttk.Treeview(leftbox)
entity_type_list.pack(expand=True, side=LEFT, fill=BOTH)

# Create scrollbar for entity_type_list just to its right #
sb_etl = Scrollbar(leftbox)
sb_etl.pack(side=LEFT, fill=Y)

# Link sb_etl to entity_type_list
entity_type_list.configure(yscrollcommand=sb_etl.set)
sb_etl.configure(command=entity_type_list.yview)

# Populate the list with some initial values
initvals_etl = ["Characters", "Items"]
for x in initvals_etl:
    entity_type_list.insert('', END, x, text=str(x))
y = entity_type_list.insert('', END, "nums", text="Numbers")
for x in range(100):
    entity_type_list.insert(y, END, x, text=str(x))

### Create buttons at upper half of right edge ###
# Create frame to contain the buttons
bwidth = 12  # button width
b1 = Button(righttopbox, text="New", width=12)
b1.grid(row=1, column=1, sticky="")
b2 = Button(righttopbox, text="Edit", width=12)
b2.grid(row=2, column=1, sticky="")
b3 = Button(righttopbox, text="Organize", width=12)
b3.grid(row=3, column=1, sticky="")
b4 = Button(righttopbox, text="Templates", width=12)
b4.grid(row=4, column=1, sticky="")
b5 = Button(righttopbox, text="Delete", width=12)
b5.grid(row=5, column=1, sticky="")

# Space buttons vertically
righttopbox.grid_rowconfigure(1, weight=1)
righttopbox.grid_rowconfigure(2, weight=1)
righttopbox.grid_rowconfigure(3, weight=1)
righttopbox.grid_rowconfigure(4, weight=1)
righttopbox.grid_rowconfigure(5, weight=1)

# Center buttons horizontally
rtb_pad_left = Frame(righttopbox, width=1)
rtb_pad_right = Frame(righttopbox, width=1)
rtb_pad_left.grid(row=1, column=0, rowspan=5)
rtb_pad_right.grid(row=1, column=2, rowspan=5)
righttopbox.grid_columnconfigure(0, weight=1)
righttopbox.grid_columnconfigure(1, weight=1)
righttopbox.grid_columnconfigure(2, weight=1)

### Create placeholder textbox in the middle frame
mainbox = Text(midbox, bg="white")
mainbox.pack(expand=True, fill=BOTH)

### Create placeholder textbox in right bottom frame ###
reserved = Text(rightbottombox, bg="purple", width=1)
reserved.pack(expand=True, fill=BOTH)

### Create log output box at bottom of screen
logbox = Text(bottombox, height=6, width=80, bg="orange")
logbox.pack(expand=True, fill=BOTH)

print(rightbottombox.grid_size())

master.mainloop()

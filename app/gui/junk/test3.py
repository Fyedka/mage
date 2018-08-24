from tkinter import *
from tkinter import ttk


class CharDbGui(Frame):
    # Mage character database object
    def __init__(self, root, database=None, *args, **kwargs):
        Frame.__init__(self, root, *args, **kwargs)
        self.root = root

        ### Broad layout into color-coded frames first ###
        self.rowweight(range(1, 5), [10, 40, 40, 10])
        self.colweight(range(1, 4), [25, 75, 25])
        top_toolbar = Frame(self, bg="green", height=50, width=1)
        top_toolbar.grid(row=1, column=1, columnspan=4, sticky=E+W+N+S)
        leftbox = Frame(self, height=1, width=1)
        leftbox.grid(row=2, column=1, rowspan=2, sticky=N+S+E+W)
        midbox = Frame(self, bg="white", height=1, width=1)
        midbox.grid(row=2, column=2, rowspan=2, sticky=N+S+E+W)
        righttopbox = Frame(self, bg="black", height=1, width=1)
        righttopbox.grid(row=2, column=3, sticky=N+S+E+W)
        rightbottombox = Frame(self, bg="purple", height=1, width=1)
        rightbottombox.grid(row=3, column=3, sticky=N+S+E+W)
        bottombox = Frame(self, bg="orange", height=1, width=1)
        bottombox.grid(row=4, column=1, columnspan=4, sticky=N+S+E+W)
        entity_type_list = ttk.Treeview(leftbox)
        entity_type_list.pack(expand=True, side=LEFT, fill=BOTH)
        sb_etl = Scrollbar(leftbox)
        sb_etl.pack(side=LEFT, fill=Y)

        ### Placeholder widgets ###
        mainbox = Text(midbox, bg="white")
        mainbox.pack(expand=True, fill=BOTH)
        reserved = Text(rightbottombox, bg="purple", width=1)
        reserved.pack(expand=True, fill=BOTH)
        logbox = Text(bottombox, height=6, width=80, bg="orange")
        logbox.pack(expand=True, fill=BOTH)

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

        # add self to root
        self.pack(expand=True, fill=BOTH)

    def rowweight(self, index, weight):
        # Adjust weight(s) of row(s).
        if type(index) == int:  # Singleton case
            assert(type(weight) == int)
            self.root.grid_rowconfigure(index, weight=weight)
        else:  # Range case
            assert(len(index) == len(weight))
            for i, w in zip(index, weight):
                self.root.grid_rowconfigure(i, weight=w)

    def colweight(self, index, weight):
        # Adjust weight(s) of column(s).
        if type(index) == int:  # Singleton case
            assert(type(weight) == int)
            self.root.grid_columnconfigure(index, weight=weight)
        else:  # Range case
            assert(len(index) == len(weight))
            for i, w in zip(index, weight):
                self.root.grid_columnconfigure(i, weight=w)

    def fillDefaults(self):
        # Placeholder values to test with
        self.root.title("Test Database")
        # Populate the list with some initial values
        initvals_etl = ["Characters", "Items"]
        for x in initvals_etl:
            self.tree.insert('', END, x, text=str(x))

        y = self.tree.insert('', END, "nums", text="Numbers")
        for x in range(100):
            self.tree.insert(y, END, x, text=str(x))

    def launch(self):
        self.root.mainloop()


if __name__ == '__main__':
    root = Tk()
    gui = CharDbGui(root)
    root.wm_state('zoomed')
    gui.launch()

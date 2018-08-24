from tkinter import *
from tkinter import ttk


class CharDbGui(Frame):
    # GUI object
    def __init__(self, root, database=None, *args, **kwargs):
        Frame.__init__(self, root, *args, **kwargs)
        self.root = root

        ### Broad layout into frames first ###
        self.rowweight(range(1, 5), [10, 40, 40, 10])
        self.colweight(range(1, 4), [25, 75, 25])
        top_toolbar = Text(self, bg="green")
        top_toolbar.grid(row=1, column=1, columnspan=4, sticky=E+W+N+S)
        leftbox = Text(self, bg="gray")
        leftbox.grid(row=2, column=1, rowspan=2, sticky=N+S+E+W)
        midbox = Text(self, bg="white")
        midbox.grid(row=2, column=2, rowspan=2, sticky=N+S+E+W)
        righttopbox = Text(self, bg="black")
        righttopbox.grid(row=2, column=3, sticky=N+S+E+W)
        rightbottombox = Text(self, bg="purple")
        rightbottombox.grid(row=3, column=3, sticky=N+S+E+W)
        bottombox = Text(self, bg="orange")
        bottombox.grid(row=4, column=1, columnspan=4, sticky=N+S+E+W)

        # Position self in root
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

    def launch(self):
        self.root.mainloop()


if __name__ == '__main__':
    root = Tk()
    gui = CharDbGui(root)
    root.wm_state('zoomed')
    gui.launch()

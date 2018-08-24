from tkinter import *
from tkinter import ttk
import backend as bk
from PIL import Image, ImageTk
from tabbeddisplay import TabbedDisplay

_table = bk._table
_db = bk._db


class CharDbGui(Frame):
    # Mage character database object
    def __init__(self, root, database=None, *args, **kwargs):
        Frame.__init__(self, root, *args, **kwargs)
        self.root = root
        self.database = database  # source of data for populating lists

        ### Broad layout into frames first -- color-coded for ease of debugging ###
        self.rowweight(range(1, 5), [10, 40, 40, 10])
        self.colweight(range(1, 4), [25, 75, 25])
        top_toolbar = Frame(self, bg="green", height=50, width=1)
        top_toolbar.grid(row=1, column=1, columnspan=4, sticky=E+W+N+S)

        leftbox = Frame(self, height=1, width=1)
        leftbox.grid(row=2, column=1, rowspan=2, sticky=N+S+E+W)

        midbox = Frame(self, height=1, width=1)
        midbox.grid(row=2, column=2, rowspan=2, sticky=N+S+E+W)

        righttopbox = Frame(self, bg="black", height=1, width=1)
        righttopbox.grid(row=2, column=3, sticky=N+S+E+W)

        rightbottombox = Frame(self, bg="purple", height=1, width=1)
        rightbottombox.grid(row=3, column=3, sticky=N+S+E+W)

        bottombox = Frame(self, bg="orange", height=1, width=1)
        bottombox.grid(row=4, column=1, columnspan=4, sticky=N+S+E+W)

        ### Create hierarchical list at left edge ###
        self.tree = ttk.Treeview(leftbox, selectmode='browse')
        self.tree.heading('#0', text='DATABASE')
        self.tree.pack(expand=True, side=LEFT, fill=BOTH)

        # Create scrollbar for self.tree just to its right #
        scrollbar = Scrollbar(leftbox)
        scrollbar.pack(side=LEFT, fill=Y)

        # Link sb_etl to self.tree
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.tree.yview)

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

        ### Middle frame: Create display area that can accommodate multiple tabs
        self.mainbox = TabbedDisplay(midbox)
        self.display_frames = []
        self.display_frames.append(Frame())
        self.canvases = []
        for i, frame in enumerate(self.display_frames):
            label = "<blank>"
            self.mainbox.add(frame, text=label)
            self.canvases.append(Canvas(frame, bg='white'))
            self.canvases[i].pack(side=LEFT, expand=True, fill=BOTH)
            # Create vertical scrollbar for canvas
            sb = Scrollbar(frame)
            sb.pack(side=LEFT, fill=Y)
            # Link new scrollbar to canvas
            self.canvases[i].configure(yscrollcommand=sb.set)
            sb.configure(command=self.canvases[i].yview)
            # Link mousewheel scrolling to canvas when mouse hovered in its bounds.
            self.canvases[i].bind("<MouseWheel>", self.scroll_canvas)
            # Bind display to update when user changes character selection and to open in new
            # tab when user double-clicks on a character entry.
            self.tree.bind('<Double-Button-1>', self.display_selection)
            self.tree.bind('<Control-Double-Button-1>',
                           self.display_selection_newtab)
        self.mainbox.pack(expand=True, fill=BOTH)

        ### Create placeholder textbox in right bottom frame ###
        reserved = Text(rightbottombox, bg="purple", width=1)
        reserved.pack(expand=True, fill=BOTH)

        ### Create log output box at bottom of screen
        logbox = Text(bottombox, height=6, width=80, bg="orange")
        logbox.pack(expand=True, fill=BOTH)

        # Fill with sample data to test
        if not self.database:
            self.fill_defaults()

        # add self to root
        self.pack(expand=True, fill=BOTH)

    def rowweight(self, index, weight):
        # Adjust weight(s) of row(s).
        if type(index) == int:  # Singleton case
            assert(type(weight) == int)
            self.grid_rowconfigure(index, weight=weight)
        else:  # Range case
            assert(len(index) == len(weight))
            for i, w in zip(index, weight):
                self.grid_rowconfigure(i, weight=w)

    def colweight(self, index, weight):
        # Adjust weight(s) of column(s).
        if type(index) == int:  # Singleton case
            assert(type(weight) == int)
            self.grid_columnconfigure(index, weight=weight)
        else:  # Range case
            assert(len(index) == len(weight))
            for i, w in zip(index, weight):
                self.grid_columnconfigure(i, weight=w)

    def fill_defaults(self):
        # Placeholder values to test with
        self.root.title("Test Database")
        # Populate the list with some initial values
        initvals_etl = ["Characters", "Items"]
        for x in initvals_etl:
            self.tree.insert('', END, x, text=str(x))
        char_names = bk.get_rows(col='name', table=_table, db=_db)
        for x in [x[0] for x in char_names]:
            self.tree.insert('Characters', END, x, text=x, tag='char')
        y = self.tree.insert('', END, "nums", text="Numbers")
        for x in range(100):
            self.tree.insert(y, END, x, text=str(x))

        ### For debugging; will disable later
        # self.tree.bind('<<TreeviewSelect>>', self.report)

    def report(self, event):
        curr_item = self.tree.focus()
        print(self.tree.item(curr_item))

    def display_selection(self, event):
        """
        WORK IN PROGRESS!
        Updates current display window to show info for selected character.

        TODO:
        - Handle selections other than characters.
        - Make better tags
        """
        # Get canvas object
        frameId = self.mainbox.select()
        frame = self.mainbox.nametowidget(frameId)
        try:
            canvas = self.mainbox.nametowidget(frameId + ".!canvas")
        except KeyError:
            self.display_selection_newtab(event)
            return

        # First clear previous contents
        canvas.delete(canvas.find_all())
        # Then display selected character info
        curr_item = self.tree.item(self.tree.focus())
        if 'char' in curr_item['tags']:
            (labels, vals) = self.get_char_info(curr_item['text'])
            (TT, char) = self.format_chardata(labels, vals)
            canvas.create_text(5, 0, text=TT, anchor=NW, tag='text')
            canvas.config(scrollregion=canvas.bbox(ALL))
            canvas.xview_moveto(0)
            canvas.yview_moveto(0)
            self.mainbox.tab(frameId, text=char['name'])

    def display_selection_newtab(self, event):
        frame = Frame()
        self.display_frames.append(frame)
        self.mainbox.add(frame)
        self.mainbox.select(frame)
        # Add canvas to frame
        canvas = Canvas(frame, bg='white')
        self.canvases.append(canvas)
        canvas.pack(side=LEFT, expand=True, fill=BOTH)
        # TODO: Get character info
        curr_item = self.tree.item(self.tree.focus())
        if 'char' in curr_item['tags']:
            (labels, vals) = self.get_char_info(curr_item['text'])
            (TT, char) = self.format_chardata(labels, vals)
        # TODO: Handle non-character types
        # Add text to canvas
        canvas.create_text(5, 0, text=TT, anchor=NW, tag='text')
        canvas.config(scrollregion=canvas.bbox(ALL))
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        # Add label to tab
        self.mainbox.tab(frame, text=char['name'])
        # Create vertical scrollbar for canvas
        sb = Scrollbar(frame)
        sb.pack(side=RIGHT, fill=Y)
        # Link new scrollbar to canvas
        canvas.configure(yscrollcommand=sb.set)
        sb.configure(command=canvas.yview)
        # Link mousewheel scrolling to canvas when mouse hovered in its bounds.
        canvas.bind("<MouseWheel>", self.scroll_canvas)

    def format_chardata(self, labels, vals):
        """
        Temporary formatting for character data display
        """
        if len(vals) == 1:
            vals = list(vals[0])
        else:
            # TODO: Handle this case
            pass
        lines = []
        char = {}
        for lab, val in zip(labels, vals):
            lines.append(lab + ": " + str(val))
            char[lab] = val
        T = "\n".join(lines)
        return (T, char)

    def scroll_canvas(self, event):
        frameId = self.mainbox.select()
        canvas = self.mainbox.nametowidget(frameId + ".!canvas")
        canvas.yview_scroll(int(-1*event.delta/120), "units")

    def get_char_info(self, name=None):
        vals = bk.get_rows("name=='"+name+"'", table=_table, db=_db)
        labels = bk.get_col_headers(table=_table, db=_db)
        return (labels, vals)

    def launch(self):
        self.root.mainloop()


if __name__ == '__main__':
    root = Tk()
    gui = CharDbGui(root)
    root.wm_state('zoomed')
    gui.launch()

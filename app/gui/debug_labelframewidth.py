import tkinter as tk
from tkinter import ttk


class App(tk.Frame):
    def __init__(self, *args, sb_width=20, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.lf1 = tk.LabelFrame(self, text="BOX 1")
        self.lf2 = tk.LabelFrame(self, text="BOX 2")
        self.lf1.grid(row=0, column=0)
        self.lf2.grid(row=1, column=0)

        for i in range(3):
            for j in range(4):
                tk.Button(self.lf1, text="I am a button taking up space").grid(
                    row=i, column=j)

        for i in range(4):
            for j in range(5):
                tk.Button(self.lf2, text="I am also a button taking up space").grid(
                    row=i, column=j)

        self.bind('<Configure>', self.__eq_size)

    def __eq_size(self, event):
        try:
            if self.lf1.winfo_width() + int(str(self.lf1.cget('padx')))*2 != self.lf2.winfo_width():
                self.lf1.config(padx=(self.lf2.winfo_width() -
                                      self.lf1.winfo_width())/2)
        except:
            pass


class Scrollable(ttk.Frame):
    def __init__(self, frame, width=16):
        scrollbar = tk.Scrollbar(frame, width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)
        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.canvas.yview)
        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame)

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(
            0, 0, window=self, anchor=tk.NW)

    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"
        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width=canvas_width)

    def update(self):
        "Update the canvas and the scrollregion"
        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))

    def scroll_canvas(self, event):
        self.canvas.yview_scroll(int(-1*event.delta/120), "units")


### TEST CODE ###
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.pack(expand=True, fill='both')
    root.mainloop()

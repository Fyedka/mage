import tkinter as tk
from tkinter import ttk


class App(tk.Frame):
    def __init__(self, *args, sb_width=20, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.lf1 = tk.LabelFrame(self, text="BOX 1")
        self.lf2 = tk.LabelFrame(self, text="BOX 2")
        self.lf3 = tk.LabelFrame(self, text="BOX 3")
        self.lf1.grid(row=0, column=0)
        self.lf2.grid(row=1, column=0)
        self.lf3.grid(row=2, column=0)

        for i in range(3):
            for j in range(4):
                tk.Button(self.lf1, text="I am a button taking up space").grid(
                    row=i, column=j)

        for i in range(4):
            for j in range(5):
                tk.Button(self.lf2, text="I am also a button taking up space").grid(
                    row=i, column=j)

        for i in range(2):
            for j in range(2):
                tk.Button(self.lf3, text="ME TOO!").grid(row=i, column=j)

        self.bind('<Configure>', self.__on_configure)

    def __on_configure(self, event):
        self.after_idle(self.__eq_size, event)

    def __eq_size(self, event):
        w = list()
        lfs = [self.lf1, self.lf2, self.lf3]
        for lf in lfs:
            w.append(lf.winfo_width())
        w_max = max(w)

        for lf in lfs:
            try:
                if lf.winfo_width() + int(float(str(lf.cget('padx'))))*2 < w_max:
                    lf.config(padx=(w_max - lf.winfo_width())/2)
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

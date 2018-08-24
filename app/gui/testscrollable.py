import tkinter as tk
from tkinter import ttk
from scrollable import Scrollable
import charsheet as cs

### SET TEST TYPE ###
test_type = 3

### TEST 1 - SMALL, PREPACKAGED ###################################################
if test_type == 1:
    root = tk.Tk()

    header = ttk.Frame(root)
    body = ttk.Frame(root)
    footer = ttk.Frame(root)
    header.pack()
    body.pack()
    footer.pack()

    ttk.Label(header, text="The header").pack()
    ttk.Label(footer, text="The Footer").pack()

    scrollable_body = Scrollable(body, width=32)

    for i in range(30):
        ttk.Button(scrollable_body,
                   text="I'm a button in the scrollable frame").grid()

    scrollable_body.update()

    root.mainloop()

### TEST 2 - CHARSHEET 1 ##############################################################
"""
    This one works, saving for reference.

    TODO: Make scrollable in horizontal direction when dynamic window size makes it
    desirable (currently only works for vertical).

    TODO: Test if mousewheel scrolling works.
"""
if test_type == 2:
    root = tk.Tk()
    mainframe = ttk.Frame(root)
    mainframe.pack(expand=True, fill='both')

    scrollable = Scrollable(mainframe, width=20)

    char = cs.CharSheet(scrollable)
    char.grid(sticky='NEWS')
    scrollable.update()
    root.mainloop()

### TEST 3 - CHARSHEET 2 ###############################################################
"""
    RESULTS
    - Packing of mainframe can happen either before OR after Scrollable creation.
"""
if test_type == 3:
    root = tk.Tk()
    mainframe = ttk.Frame(root)
    scrollable = Scrollable(mainframe, width=20)

    mainframe.pack(expand=True, fill='both')

    char = cs.CharSheet(scrollable)
    char.grid(sticky='NEWS')
    scrollable.update()
    root.mainloop()
########################################################################################

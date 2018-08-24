from tkinter import *
from tkinter import ttk


### FUNCTIONS ###
def find_all_descendants(widget, max_depth=-1):
    """Get all descendants (to optionally limited depth) of a widget"""
    if 'winfo_children' not in dir(widget):
        print("'widget' is not a widget - an error will be thrown.")

    return_list = list()

    children = widget.winfo_children()
    if children and max_depth != 0:
        for child in children:
            return_list.append(child)
            return_list = return_list + \
                find_all_descendants(child, max_depth-1)

    return return_list

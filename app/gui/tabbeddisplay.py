import tkinter as tk
from tkinter import ttk

# TODO: Figure out how to make tab background change to this (or any other) color.
BG_GRAY_LIGHT = "#f0f0f0"


class TabbedDisplay(ttk.Notebook):
    """ Like a ttk Notebook, but with close buttons on each tab."""

    __initialized = False

    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__initialized = True

        kwargs["style"] = "TabbedDisplay"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

        ### Temporary for debugging ###
        self.bind("<ButtonPress-3>", self.report, True)

    ### Just for debugging ###
    def report(self, event):
        """Right-click on an element in the TabbedDisplay to print info about it.
        (Used for debugging)"""
        elem = self.identify(event.x, event.y)
        print(elem)
        s = ttk.Style()
        bg = s.lookup("TabbedDisplay." + elem, "background")
        print(bg)
        return

    def on_close_press(self, event):
        """Called when the left mouse button is clicked over the close button."""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index

    def on_close_release(self, event):
        """Called when left mouse button is released over the close button."""
        if not self.instate(['pressed']):
            return

        element = self.identify(event.x, event.y)
        index = self.index("@%d,%d" % (event.x, event.y))

        if "close" in element and self._active == index:
            self.forget(index)
            self.event_generate("<<DisplayTabClosed>>")

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                             ("active", "pressed", "!disabled", "img_closepressed"),
                             ("active", "!disabled", "img_closeactive"),
                             border=8, sticky=''
                             )

        style.layout("TabbedDisplay", [
                 ("TabbedDisplay.client", {"sticky": "nswe"})])
        style.layout("TabbedDisplay.Tab", [
            ("TabbedDisplay.tab", {
                "sticky": "nswe",
                "children": [
                    ("TabbedDisplay.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("TabbedDisplay.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("TabbedDisplay.label", {
                                        "side": "left", "sticky": ''}),
                                    ("TabbedDisplay.close", {
                                        "side": "left", "sticky": ''}),
                                    ]
                            })
                        ]
                    })
                ]
            })
        ])

class TripleHeader(Frame):
    """Subheader for stat name, #dots, and specialization (if any).
    Argument 'opts' should be list of dictionaries (for Label(**kwargs))."""

    def __init__(self, master=None, cnf={}, *args, opts=[],
                 **kwargs):
        """TripleHeader constructor"""

        super().__init__(master, cnf, *args, **kwargs)

        ### OVERRIDE DEFAULTS ###
        default_labels = ["", "Dots", "Specialization"]
        default_widths = [30, 4, 30]

        for i in range(0, 3):
            try:
                opt = opts[i]
            except:
                opt = dict()
            if not "text" in opt:
                opt["text"] = default_labels[i]
            sh = Label(self, **opt)
            sh.grid(row=0, column=i)

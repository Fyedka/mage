from tkinter import *
from tkinter import ttk
from scrollable import Scrollable


class CharSheet(Frame):
    """Mage character sheet laid out for screen viewing
    TODO:
    - First get look right for viewing.
       --> Need x-padding between the LabelEntry boxes.
       --> Add LabelFrames around sections.
       --> Edit window title.
    - Enable filling in values from database entries
    - Enable reading in of user values to variables and storing of results.
    - Validate user entries.
    - Add "Save to database" button.
    - Make entries change to static label when not in focus.
    - Make exportable as PDF.

    """

    def __init__(self, *args, **kwargs):
        ### DEFAULTS ###
        # if "height" not in kwargs:
        #     kwargs["height"] = 600

        Frame.__init__(self, *args, **kwargs)

        # self.content = Frame(*args, **kwargs)
        self.root = self.winfo_parent()

        ### Create sections (SELF version) ###
        self.general_info_section = GeneralInfoForm(self)
        self.attributes_section = AttributesForm(self)
        self.abilities_section = AbilitiesForm(self)
        self.spheres_section = SpheresForm(self)
        self.advantages_section = AdvantagesForm(self)

        # ### Create sections (SELF.CONTENT version)
        # self.general_info_section = GeneralInfoForm(self.content)
        # self.attributes_section = AttributesForm(self.content)
        # self.abilities_section = AbilitiesForm(self.content)
        # self.spheres_section = SpheresForm(self.content)
        # self.advantages_section = AdvantagesForm(self.content)

        ### Pack sections from top to bottom ###
        self.general_info_section.pack(side=TOP, expand=True, fill=BOTH)
        self.attributes_section.pack(side=TOP, expand=True, fill=BOTH)
        self.abilities_section.pack(side=TOP, expand=True, fill=BOTH)
        self.spheres_section.pack(side=TOP, expand=True, fill=BOTH)
        self.advantages_section.pack(side=TOP, expand=True, fill=BOTH)

        # ### Put on a canvas to allow scrolling ###
        # canvas = Canvas(self)
        # # canvas.grid(column=1, row=1, sticky='NEWS')
        # canvas.pack(side=LEFT, expand=True, fill=BOTH)
        # canvas.create_window(0, 0, anchor=NW, window=self.content)

        # ### Try adding scrollbar to self ###
        # sb = Scrollbar(self, width=20)
        # sb.pack(side=LEFT, expand=True, fill=Y, anchor=W)
        # # sb.grid(column=2, row=1, sticky='NS')
        # # Connect canvas and scrollbar
        # canvas.configure(yscrollcommand=sb.set)
        # sb.configure(command=canvas.yview)
        # canvas.config(height=canvas.winfo_reqheight())
        # self.content.config(height=canvas.winfo_height())
        # self.config(height=self.content.winfo_height())
        # canvas.config(scrollregion=canvas.bbox(ALL))

        # # Mousewheel scrolling
        # canvas.bind("<MouseWheel>", self.scroll_canvas)

        # # Pack self in main application window
        # self.pack(expand=True, fill=BOTH)

        ### DEBUGGING EXTRAS ########################################
        self.bind_all("<ButtonPress-1>", func=self.report, add=True)
        # self.canvas = canvas
        #############################################################

    # def scroll_canvas(self, event):
    #     self.canvas.yview_scroll(int(-1*event.delta/120), "units")

    def show(self):
        """Show character sheet"""
        self.root.mainloop()
        return

    def report(self, event):
        """Get info about objects when clicking on them (For debugging).
        Customize as needed"""
        (x, y) = self.winfo_pointerxy()
        w = self.winfo_containing(x, y)
        rootx = w.winfo_rootx()
        rooty = w.winfo_rooty()
        height = w.winfo_height()
        width = w.winfo_width()
        reqheight = w.winfo_reqheight()
        reqwidth = w.winfo_reqwidth()
        geometry = w.winfo_geometry()
        try:
            pady = w.cget('pady')
        except:
            pady = None
        print("Name: " + str(w))
        print("Pointer: " + str(x) + ',' + str(y))
        print("reqheight: " + str(reqheight))
        print("height: " + str(height))
        print("reqwidth: " + str(reqwidth))
        print("width: " + str(width))
        print("geometry: " + str(geometry))
        print("pady: " + str(pady))
        # f1 = self.nametowidget("!advantagesform.!labelframe.!frame")
        # f2 = self.nametowidget("!advantagesform.!labelframe.!frame2")
        # print(f1.winfo_geometry())
        # print(f2.winfo_geometry())
        # print(f2.keys())


class GeneralInfoForm(Frame):
    """Topmost part of character sheet"""

    def __init__(self, master=None, *args, padx_ext=8, pady_ext=8, **kwargs):
        """GeneralInfoForm constructor"""
        ### OVERRIDE DEFAULTS ###
        if "text" not in kwargs:
            kwargs["text"] = "General Info"
        if "padx" not in kwargs:
            kwargs["padx"] = 5
        if "pady" not in kwargs:
            kwargs["pady"] = 8

        # Frame for external padding only
        super().__init__(master, padx=padx_ext, pady=pady_ext)

        # LabelFrame for main contents
        self.label_frame = LabelFrame(self, *args, **kwargs)
        charname_box = LabelEntry(
            self.label_frame, label_opts={"text": "Character Name: "})
        playername_box = LabelEntry(self.label_frame, label_opts={
                                    "text": "Player Name: "})
        chronicle_box = LabelEntry(self.label_frame, label_opts={
                                   "text": "Chronicle: "})
        nature_box = LabelEntry(
            self.label_frame, label_opts={"text": "Nature: "})
        essence_box = LabelEntry(self.label_frame, label_opts={
                                 "text": "Essence: "})
        demeanor_box = LabelEntry(self.label_frame, label_opts={
                                  "text": "Demeanor: "})
        tradition_box = LabelEntry(self.label_frame, label_opts={
                                   "text": "Tradition: "})
        mentor_box = LabelEntry(
            self.label_frame, label_opts={"text": "Mentor: "})
        cabal_box = LabelEntry(
            self.label_frame, label_opts={"text": "Cabal: "})

        charname_box.grid(row=1, column=1, sticky='nsew')
        playername_box.grid(row=2, column=1, sticky='nsew')
        chronicle_box.grid(row=3, column=1, sticky='nsew')
        nature_box.grid(row=1, column=2, sticky='nsew')
        essence_box.grid(row=2, column=2, sticky='nsew')
        demeanor_box.grid(row=3, column=2, sticky='nsew')
        tradition_box.grid(row=1, column=3, sticky='nsew')
        mentor_box.grid(row=2, column=3, sticky='nsew')
        cabal_box.grid(row=3, column=3, sticky='nsew')

        self.label_frame.pack(expand=True, fill=BOTH)


class AttributesForm(Frame):
    """Attributes section of character sheet"""

    def __init__(self, master=None, cnf={}, *args, padx_ext=8, pady_ext=8, **kwargs):
        """AttributesForm constructor"""
        ### OVERRIDE DEFAULTS ###
        if "text" not in kwargs:
            kwargs["text"] = "Attributes"
        if "padx" not in kwargs:
            kwargs["padx"] = 5
        if "pady" not in kwargs:
            kwargs["pady"] = 8

        # Frame for external padding only
        super().__init__(master, padx=padx_ext, pady=pady_ext)

        # LabelFrame for main contents
        self.label_frame = LabelFrame(self, cnf, *args, **kwargs)

        # Column headers
        font = ("TkHeadingFont", 10, 'underline')
        self.label_frame.headers = [
            Label(self.label_frame, text="Physical", font=font),
            Label(self.label_frame, text="Social", font=font),
            Label(self.label_frame, text="Mental", font=font)
        ]
        for i, header in enumerate(self.label_frame.headers):
            header.grid(column=i, row=0)
        subheaders = ["", "Dots", "Specialization"]

        attributes = [
            ["Strength", "Dexterity", "Stamina"],
            ["Charisma", "Manipulation", "Appearance"],
            ["Perception", "Intelligence", "Wits"]
        ]
        self.lde = list()  # List of LabelDoubleEntry children
        for i in range(0, len(attributes)):
            atts = attributes[i]
            for j in range(0, len(atts)):
                if j == 0:
                    sh = subheaders
                else:
                    sh = None
                att = LabelDoubleEntry(
                    self.label_frame, label_opts={"text": atts[j] + ": "},
                    headers=sh)
                att.grid(column=i, row=1+j)
                try:
                    self.lde[j].insert(i, att)
                except IndexError:
                    self.lde.insert(j, list())
                    self.lde[j].insert(i, att)

        for x in self.lde:
            x[0].columnconfigure(1, minsize=60)
            x[2].columnconfigure(1, minsize=75)

        self.label_frame.pack(fill=BOTH, expand=True)


class AbilitiesForm(Frame):
    """Abilities section of character sheet"""

    def __init__(self, master=None, cnf={}, *args, padx_ext=8, pady_ext=8, **kwargs):
        """AbilitiesForm constructor"""
        ### OVERRIDE DEFAULTS ###
        if "text" not in kwargs:
            kwargs["text"] = "Abilities"
        if "padx" not in kwargs:
            kwargs["padx"] = 5
        if "pady" not in kwargs:
            kwargs["pady"] = 8

        # Frame for external padding only
        super().__init__(master, padx=padx_ext, pady=pady_ext)

        # LabelFrame for main contents
        self.label_frame = LabelFrame(self, cnf, *args, **kwargs)

        # Column headers
        font = ("TkHeadingFont", 10, 'underline')
        self.label_frame.headers = [
            Label(self.label_frame, text="Talents", font=font),
            Label(self.label_frame, text="Skills", font=font),
            Label(self.label_frame, text="Knowledges", font=font)
        ]
        for i, header in enumerate(self.label_frame.headers):
            header.grid(column=i, row=0)

        talents = ["Alertness", "Athletics", "Awareness", "Brawl", "Dodge", "Expression",
                   "Instruction", "Intuition", "Intimidation", "Streetwise", "Subterfuge"]
        skills = ["Do", "Drive", "Etiquette", "Firearms", "Leadership", "Meditation",
                  "Melee", "Research", "Stealth", "Survival", "Technology"]
        knowledges = ["Computer", "Cosmology", "Culture", "Enigmas", "Investigation",
                      "Law", "Linguistics", "Lore", "Medicine", "Occult", "Science"]
        subheaders = ["", "Dots", "Specialization"]

        abilities = [talents, skills, knowledges]
        self.lde = list()
        for i in range(0, len(abilities)):
            abils = abilities[i]
            for j in range(0, len(abils)):
                if j == 0:
                    sh = subheaders
                else:
                    sh = None
                abil = LabelDoubleEntry(
                    self.label_frame, label_opts={"text": abils[j] + ": "},
                    headers=sh)
                abil.grid(column=i, row=1+j)
                try:
                    self.lde[j].insert(i, abil)
                except IndexError:
                    self.lde.insert(j, list())
                    self.lde[j].insert(i, abil)

        for x in self.lde:
            x[0].columnconfigure(1, minsize=77)
            x[1].columnconfigure(1, minsize=75)
            x[2].columnconfigure(1, minsize=80)

        self.label_frame.pack(fill=BOTH, expand=True)


class SpheresForm(Frame):
    """Spheres section of character sheet"""

    def __init__(self, master=None, cnf={}, *args, padx_ext=8, pady_ext=8, **kwargs):
        """SpheresForm constructor"""
        ### OVERRIDE DEFAULTS ###
        if "text" not in kwargs:
            kwargs["text"] = "Spheres"
        if "padx" not in kwargs:
            kwargs["padx"] = 5
        if "pady" not in kwargs:
            kwargs["pady"] = 8

        # Frame for external padding only
        super().__init__(master, padx=padx_ext, pady=pady_ext)

        # LabelFrame for main contents
        self.label_frame = LabelFrame(self, cnf, *args, **kwargs)

        # Column headers and subheaders
        subheaders = ["", "Dots", "Focus"]

        spheres = [
            ["Correspondence", "Entropy", "Forces"],
            ["Life", "Mind", "Matter"],
            ["Prime", "Spirit", "Time"]
        ]
        self.lde = list()
        for i in range(0, len(spheres)):
            sphrs = spheres[i]
            for j in range(0, len(sphrs)):
                if j == 0:
                    sh = subheaders
                else:
                    sh = None
                sphr = LabelDoubleEntry(
                    self.label_frame, label_opts={"text": sphrs[j] + ": "},
                    headers=sh)
                sphr.grid(column=i, row=1+j)
                try:
                    self.lde[j].insert(i, sphr)
                except IndexError:
                    self.lde.insert(j, list())
                    self.lde[j].insert(i, sphr)

        for x in self.lde:
            x[0].columnconfigure(1, minsize=99)
            x[1].columnconfigure(1, minsize=47)
            x[2].columnconfigure(1, minsize=45)

        self.label_frame.pack(fill=BOTH, expand=True)


class AdvantagesForm(Frame):
    """Advantages and Misc section of character sheet.
    - Quintessence, Paradox, Health, Arete, Willpower (current and max), Combat,
    Backgrounds, Experience"""

    def __init__(self, master=None, cnf={}, *args, padx_ext=8, pady_ext=8, **kwargs):

        ### OVERRIDE DEFAULTS ###
        if "text" not in kwargs:
            kwargs["text"] = "Advantages / Miscellaneous"
        if "padx" not in kwargs:
            kwargs["padx"] = 5
        if "pady" not in kwargs:
            kwargs["pady"] = 8
        hfont = ('TkHeadingFont', 10, 'underline')
        width1 = 15
        minpixels1 = 83

        # Frame for external padding only
        super().__init__(master, padx=padx_ext, pady=pady_ext)

        # LabelFrame for main contents
        self.label_frame = LabelFrame(self, cnf, *args, **kwargs)

        ### Construct label frame contents ###
        # Construct "Backgrounds"
        self.backgrounds = Frame(self.label_frame)
        self.backgrounds.header = Label(self.backgrounds, text="Backgrounds",
                                        font=hfont)
        self.backgrounds.header.pack(side=TOP, anchor=N)
        self.backgrounds.sh_list = ["Name", "Dots"]
        self.backgrounds.bg = list()
        self.backgrounds.bg.insert(0, DoubleEntry(self.backgrounds,
                                                  headers=self.backgrounds.sh_list,
                                                  entry1_opts={"width": width1}))
        for i in range(0, 5):
            if i > 0:
                self.backgrounds.bg.insert(i, DoubleEntry(
                    self.backgrounds, entry1_opts={"width": width1}))
            self.backgrounds.bg[i].pack(side=TOP, expand=True, fill=BOTH)

        ### Construct "Willworking" ###
        self.will = Frame(self.label_frame,
                          height=138)
        self.will.grid_propagate(0)
        # Section Header
        self.will.header = Label(
            self.will, text="Willworking", font=hfont)
        self.will.header.pack(side=TOP, anchor=N)
        # Arete
        self.will.arete = LabelEntry(self.will, label_opts={"text": "Arete: "},
                                     entry_opts={"width": 5})
        self.will.arete.columnconfigure(1, weight=0, minsize=minpixels1)
        self.will.arete.pack(side=TOP, expand=True, fill=BOTH, anchor='center')
        # Quintessence
        self.will.quint = LabelEntry(self.will, label_opts={"text": "Quintessence: "},
                                     entry_opts={"width": 5})
        self.will.quint.pack(side=TOP, expand=True, fill=BOTH, anchor='center')
        self.will.quint.columnconfigure(1, weight=0, minsize=minpixels1)
        # Paradox
        self.will.paradox = LabelEntry(self.will, label_opts={"text": "Paradox: "},
                                       entry_opts={"width": 5})
        self.will.paradox.pack(side=TOP, expand=True,
                               fill=BOTH, anchor='center')
        self.will.paradox.columnconfigure(1, weight=0, minsize=minpixels1)
        # Willpower
        self.will.power = LabelDoubleEntry(self.will, headers=["", "Curr.", "Max."],
                                           label_opts={
                                               "text": "Willpower: ", 'pady': 0},
                                           entry1_opts={"width": 5},
                                           entry2_opts={"width": 5}, pady=0)
        self.will.power.pack(side=BOTTOM, anchor=N, expand=True, fill=BOTH)
        self.will.power.columnconfigure(1, weight=0, minsize=65)
        for h in self.will.power.headers:
            h['font'] = ('TkHeadingFont', 8)

        # Construct "Armed Combat"
        self.combat = Frame(self.label_frame)
        self.combat.header = Label(self.combat, text="Armed Combat",
                                   font=hfont)
        self.combat.header.pack(side=TOP, anchor=N)
        self.combat.sh_list = ["Weapon", "Diff.", "Dmg."]
        self.combat.weapons = list()
        self.combat.weapons.insert(0, TripleEntry(self.combat,
                                                  headers=self.combat.sh_list,
                                                  entry1_opts={"width": width1}))
        for h in self.combat.weapons[0].headers:
            if h['text'] != 'Weapon':
                h['font'] = ('TkHeadingFont', 8)

        for i in range(0, 5):
            if i > 0:
                self.combat.weapons.insert(i, TripleEntry(
                    self.combat, entry1_opts={"width": width1}))
            self.combat.weapons[i].pack(side=TOP, expand=True, fill=BOTH)

        ### Construct "Health" ###
        # TODO: Figure out how to make a tri-state checkbox that uses an X for regular
        # damage and an A for aggravated damage.
        # TODO: Figure out how to have lower injury levels checked and grayed out.
        # TODO: Mouseover tooltips.
        levels = ['Bruised (-0)', 'Hurt (-1)', 'Injured (-1)', 'Wounded(-2)',
                  'Mauled (-2)', 'Crippled(-5)', 'Incapacitated', 'Dead']
        self.health = Frame(self.label_frame)
        self.health.header = Label(self.health, text="Health",
                                   font=hfont)
        self.health.header.grid(row=0, column=1, columnspan=2, sticky='new')
        self.health.level = list()
        self.health.checkbox = list()
        for i, lvl in enumerate(levels):
            self.health.level.insert(i, Label(self.health, text=lvl, pady=0))
            self.health.level[i].grid(row=1+i, column=1, sticky='w')
            self.health.checkbox.insert(
                i, Checkbutton(self.health, pady=0, bd=1))
            self.health.checkbox[i].grid(row=1+i, column=2, sticky='e')
            self.health.rowconfigure(1+i, minsize=0)

        ### Construct "Growth" ###
        # Experience and freebie points, unspent and total.
        self.growth = Frame(self.label_frame)
        self.growth.header = Label(self.growth, text="Growth", font=hfont)
        self.growth.header.pack(side=TOP, anchor=N)
        self.growth.experience = LabelDoubleEntry(self.growth,
                                                  headers=[
                                                      "", "Unspent", "Total"],
                                                  label_opts={
                                                    "text": "Experience: ", 'pady': 0},
                                                  entry1_opts={"width": 5},
                                                  entry2_opts={"width": 5}, pady=0)
        self.growth.experience.pack(side=TOP)
        self.growth.freebie = LabelDoubleEntry(self.growth,
                                               label_opts={
                                                   "text": "Freebie Pts: "},
                                               entry1_opts={"width": 5},
                                               entry2_opts={"width": 5}, pady=0)
        self.growth.freebie.pack(side=TOP)

        ###TEMP###
        # self.growth['bd'] = 2
        # self.growth['relief'] = GROOVE

        w2 = self.growth.experience.headers[1].winfo_reqwidth()
        w1 = self.growth.freebie.label.winfo_reqwidth()

        self.growth.experience.columnconfigure(0, minsize=0)
        self.growth.freebie.columnconfigure(0, minsize=0)
        self.growth.experience.columnconfigure(1, minsize=w1)
        self.growth.freebie.columnconfigure(1, minsize=w1)
        self.growth.experience.columnconfigure(2, minsize=w2)
        self.growth.freebie.columnconfigure(2, minsize=w2)
        self.growth.experience.columnconfigure(3, minsize=0)
        self.growth.freebie.columnconfigure(3, minsize=0)

        self.growth.experience.label['anchor'] = E
        self.growth.experience.label.grid(sticky=E)
        ###TEMP###
        # self.growth.experience.label['bd'] = 2
        # self.growth.experience.label['relief'] = GROOVE

        self.growth.freebie.label['anchor'] = E
        self.growth.freebie.label.grid(sticky=E)
        ###TEMP##
        # self.growth.freebie.label['bd'] = 2
        # self.growth.freebie.label['relief'] = GROOVE

        self.growth.experience.entry1.grid(sticky='ns')
        self.growth.freebie.entry1.grid(sticky='ns')
        self.growth.experience.entry2.grid(sticky='ns')
        self.growth.freebie.entry2.grid(sticky='ns')

        ### Construct Merits and Flaws ###
        self.mf = Frame(self.label_frame)
        self.mf.header = Label(self.mf, text="Merits & Flaws",
                               font=hfont)
        self.mf.header.pack(side=TOP, anchor=N)
        self.mf.sh_list = ["Name", "Cost"]
        self.mf.item = list()
        self.mf.item.insert(0, DoubleEntry(self.mf,
                                           headers=self.mf.sh_list,
                                           entry1_opts={"width": width1}))
        for i in range(0, 5):
            if i > 0:
                self.mf.item.insert(i, DoubleEntry(
                    self.mf, entry1_opts={"width": width1}))
            self.mf.item[i].pack(side=TOP, expand=True, fill=BOTH)

        ### Arrange label frame contents ###
        self.backgrounds.grid(row=1, column=1, sticky=NS, rowspan=2)
        self.will.grid(row=1, column=2, sticky=NS, rowspan=1)
        self.combat.grid(row=1, column=3, sticky=NS, rowspan=2)
        self.health.grid(row=1, column=4, sticky=NSEW, rowspan=2)
        self.growth.grid(row=2, column=2, sticky=NS, rowspan=1)
        self.mf.grid(row=1, column=5, rowspan=2, sticky=NS)

        # Pack label frame into self
        self.label_frame.pack(expand=True, fill=BOTH)

        #TEMP
        # self.backgrounds['relief'] = GROOVE
        # self.backgrounds['bd'] = 2
        # self.will['relief'] = GROOVE
        # self.will['bd'] = 2
        self.health.checkbox[0]['relief'] = GROOVE


class TripleEntry(Frame):
    """Three connected entries, for things like Weapons, where names, damage, and
     difficulties all vary"""

    def __init__(self, master=None, cnf={}, *args, entry1_opts={},
                 entry2_opts={}, entry3_opts={}, headers=None, **kwargs):

        super().__init__(master, cnf=cnf, **kwargs)

        ### OVERRIDE DEFAULTS ###
        if "width" not in entry1_opts:
            #entry_opts["width"] = 42 - len(label_opts["text"])
            entry1_opts["width"] = 27
        if "width" not in entry2_opts:
            entry2_opts["width"] = 5
        if "width" not in entry3_opts:
            entry3_opts["width"] = 5

        self.entry1 = Entry(self, **entry1_opts)
        self.entry2 = Entry(self, **entry2_opts)
        self.entry3 = Entry(self, **entry3_opts)

        self.entry1.grid(row=1, column=1, sticky='nse')
        self.entry2.grid(row=1, column=2, sticky='nse')
        self.entry3.grid(row=1, column=3, sticky='nse')

        self.columnconfigure(1, minsize=50)
        self.columnconfigure(2, minsize=25)
        self.columnconfigure(3, minsize=25)

        self.config(padx=8)

        self.headers = list()
        if headers:
            it = iter(headers)
            for i in range(0, 3):
                nit = next(it)
                h = Label(self, text=nit, padx=0, pady=1)
                h.grid(column=i+1, row=0, sticky=S)
                self.headers.insert(i, h)

    def config_entry1(self, *args, **kwargs):
        self.entry1.configure(*args, **kwargs)

    def config_entry2(self, *args, **kwargs):
        self.entry2.config(*args, **kwargs)

    def config_entry3(self, *args, **kwargs):
        self.entry3.config(*args, **kwargs)


class DoubleEntry(Frame):
    """Two connected entries, for things like Backgrounds, where names and dots both
    vary."""

    def __init__(self, master=None, cnf={}, *args, entry1_opts={},
                 entry2_opts={}, headers=None, **kwargs):

        super().__init__(master, cnf=cnf, **kwargs)

        ### OVERRIDE DEFAULTS ###
        if "width" not in entry1_opts:
            #entry_opts["width"] = 42 - len(label_opts["text"])
            entry1_opts["width"] = 27
        if "width" not in entry2_opts:
            entry2_opts["width"] = 5

        self.entry1 = Entry(self, **entry1_opts)
        self.entry2 = Entry(self, **entry2_opts)

        self.entry1.grid(row=1, column=1, sticky='nse')
        self.entry2.grid(row=1, column=2, sticky='nse')

        self.columnconfigure(1, minsize=50)
        self.columnconfigure(2, minsize=25)

        self.config(padx=8)

        if headers:
            it = iter(headers)
            for i in range(0, 2):
                nit = next(it)
                # if i == 0:
                #     w = entry1_opts["width"]
                # elif i == 1:
                #     w = entry2_opts["width"]
                h = Label(self, text=nit, padx=0, pady=1)
                h.grid(column=i+1, row=0)

    def config_entry1(self, *args, **kwargs):
        self.entry1.configure(*args, **kwargs)

    def config_entry2(self, *args, **kwargs):
        self.entry2.config(*args, **kwargs)


class LabelEntry(Frame):
    """Simple combination of label widget with entry widget"""

    def __init__(self, master=None, cnf={}, *args, label_opts={},
                 entry_opts={}, headers=None, **kwargs):

        super().__init__(master, cnf=cnf, **kwargs)

        ### OVERRIDE DEFAULTS ###
        if "width" not in entry_opts:
            #entry_opts["width"] = 42 - len(label_opts["text"])
            entry_opts["width"] = 27
        if "anchor" not in label_opts:
            label_opts["anchor"] = E

        self.label = Label(self, **label_opts)
        self.entry = Entry(self, **entry_opts)

        self.label.grid(row=1, column=1, sticky='nse')
        self.entry.grid(row=1, column=2, sticky='nsw')

        self.columnconfigure(1, weight=1, minsize=50)
        self.columnconfigure(2, minsize=50)

        self.config(padx=8)

        if headers:
            it = iter(headers)
            for i in range(0, 2):
                nit = next(it)
                h = Label(self, text=nit)
                h.grid(column=i+1, row=0)

    def config_label(self, *args, **kwargs):
        self.label.configure(*args, **kwargs)

    def config_entry(self, *args, **kwargs):
        self.entry.config(*args, **kwargs)


class LabelDoubleEntry(Frame):
    """Widget composed of one label and two entries.
    Designed for use with stats that have both dots and potentially specializations
    (i.e., attributes, abilities, and spheres."""

    def __init__(self, master=None, cnf={}, *args, label_opts={}, entry1_opts={},
                 entry2_opts={}, headers=None, **kwargs):
        """LabelDoubleEntry constructor."""

        super().__init__(master, cnf, *args, **kwargs)

        ### OVERRIDE DEFAULTS ###
        if "anchor" not in label_opts:
            label_opts["anchor"] = E
        if "width" not in entry1_opts:
            entry1_opts["width"] = 5
        if "width" not in entry2_opts:
            entry2_opts["width"] = 22

        self.label = Label(self, **label_opts)
        self.entry1 = Entry(self, **entry1_opts)
        self.entry2 = Entry(self, **entry2_opts)

        self.label.grid(row=1, column=1, sticky='nse')
        self.entry1.grid(row=1, column=2, sticky='nsw')
        self.entry2.grid(row=1, column=3, sticky='nsw')

        self.columnconfigure(1, weight=1, minsize=90)
        self.columnconfigure(2)
        self.columnconfigure(3)

        self.config(padx=8)

        self.headers = list()
        if headers:
            it = iter(headers)
            for i in range(0, 3):
                nit = next(it)
                h = Label(self, text=nit)
                h.grid(column=i+1, row=0)
                self.headers.insert(i, h)

    def config_label(self, *args, **kwargs):
        self.label.configure(*args, **kwargs)

    def config_entry1(self, *args, **kwargs):
        self.entry1.config(*args, **kwargs)

    def config_entry2(self, *args, **kwargs):
        self.entry2.config(*args, **kwargs)


if __name__ == '__main__':
    ### TEST CODE ###
    root = Tk()
    cs = Scrollable(CharSheet(root))
    cs.nametowidget(cs.winfo_parent()).pack(in_=root, expand=True, fill=BOTH)
    cs.update()
    cs.winfo_toplevel().mainloop()

else:
    ### EXECUTE ON IMPORT ###
    pass

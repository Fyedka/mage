# from characters import Character
from consolemenu import *
from consolemenu.items import *
import backend as dat

### CLASSES ###


class EncounterSetupMenu(ConsoleMenu):
    def __init__(self, char_list=None, db=None, *args, **kwargs):
        super(EncounterSetupMenu, self).__init__(
            title="ENCOUNTER SETUP", subtitle="CHARACTERS AND LOCATIONS", *args, **kwargs)
        self.db = db
        self.char_list = char_list
        # self.prologue_text = self.construct_header()
        item_list = self.build_menu_items()
        for item in item_list:
            self.append_item(item)

    def construct_header(self):
        lines = []
        lines.append("Characters: ")
        if not self.char_list:
            lines.append('None')
        else:
            for char in self.char_list:
                if not char.x or not char.y:
                    lines.append(char.name + " (not placed yet)")
                else:
                    lines.append(char.name + " (%d, %d)" % (char.x, char.y))
        return print("\n".join(lines))

    def build_menu_items(self):
        char_names_db = dat.get_rows(
            col='name', table='characters', db=self.db)
        try:
            char_names_encounter = [char.name for char in self.char_list]
        except TypeError:
            char_names_encounter = []
        for name in char_names_db:
            if name in char_names_encounter:
                char_names_db.remove(name)
        add_character_menu = SelectionMenu(
            char_names_db, title=self.title, subtitle='ADD CHARACTER')
        self.add_character_menu = add_character_menu
        add_character_item = SubmenuItem("Add Character", add_character_menu)
        return [add_character_item]

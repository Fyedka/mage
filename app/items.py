

### FUNCTIONS ###


### CLASSES ###
class Item(object):
    # Generic item object type.

    def __init__(self, **kwargs):
        # Defaults:
        self.name = 'unnamed item'
        self.lb = 1
        self.desc = ''
        self.id = 0
        for key, value in kwargs.items():
            setattr(self, key, value)


class Weapon(Item):
    # Item subtype: Weapon. Has some additional stats.

    def __init__(self, *args, **kwargs):
        super().__init__()
        # Defaults:
        self.id = 0
        self.name = 'punch'
        self.dmg_stat = 'strength'
        self.dmg_offset = 0
        self.atk_ability = 'brawl'
        self.atk_stat = 'dexterity'
        self.conceal = None
        self.difficulty = 6
        self.range = 1
        self.isRanged = False
        self.dmg_base = 0
        self.weight = 0
        for key, value in kwargs.items():
            setattr(self, key, value)

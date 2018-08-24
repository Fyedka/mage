from items import Weapon
from dice import roll
import random
import database as db

### MODULE FUNCTIONS ###


def get_character(name=None, **kwargs):
    # Add character object to memory using info from SQL database.
    result = db.query_unique('characters', 'name', name)
    char = Character(**result)
    return char


def clear_actions(char):
    char.action_queue = None

### CLASSES ###


class Character(object):
    # Simulates a Mage: The Ascension character.

    def __init__(self, **kwargs):
        # Defaults:
        self.id = None
        self.name = 'unnamed character'
        self.strength = 1
        self.dexterity = 1
        self.stamina = 1
        self.brawl = 1
        self.armor_rating = 0
        self.injury_level = 0
        self.weapon = Weapon()
        self.x = 0
        self.y = 0
        self.z = 0
        self.inventory = set()
        for key, value in kwargs.items():
            setattr(self, key, value)

        # Derived stats:
        self.refresh()

    def move(self, x=0, y=0, z=0):
        self.x = self.x + x
        self.y = self.y + y
        self.z = self.z + z

    def set_loc(self, x=None, y=None, z=None):
        if x:
            self.x = x
        if y:
            self.y = y
        if z:
            self.z = z

    def refresh(self):
        # Update/recalculate all derived stats
        # REVISIT THIS TO MAKE SURE THE ORDER IN WHICH THIS HAPPENS MAKES SENSE
        self.injury_mod = db.get_injury(self.injury_level).dice_mod
        self.atk_stat = self.weapon.atk_stat
        self.atk_stat_val = getattr(self, self.atk_stat)
        self.atk_diff = self.weapon.difficulty
        self.atk_abil = self.weapon.atk_ability
        self.atk_abil_val = getattr(self, self.atk_abil)

    def attack(self, target):
        # Attack specified target with equipped weapon.
        # // TO DO: //
        # Some of this might make more sense to bring outward to a broader
        # combat module instead of being contained inside the character.  The
        # character could just return its own attack roll result.
        pass

        # Compile relevant attack stats.
        # // TO DO: //
        # Add in situational modifiers when possible.
        atk_stat_val = self.atk_stat_val
        atk_abil_val = getattr(self, self.weapon.atk_ability)
        atk_diff = self.weapon.difficulty

        # Calculate size of dice pool
        # // TO DO: Subtract injury penalties //
        atk_dicepool = atk_stat_val + atk_abil_val - \
            db.get_injury(self.injury_level).dice_mod

        # // TO DO: //
        # Does attacker choose to save any dice for dodging, etc?
        # Make it random for now until I build an interface for it.
        save_dice = random.randint(0, atk_dicepool-1)

        # Check whether attack succeeds, fails, botches.
        atk = roll(atk_stat_val + atk_abil_val - save_dice, atk_diff)

        # // TO DO: integrate defender dodging here //
        # Can defender dodge? (ie do they have dice left in pool?)
        # Does defender choose to spend on dodging?

        # If attack succeeds, roll damage.
        if atk.total > 0:
            dmg_stat_val = getattr(self, self.weapon.dmg_stat)
            dmg_offset = self.weapon.dmg_offset
            dmg = roll(dmg_stat_val + dmg_offset, 6).total

        # Check how much damage was soaked.
        if dmg > 0:
            soak = roll(target.stamina + target.armor_rating, 6)
            dmg_final = dmg - soak

        # Apply changes to defender's injury level as appropriate.
        if dmg_final > 0:
            target.injury_level = target.injury_level + dmg_final



### TEST CODE ###
b = get_character('Brandon')
print(b.strength)
c = get_character('Crystal')
print(c.strength)

num = int('hello')

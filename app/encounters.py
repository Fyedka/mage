# import characters as ch
from dice import roll
import random
from operator import itemgetter
import consolemenu as cm
import menus

db = r"C:\Users\brand\Dropbox\python\mage\app\resources\mage_2ed_ref.db"

### FUNCTIONS ###


def set_location(something, x, y):
    something.x = x
    something.y = y
    pass


def dodge_only(char):
    # TODO: clear character action queue and set aside full dodge dice.
    ch.clear_actions(char)
    pass


def roll_initiative():
    # Handle initiative phase each round.
    pass


def construct_menu_header(char):
    msg = "Decision phase: %s" % char.name
    msg = msg + "\nActions in queue:"
    if (not "action_queue" in dir(char)) or not char.action_queue:
        msg = msg + "(none)"
        msg = msg + "\nDice pool: (unknown)"
    else:
        msg = msg + ", ".join(char.action_queue)
        msg = msg + "\nDice pool: %d" % char.dice_pool


def declare_actions(char):
    # Create object for main (Tier 1) menu
    encounter_menu = cm.ConsoleMenu(
        "Crystal WOD Tools", "Encounter Helper", prologue_text=construct_menu_header(char))

    ### Create objects for Tier 2 of menus/items ###
    # Add action
    add_action_menu = cm.ConsoleMenu(
        "Encounter Helper", "Add Action", prologue_text=construct_menu_header(char))
    add_action_item = cm.SubMenuItem(
        "Add action to queue", add_action_menu, encounter_menu)
    # Remove action
    remove_action_menu = cm.ConsoleMenu(
        "Encounter Helper", "Remove Action", prologue_text=construct_menu_header(char))
    if len(char.action_queue) > 1:
        remove_action_item = cm.SubMenuItem(
            "Remove action from queue", remove_action_menu, encounter_menu)
    elif len(char.action_queue) == 1:
        remove_action_item = cm.FunctionItem(
            "Remove action from queue", ch.clear_actions, char)
    else:
        remove_action_item = None
    # Re-order actions
    reorder_actions_menu = cm.ConsoleMenu(
        "Encounter Helper", "Re-order Actions", prologue_text=construct_menu_header(char))
    if len(char.action_queue) > 1:
        reorder_actions_item = cm.SubMenuItem(
            "Re-order action queue", reorder_actions_menu, encounter_menu)
    else:
        reorder_actions_item = None
    # Clear action queue
    if len(char.action_queue) > 0:
        clear_actions_item = cm.FunctionItem(
            "Clear action queue", ch.clear_actions, char)
    else:
        clear_actions_item = None
    # Reserve all dice for dodging
    dodge_only_item = cm.FunctionItem(
        "Take no action and reserve all dice for dodging", dodge_only, [char])
    # Accept current action queue
    if len(char.action_queue) > 0:
        accept_queue_item = cm.MenuItem(
            "Accept current action queue for this character", should_exit=True)
    else:
        accept_queue_item = None

    ### Slot Tier 2 items into Tier 1 menu ###
    if add_action_item:
        encounter_menu.append_item(add_action_item)
    if remove_action_item:
        encounter_menu.append_item(remove_action_item)
    if reorder_actions_item:
        encounter_menu.append_item(reorder_actions_item)
    if clear_actions_item:
        encounter_menu.append_item(clear_actions_item)
    if dodge_only_item:
        encounter_menu.append_item(dodge_only_item)
    if accept_queue_item:
        encounter_menu.append_item(accept_queue_item)

    ### "Add Action" Menu ###
    add_action_menu.append_item(cm.SubMenuItem(
        "Move", move_menu, add_action_menu))


### CLASSES ###
class Encounter(object):
    pass

    def __init__(self, char_list=None, *args, map=None, db=None, **kwargs):
        if char_list:
            self.char_list = char_list
        if db:
            self.db = db
        self.setup()
        # self.map = map
        pass

    def add_char(self, *args, **kwargs):
        # TODO: Figure out how to access character list
        # TODO: Figure out how to select character to add
        if selected_character:
            self.char_list.append(selected_character)

    def rm_char(self, *args, **kwargs):
        if selected_character:
            self.char_list.remove(selected_character)

    def setup(self):
        """
        UNFINISHED!
        Launch menu where user selects which characters will be involved in this
        encounter.
        FOR THE FUTURE:
        - Allow map for the encounter to be set here.
        """
        m = menus.EncounterSetupMenu(db=self.db)
        m.show()

    # TODO: Build in support for maps
    # def set_map(self, map):
    #     self.map = map


### General setup of whole encounter ###
# Which characters involved: gets passed in as char_list from character pool.

# enc = Encounter(char_list)


# # TODO: Decide how to read in x and y coordinates of characters
# for ind, char in enumerate(char_list):
#     x = 0
#     y = 0
#     set_location(char_list[ind], x, y)
#
#     # // TODO: Allow ST to adjust difficulty of initiative or set order manually.
#
#     init_diff = 4
#     # Roll initiative for each character
#     for ind, char in enumerate(char_list):
#         # roll initiative
#         dice = char.wits + char.alertness
#         res = roll(dice, init_diff)
#         # Added float should resolve any ties without affecting rest
#         char_list[ind].initiative = res.total + random.uniform(-.4, .4)
#
#     # Declare action(s) for characters in ascending-initiative order.
#     decision_stack = sorted(char_list, key=lambda x: x.initiative)
#     while len(decision_stack) > 0:
#         char = pop(decision_stack, 0)
#
#         # TODO: Figure out what options to give user.  For now: move, attack, dodge.
#
#         # TODO: Get and store user input about what action(s) character is performing.
#
#         # TODO: Store log of character's planned actions
#         char.action_queue
#
#         # TODO: Determine size of dice pool based on action(s).
#
#         # TODO: Split dice pool if applicable.
#
#     # Loop through until all actions resolved
#     for action in range(0, max_actions):
#         pass
#         # Resolve in descending-initiative order
#         for char in initiative_order:
#             pass
#             if char_has_actions_left:
#                 if not action_still_valid:
#                     # Change action (diff + 1)
#                     pass
#                 # Resolve action
#                 pass


if __name__ == '__main__':
    ### TEST CODE ###
    db = r"C:\Users\brand\Dropbox\python\mage\app\resources\mage_2ed_ref.db"
    char_list = None  # TODO: define this list
    Encounter(db=db)
else:
    ### EXECUTE ON IMPORT ###
    pass

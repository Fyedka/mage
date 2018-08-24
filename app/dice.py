import random
from attrdict import AttrDict

### FUNCTIONS ###


def roll(dice=1, difficulty=6):
    # Rolls a given number of dice at a given difficulty and returns relevant
    # information about the outcome.
    result = []
    for x in range(dice):
        result.append(random.randint(1, 10))
    successes = sum([x >= difficulty for x in result])
    ones = sum([x == 1 for x in result])
    if successes == 0:
        if ones:
            msg = str(ones) + " botches!"
            total = -ones
        else:
            msg = 'Failure!'
            total = 0
    elif ones < successes:
        msg = str(successes - ones) + " successes!"
    else:
        msg = "Failure!"
        total = 0
    return AttrDict({'successes': successes,
                     'ones': ones,
                     'total': total,
                     'msg': msg,
                     'raw': result})

    def attempt(char, action):
        pass
        # Look up somehow which attr+ability combo to use based on action.

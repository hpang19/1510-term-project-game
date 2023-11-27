"""
This module includes all features related to the challenges.
"""

from . import FOE_MAP
from random import choice


def check_for_foes(current_room):
    foe = FOE_MAP[current_room[1]]
    level = current_room[0]
    foe = choice(foe[:(level - 1)]) if current_room[1] == 'Street' else foe
    if foe == 'rats':
        random_number = choice(range(4))
    elif foe == 'dogs':
        random_number = choice(range(3))
    elif foe == 'kids':
        random_number = choice(range(2))
    else:
        random_number = 0
    return random_number == 0


def fight_with_foe(current_room, character):
    pass
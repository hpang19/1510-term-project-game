"""
This module includes all features related to the challenges.
"""

from . import FOE_MAP, RATS_WEAPONS
from board import LOCATION_PREFIX
from random import choice


def get_foe(current_room):
    foe = FOE_MAP[current_room[1]]
    level = current_room[0]
    foe = choice(foe[:(level - 1)]) if current_room[1] == 'Street' else foe
    return foe


def check_for_foes(current_room):
    foe = get_foe(current_room)
    if foe == 'rats':
        random_number = choice(range(4))
    elif foe == 'dogs':
        random_number = choice(range(3))
    elif foe == 'kids':
        random_number = choice(range(2))
    else:
        random_number = 0
    return random_number == 0


def selection_in_range(integer, min_value, max_value):
    return True if min_value <= integer <= max_value else False


def rats_challenge(location):
    print(f'There is a rat {LOCATION_PREFIX[location]} {location.lower()}.')
    print('To proceed, you need to kill the rats. Please select a weapon to kill the rats:')
    while True:
        try:
            weapon_id = int(input('[1]: Air Gun  [2]: Pesticides  [3] Hot Water '))
        except TypeError:
            print('You have to input an integer from the list:')
        else:
            if selection_in_range(weapon_id, 1, 3):
                message = RATS_WEAPONS[weapon_id]
                print(message)
                return True
            else:
                print('You have to input an integer from the list:')


def fight_with_foe(current_room, character):
    foe = get_foe(current_room)
    if foe == 'rats':
        return rats_challenge(current_room[1])
    elif foe == 'dogs':
        return
    elif foe == 'kids':
        return
    else:
        return
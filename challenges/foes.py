"""
This module includes all features related to the challenges.
"""

from . import FOE_MAP, RATS_WEAPONS
from board import LOCATION_PREFIX
from .question_bank import math_question
from random import choice


def get_foe(current_room):
    foe = FOE_MAP[current_room[1]]
    level = current_room[0]
    foe = choice(foe[:level]) if current_room[1] == 'Street' else foe
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
    print('To proceed, you need to kill the rats. Please select a weapon to kill the rats from the list:')
    while True:
        try:
            weapon_id = int(input('[1]: Air Gun  [2]: Pesticides  [3] Hot Water '))
        except ValueError:
            print('You have to input an integer from the list:')
        else:
            if selection_in_range(weapon_id, 1, 3):
                message = RATS_WEAPONS[weapon_id]
                print(message)
                if weapon_id != 1:
                    print('Keep trying, Chris! \nPlease select another weapon from the list')
                else:
                    return True
            else:
                print('You have to input an integer from the list:')


def dogs_challenge(location):
    print(f'There is a dog {LOCATION_PREFIX[location]} {location.lower()}.')
    print('Now the dog is trying to attack, you need to decide whether to dodge left or right. Please make a choice:')
    while True:
        try:
            dodge_direction = int(input('You decide to dodge [1]: left  [2]: right '))
        except ValueError:
            print('You have to input an integer from the list:')
        else:
            if selection_in_range(dodge_direction, 1, 2):
                dodge = ["left", "right"][dodge_direction - 1]
                print(f'You are dodging {dodge}.')
                return dodge_direction == choice([1, 2])
            else:
                print('You have to input an integer from the list:')


def kids_challenge(location):
    print(f'There are kids running {LOCATION_PREFIX[location]} {location.lower()}.')
    print('You called school and the teacher comes. The teacher is challenging you with a Math question:')
    challenges = math_question()
    challenge_question = choice(list(challenges.keys()))
    challenge_answer = challenges[challenge_question]
    your_answer = input(f'{challenge_question} ')
    return True if your_answer == challenge_answer else False



def fight_with_foe(current_room, character):
    foe = get_foe(current_room)
    if foe == 'rats':
        rats_challenge(current_room[1])
    elif foe == 'dogs':
        success = dogs_challenge(current_room[1])
    elif foe == 'kids':
        success = kids_challenge(current_room[1])
        print('Successful:', success)
    else:
        return
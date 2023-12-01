"""
This module includes all features related to the challenges.
"""

from . import FOE_MAP, RATS_WEAPONS
from board import LOCATION_PREFIX
from .question_bank import math_question, python_question
from random import choice
import sys
sys.path.append('..')
from GUI import prompts


def get_foe(current_room_description):
    foe = FOE_MAP[current_room_description[1]]
    level = current_room_description[0]
    foe = choice(foe[:level]) if current_room_description[1] == 'Street' else foe
    return foe


def check_for_foes(current_room_description):
    foe = get_foe(current_room_description)
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


def rats_challenge(location, frame):
    print(f'There is a rat {LOCATION_PREFIX[location]} {location.lower()}.')
    print('To proceed, you need to kill the rats. Please select a weapon to kill the rats from the list:')
    while True:
        try:
            if frame:
                weapon_id = int(prompts.Prompts(frame).prompt('[1]: Air Gun  [2]: Pesticides  [3] Hot Water '))
            else:
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


def dogs_challenge(location, frame):
    print(f'There is a dog {LOCATION_PREFIX[location]} {location.lower()}.')
    print('Now the dog is trying to attack, you need to decide whether to dodge left or right. Please make a choice:')
    while True:
        try:
            if frame:
                dodge_direction = int(prompts.Prompts(frame).prompt('You decide to dodge [1]: left  [2]: right '))
            else:
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


def kids_challenge(location, frame):
    print(f'There are kids running {LOCATION_PREFIX[location]} {location.lower()}.')
    print('You called school and the teacher comes. The teacher is challenging you with a Math question:')
    challenges = math_question()
    challenge_question = choice(list(challenges.keys()))
    challenge_answer = challenges[challenge_question]
    if frame:
        your_answer = prompts.Prompts(frame).prompt(f'{challenge_question} ')
    else:
        your_answer = input(f'{challenge_question} ')
    return True if your_answer == challenge_answer else False


def boss_challenge(location, character, frame):
    students = ['Joey', 'Hsin']
    print(f'There are {students[0]} and {students[1]} {LOCATION_PREFIX[location]} {location.lower()}.')
    print('Final exam is approaching, they have a lot of questions to ask you.')
    challenges = python_question()
    satisfied = False
    print(f'{choice(students)} has a question:')
    while not satisfied:
        challenge_question = choice(list(challenges.keys()))
        challenge_answer = challenges[challenge_question]
        if frame:
            your_answer = prompts.Prompts(frame).prompt(f'{challenge_question} ').upper()
        else:
            your_answer = input(f'{challenge_question} ').upper()
        if your_answer == challenge_answer:
            satisfied = True
        else:
            print(f'[X] The answer is {challenge_answer}.')
            character['caffeine'] -= 50
            print(f'Your caffeine just dropped 50. Your current caffeine level is {character["caffeine"]}')
            if character['caffeine'] <= 0:
                print('You have run out of your caffeine!')
                return
            print(f'Now {choice(students)} has another question:')


def fight_with_foe(current_room, character, frame=None):
    foe = get_foe(current_room)
    if foe == 'rats':
        rats_challenge(current_room[1], frame)
    elif foe == 'dogs':
        success = dogs_challenge(current_room[1], frame)
        if not success:
            character['caffeine'] -= 10
    elif foe == 'kids':
        success = kids_challenge(current_room[1], frame)
        if not success:
            character['caffeine'] -= 20
    else:
        boss_challenge(current_room[1], character, frame)

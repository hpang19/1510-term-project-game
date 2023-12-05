"""
This module includes all features related to the challenges.
"""

from . import FOE_MAP, RATS_WEAPONS, MATH_QUESTIONS, PYTHON_QUESTIONS
from board import LOCATION_PREFIX
from random import choice
import sys
sys.path.append('..')
from GUI import prompts


def get_foe(current_room_description):
    foe = FOE_MAP[current_room_description[1]]
    level = current_room_description[0]
    foe = foe[level-1] if current_room_description[1] == 'Street' else foe
    return foe


def check_for_foes(current_room_description):
    foe = get_foe(current_room_description)
    if foe == 'rats':
        return choice(range(4)) == choice(range(4))
    elif foe == 'dogs':
        return choice(range(3)) == choice(range(3))
    elif foe == 'kids':
        return choice(range(3)) == choice(range(3))
    else:
        return True


def rats_challenge(location, frame, text_area_object):
    prompts.print_message(f'There is a rat {LOCATION_PREFIX[location]} {location.lower()}.\n', text_area_object)
    message = 'To proceed, you need to kill the rats. Please select a weapon to kill the rats from the list:\n'
    prompts.print_message(message, text_area_object)
    while True:
        try:
            if frame:
                weapon_id = int(prompts.Prompts(frame).prompt('[1]: Air Gun  [2]: Pesticides  [3] Hot Water '))
            else:
                weapon_id = int(input('[1]: Air Gun  [2]: Pesticides  [3] Hot Water '))
        except ValueError:
            prompts.print_message('You have to input an integer from the list:\n', text_area_object)
        else:
            if weapon_id in (1, 2, 3):
                message = RATS_WEAPONS[weapon_id] + '\n'
                prompts.print_message(message, text_area_object)
                if weapon_id != 1:
                    message = 'Keep trying, Chris! \nPlease select another weapon from the list\n'
                    prompts.print_message(message, text_area_object)
                else:
                    return True
            else:
                prompts.print_message('You have to input an integer from the list:\n', text_area_object)


def dogs_challenge(location, frame, text_area_object):
    message = f'There is a dog {LOCATION_PREFIX[location]} {location.lower()}.\n'
    prompts.print_message(message, text_area_object)
    msg = 'Now the dog is trying to attack, you need to decide whether to dodge left or right. Please make a choice:\n'
    prompts.print_message(msg, text_area_object)
    while True:
        try:
            if frame:
                dodge_direction = int(prompts.Prompts(frame).prompt('You decide to dodge [1]: left  [2]: right '))
            else:
                dodge_direction = int(input('You decide to dodge [1]: left  [2]: right '))
        except ValueError:
            prompts.print_message('You have to input an integer from the list:\n', text_area_object)
        else:
            if dodge_direction in (1, 2):
                dodge = ["left", "right"][dodge_direction - 1]
                dog_choice = choice([1, 2])
                msg = f'You are dodging {dodge.upper()} and dog attacked {["left", "right"][dog_choice - 1].upper()}\n'
                prompts.print_message(msg, text_area_object)
                return dodge_direction != dog_choice
            else:
                prompts.print_message('You have to input an integer from the list:\n', text_area_object)


def kids_challenge(location, frame, text_area_object):
    message = f'There are kids running {LOCATION_PREFIX[location]} {location.lower()}.\n'
    prompts.print_message(message, text_area_object)
    message = 'You called school and the teacher comes. The teacher is challenging you with a Math question:\n'
    prompts.print_message(message, text_area_object)
    challenge_question = choice(list(MATH_QUESTIONS.keys()))
    challenge_answer = MATH_QUESTIONS[challenge_question]
    if frame:
        your_answer = prompts.Prompts(frame).prompt(f'{challenge_question} ')
    else:
        your_answer = input(f'{challenge_question} ')
    if your_answer == challenge_answer:
        prompts.print_message('Great! That is correct answer!\n', text_area_object)
    else:
        message = f'Too bad! The correct answer is {challenge_answer}. Try harder next time!\n'
        prompts.print_message(message, text_area_object)
    return your_answer == challenge_answer


def boss_challenge(location, character, frame, text_area_object):
    students = ['Joey', 'Hsin']
    message = f'There are {students[0]} and {students[1]} {LOCATION_PREFIX[location]} {location.lower()}.\n'
    prompts.print_message(message, text_area_object)
    prompts.print_message('Final exam is approaching, they have a lot of questions to ask you.\n', text_area_object)
    prompts.print_message(f'{choice(students)} has a question:\n', text_area_object)
    while not character['kill_final_boss']:
        challenge_question = choice(list(PYTHON_QUESTIONS.keys()))
        challenge_answer = PYTHON_QUESTIONS[challenge_question]
        if frame:
            your_answer = prompts.Prompts(frame).prompt(f'{challenge_question} ').upper()
        else:
            your_answer = input(f'{challenge_question} ').upper()
        if your_answer == challenge_answer:
            character['kill_final_boss'] = True
        else:
            prompts.print_message(f'[X] The answer is {challenge_answer}.\n', text_area_object)
            character['caffeine'] -= 50
            message = f'Your caffeine just dropped 50. Your current caffeine level is {max(character["caffeine"], 0)}\n'
            prompts.print_message(message, text_area_object)
            if character['caffeine'] <= 0:
                prompts.print_message('You have run out of your caffeine!\n', text_area_object)
                return
            prompts.print_message(f'Now {choice(students)} has another question:\n', text_area_object)


def fight_with_foe(current_room, character, frame=None, text_area_object=None):
    foe = get_foe(current_room)
    if foe == 'rats':
        rats_challenge(current_room[1], frame, text_area_object)
    elif foe == 'dogs':
        success = dogs_challenge(current_room[1], frame, text_area_object)
        if not success:
            character['caffeine'] -= 10
            prompts.print_message('Oops! You lost 10 caffeine level.\n', text_area_object)
        else:
            prompts.print_message('Yay! It missed you.\n', text_area_object)
    elif foe == 'kids':
        success = kids_challenge(current_room[1], frame, text_area_object)
        if not success:
            character['caffeine'] -= 20
            prompts.print_message('Oops! You lost 20 caffeine level.\n', text_area_object)
    else:
        boss_challenge(current_room[1], character, frame, text_area_object)

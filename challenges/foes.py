"""
This module includes all features related to the challenges.
"""

from challenges import FOE_MAP, RATS_WEAPONS, MATH_QUESTIONS, PYTHON_QUESTIONS
from board import LOCATION_PREFIX
import random
import sys
sys.path.append('..')
from GUI import prompts
from levels import HOORAY_ART, KO_ART


def get_foe(current_room_description: list) -> str:
    """
    Get the foe based on the current room description.

    :param current_room_description: a list
    :precondition: current_room_description is a list consist of three elements [level, room, item]
    :postcondition: get the foe with corresponding level and location
    :return: a string representing the foe

    >>> current_room_description = [1, 'Kitchen', "Nothing"]
    >>> get_foe(current_room_description)
    'rats'

    >>> current_room_description = [2, 'Grocery Store', "Nothing"]
    >>> get_foe(current_room_description)
    'dogs'
    """
    foe = FOE_MAP[current_room_description[1]]
    level = current_room_description[0]
    foe = foe[level-1] if current_room_description[1] == 'Street' else foe
    return foe


def check_for_foes(current_room_description: list) -> bool:
    """
    Check for the presence of foes in the current room by matching two random choices.

    :param current_room_description: a list
    :precondition: current_room_description is a list consist of three elements [level, room, item]
    :postcondition: check if foe exist by matching two random choices and return the result in boolean
    :return: a boolean indicating if there are foes present
    """
    foe = get_foe(current_room_description)
    if foe == 'rats':
        return random.choice(range(4)) == random.choice(range(4))
    elif foe == 'dogs':
        return random.choice(range(3)) == random.choice(range(3))
    elif foe == 'kids':
        return random.choice(range(3)) == random.choice(range(3))
    else:
        return True


def rats_challenge(location: str, character: dict, frame=None, text_area_object=None, button_frame=None) -> bool:
    """
    Engage in a challenge against rats in a specific location.

    This function will print the message to ask player to kill the rats. Then pass the player's answer to rats_callback.

    :param location: a string indicating the location of the challenge
    :param character: a dictionary representing the game character
    :precondition: location has to be a string and exist as one of the keys in LOCATION_PREFIX
    :postcondition: a call to rats_callback function passing play's answer, correct answer and character dictionary
    """
    prompts.print_message(f'There is a rat {LOCATION_PREFIX[location]} {location.lower()}.\n', text_area_object)
    message = 'To proceed, you need to kill the rats. Please select a weapon to kill the rats from the list:\n'
    challenge_question = '[1]: Air Gun  [2]: Pesticides  [3] Hot Water '
    end = ' (press ENTER to submit your answer)'
    if frame:
        prompts.Prompts(frame).prompt(message + '\n' + challenge_question + end, rats_callback, character=character,
                                      text_area_object=text_area_object, button_frame=button_frame)
    else:
        int(input('[1]: Air Gun  [2]: Pesticides  [3] Hot Water '))


def rats_callback(answer, character, text_area_object=None, button_frame=None):
    """
    Penalize or print congratulation message based on the weapon choice.

    Check if the answer is correct. If the answer is correct, print encouraging message. If the answer is wrong,
    update the character dictionary to deduct caffeine level.
    
    :param answer: a string representing the weapon choice
    :param character: a dictionary representing the game character
    :precondition: character is a dictionary where "caffeine" exists as keys
    :postcondition: update the character dictionary to deduct caffeine level
    """
    if answer in ('1', '2', '3'):
        weapon_id = int(answer)
        message = RATS_WEAPONS[weapon_id] + '\n'
        prompts.print_message(message, text_area_object)
        if weapon_id != 1:
            penalty(1, character, 10, text_area_object)
    else:
        prompts.print_message("Why don't you pick from the list, Chris?\n", text_area_object)
        penalty(1, character, 10, text_area_object)


def dogs_challenge(location: str, character: dict, frame=None, text_area_object=None, button_frame=None) -> bool:
    """
    Engage in a challenge against dogs in a specific location.

    This function will print the message to ask player to choose a direction to dodge the dog attack. Then pass the
    player's answer to dogs_callback.

    :param location: a string indicating the location of the challenge
    :param character: a dictionary representing the game character
    :precondition: location has to be a string and exist as one of the keys in LOCATION_PREFIX
    :postcondition: a call to dogs_callback function passing play's answer, correct answer and character dictionary
    """
    message = f'There is a dog {LOCATION_PREFIX[location]} {location.lower()}.\n'
    prompts.print_message(message, text_area_object)
    msg = 'Now the dog is trying to attack, you need to decide whether to dodge left or right. Please make a choice:\n'
    challenge_question = 'You decide to dodge [1]: left  [2]: right '
    end = ' (press ENTER to submit your answer)'
    if frame:
        prompts.Prompts(frame).prompt(msg + '\n' + challenge_question + end, dogs_callback, character=character,
                                      text_area_object=text_area_object, button_frame=button_frame)
    else:
        int(input(challenge_question))


def dogs_callback(answer, character, text_area_object=None, button_frame=None):
    """
    Penalize or print congratulation message based on the dodge direction and dog attack direction.

    Check if the answer is correct. If the answer is correct, print encouraging message. If the answer is wrong,
    update the character dictionary to deduct caffeine level.

    :param answer: a string representing the dodge direction
    :param character: a dictionary representing the game character
    :precondition: character is a dictionary where "caffeine" exists as keys
    :postcondition: update the character dictionary to deduct caffeine level
    """
    if answer in ('1', '2'):
        dodge = ["left", "right"][int(answer) - 1]
        dog_choice = random.choice(['1', '2'])
        msg = f'You are dodging {dodge.upper()} and dog attacked {["left", "right"][int(dog_choice) - 1].upper()}\n'
        prompts.print_message(msg, text_area_object)
        if answer != dog_choice:
            penalty(None, character, 20, text_area_object)
        else:
            prompts.print_message('Yay! It missed you.\n', text_area_object)
    else:
        prompts.print_message("Why don't you pick from the list, Chris?\n", text_area_object)
        penalty(None, character, 20, text_area_object)


def kids_challenge(location: str, character: dict, frame=None, text_area_object=None, button_frame=None) -> bool:
    """
    Engage in a challenge against kids in a specific location.

    This function will print the message to ask player to answer a math question. Then pass the player's answer to
    kids_callback.

    :param location: a string indicating the location of the challenge
    :param character: a dictionary representing the game character
    :precondition: location has to be a string and exist as one of the keys in LOCATION_PREFIX
    :postcondition: a call to kids_callback function passing play's answer, correct answer and character dictionary
    """
    message = f'There are kids running {LOCATION_PREFIX[location]} {location.lower()}.\n'
    prompts.print_message(message, text_area_object)
    message = 'You called school and the teacher comes. The teacher is challenging you with a Math question:\n'
    challenge_question = random.choice(list(MATH_QUESTIONS.keys()))
    challenge_answer = MATH_QUESTIONS[challenge_question]
    end = ' (press ENTER to submit your answer)'
    if frame:
        prompts.Prompts(frame).prompt(f'{message}\n{challenge_question} {end}', kids_callback,
                                      challenge_answer=challenge_answer, character=character,
                                      text_area_object=text_area_object, button_frame=button_frame)
    else:
        input(f'{challenge_question} ')
    
    
def kids_callback(answer, challenge_answer, character, text_area_object=None, button_frame=None):
    """
    Penalize or print congratulation message based on the answer to the challenge.

    Check if the answer is correct. If the answer is correct, print encouraging message. If the answer is wrong,
    update the character dictionary to deduct caffeine level.

    :param answer: a string representing the answer
    :param challenge_answer: a string representing the correct answer
    :param character: a dictionary representing the game character
    :precondition: character is a dictionary where "caffeine" exists as keys
    :postcondition: update the character dictionary to deduct caffeine level
    """
    if answer == challenge_answer:
        prompts.print_message('Great! That is correct answer!\n', text_area_object)
    else:
        penalty(challenge_answer, character, 50, text_area_object)


def boss_challenge(location: str, character: dict, frame=None, text_area_object=None, button_frame=None) -> None:
    """
    Engage in a challenge against the boss character at a specific location.

    :param location: A string indicating the location of the challenge
    :param character: A dictionary representing the game character
    :precondition: location has to be a string and exist as one of the keys in LOCATION_PREFIX
    :postcondition: a call to boss_callback function passing play's answer, correct answer and character dictionary
    """
    students = ['Joey', 'Hsin']
    message = f'There are {students[0]} and {students[1]} {LOCATION_PREFIX[location]} {location.lower()}.\n'
    prompts.print_message(message, text_area_object)
    prompts.print_message('Final exam is approaching, they have a lot of questions to ask you.\n', text_area_object)
    challenge_question = random.choice(list(PYTHON_QUESTIONS.keys()))
    challenge_answer = PYTHON_QUESTIONS[challenge_question]
    end = ' (press ENTER to submit your answer)'
    if frame:
        prompts.Prompts(frame).prompt(f'{random.choice(students)} has a question:\n\n{challenge_question} {end}',
                                      boss_callback, challenge_answer=challenge_answer, character=character,
                                      text_area_object=text_area_object, button_frame=button_frame)
    else:
        your_answer = input(f'{challenge_question} ').upper()
        boss_callback(your_answer, challenge_answer, character)


def boss_callback(answer, challenge_answer, character, text_area_object=None, button_frame=None):
    """
    Penalize or print congratulation message based on the answer to the challenge.

    Check if the answer is correct. If the answer is correct, update the character dictionary to indicate the final
    boss is defeated. If the answer is wrong, update the character dictionary to deduct caffeine level.

    :param answer: a string representing the answer
    :param challenge_answer: a string representing the correct answer
    :param character: a dictionary representing the game character
    :precondition: character is a dictionary where "kill_final_boss" and "caffeine" exist as keys
    :postcondition: update the character dictionary to indicate the final boss is defeated or deduct caffeine level

    >>> character_test = {'kill_final_boss': False, 'caffeine': 100}
    >>> boss_callback('A', 'B', character_test, None)
    >>> character_test['kill_final_boss']
    False

    >>> boss_callback('A', 'A', character_test, None)
    >>> character_test['kill_final_boss']
    True
    """
    if challenge_answer == answer:
        character['kill_final_boss'] = True
        message = HOORAY_ART + '\n\n' + 'Congratulations, Chris! You defeated Joey and Hsin!'
        if text_area_object:
            prompts.print_message(message, text_area_object)
    else:
        penalty(challenge_answer, character, 500, text_area_object)


def penalty(answer, character, loss_caffeine, text_area_object):
    """
    Update character caffeine by calculate caffeine level drop based on the penalty.

    :param answer: a string representing the correct answer
    :param character: a dictionary representing the game character
    :param loss_caffeine: an integer representing the amount of caffeine to be deducted
    :precondition: character is a dictionary where "caffeine" exists as a key
    :precondition: loss_caffeine is an positive integer
    :postcondition: calculate caffeine level based on the penalty and update the character dictionary

    >>> character_test = {'caffeine': 100}
    >>> penalty('A', character_test, 10, None)
    >>> character_test['caffeine']
    90

    >>> character_test = {'caffeine': 100}
    >>> penalty('A', character_test, 50, None)
    >>> character_test['caffeine']
    50
    """
    if text_area_object:
        prompts.print_message(f'[X] The answer should be {answer}.\n', text_area_object)
    character['caffeine'] -= loss_caffeine
    message = (f'Your caffeine just dropped {loss_caffeine}. Your current caffeine level is'
               f' {max(character["caffeine"], 0)}\n')
    if text_area_object:
        prompts.print_message(message, text_area_object)
    if character['caffeine'] <= 0:
        character['game_over'] = True
        message = KO_ART + '\n\n' + "You have run out of your caffeine! :'(\n"
        if text_area_object:
            prompts.print_message(message, text_area_object)


def fight_with_foe(current_room: list, character: dict, frame=None, text_area_object=None, button_frame=None):
    """
    Fight with a foe and calculate caffeine level based on fight result.

    :param current_room: a list representing the current room's description
    :param character: a dictionary representing the game character
    :precondition: current_room is a list consist of three elements [level, room, item]
    :precondition: character is a dictionary where "caffeine" exists as a key
    """
    foe = get_foe(current_room)
    if foe == 'rats':
        rats_challenge(current_room[1], character, frame, text_area_object, button_frame)
    elif foe == 'dogs':
        dogs_challenge(current_room[1], character, frame, text_area_object, button_frame)
    elif foe == 'kids':
        kids_challenge(current_room[1], character, frame, text_area_object, button_frame)
    else:
        boss_challenge(current_room[1], character, frame, text_area_object, None)

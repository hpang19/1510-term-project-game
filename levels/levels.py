"""
This module includes all features related to the levels.
"""

import sys
sys.path.append("..")
from teas import TEA_MAP, TEA_RECIPE
from GUI import prompts


def assign_new_task(level, text_area_object=None):
    if level <= 3:
        tea = TEA_MAP[level]
        recipe = TEA_RECIPE[tea]
        message = f'Your next task is making a {tea}. In order to make {tea}, you need to {recipe}\n'
        prompts.print_message(message, text_area_object)
    else:
        message = f'You are almost there! Now go to the destination, Joey and Hsin is there waiting to challenge you!\n'
        prompts.print_message(message, text_area_object)


def steps_to_move(level, direction, frame=None, text_area_object=None):
    message = f'You can move up to {level} steps a time, how many steps do you want to move in {direction} direction? '
    if level == 1:
        return 1
    else:
        steps = 0
        while steps <= 0 or steps > level:
            if frame:
                user_input = prompts.Prompts(frame).prompt(message)
            else:
                user_input = input(message)
            try:
                steps = int(user_input)
            except ValueError:
                prompts.print_message(f'{user_input} is not a valid step.\n', text_area_object)
            else:
                return steps

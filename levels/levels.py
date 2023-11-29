"""
This module includes all features related to the levels.
"""

import sys
sys.path.append("..")
from teas import TEA_MAP, TEA_RECIPE


def assign_new_task(level):
    tea = TEA_MAP[level]
    recipe = TEA_RECIPE[tea]
    print(f'Your next task is making a {tea}. In order to make {tea}, you need to {recipe}')


def steps_to_move(level, direction):
    prompt = f'You can move up to {level} steps a time, how many steps do you want to move in {direction} direction? '
    if level == 1:
        return 1
    else:
        steps = 0
        while steps and steps > level:
            user_input = input(prompt)
            try:
                steps = int(user_input)
            except ValueError:
                print(f'{user_input} is not a valid step.')
            else:
                return steps


def unlock_next_level_rooms(level, board):
    pass

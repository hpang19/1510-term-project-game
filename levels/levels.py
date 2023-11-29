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


def unlock_next_level_rooms(level, board):
    pass

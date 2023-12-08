"""
This module includes all features related to the levels.
"""

import sys
sys.path.append("..")
from teas import TEA_MAP, TEA_RECIPE
from GUI import prompts
from levels import ASCII_ART, KO_ART


def assign_new_task(level: int, text_area_object=None):
    """
    Assigns a new task based on the given level and displays it.

    :param level: an integer representing the current level
    :postcondition: print the new task based on level

    Example:
    >>> assign_new_task(2)
    Your next task is making a Green Tea. In order to make Green Tea, you need to boil water and add matcha powder

    >>> assign_new_task(4)
    You are almost there! Now go to the destination, Joey and Hsin are waiting to challenge you!
    """
    if level <= 3:
        tea = TEA_MAP[level]
        recipe = TEA_RECIPE[tea]
        message = f'Your next task is making a {tea}. In order to make {tea}, you need to {recipe}\n'
        prompts.print_message(message, text_area_object)
    else:
        message = f'You are almost there! Now go to the destination, Joey and Hsin is there waiting to challenge you!\n'
        prompts.print_message(message, text_area_object)


def print_ASCII():
    print(ASCII_ART)


def print_KO():
    print(KO_ART)

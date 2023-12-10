"""
This module includes all features related to the levels.
"""

import sys
sys.path.append("..")
from teas import TEA_MAP, TEA_RECIPE
from GUI import prompts
from levels import ASCII_ART, KO_ART, HOORAY_ART


def assign_new_task(level: int, text_area_object=None):
    """
    Assigns a new task based on the given level and displays it.

    :param level: a positive integer representing the current level
    :precondition: the level argument has to be positive integer less than or equal to 4 passed from the game
    :postcondition: print the new task based on level

    >>> assign_new_task(2)
    Your next task is making a Matcha. In order to make Matcha, you need to In a mug, whisk together 1 teaspoon of matcha powder, 1 tablespoon of honey, and a splash of hot water to form a paste, then add ¾ cup of almond milk, whisk until combined, and enjoy your matcha latte!

    >>> assign_new_task(4)
    You are almost there! Now go to the destination, Joey and Hsin are waiting to challenge you!
    """
    if level <= 3:
        tea = TEA_MAP[level]
        recipe = TEA_RECIPE[tea]
        message = f'Your next task is making a {tea}. In order to make {tea}, {recipe}\n'
        prompts.print_message(message, text_area_object)
    else:
        message = f'You are almost there! Now go to the destination, Joey and Hsin are waiting to challenge you!\n'
        prompts.print_message(message, text_area_object)


def print_ASCII():
    """
    Print the ASCII art for the game start.
    """
    print(ASCII_ART)


def print_KO():
    """
    Print the ASCII art for losing the game.
    """
    print(KO_ART)

def print_HOORAY():
    """
    Print the ASCII art for winning the game.
    """
    print(HOORAY_ART)

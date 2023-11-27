"""
This module includes all features related to the character.
"""

from board import DIRECTION_MAP


def make_character():
    """
    Create a character.

    The character's caffeine starts at 50 at level 1, and it has empty shopping bag and no tea consumed at the
    beginning of the game, the final boss hasn't been killed.

    :postcondition: return a dictionary as an initial character
    :return: a dictionary representing the character

    >>> make_character()
    {'caffeine': 50, 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
    """
    character = {
        'caffeine': 50,
        'coordinate': (0, 0),
        'shopping_bag': [],
        'tea': [],
        'kill_final_boss': False
    }
    return character


def move_character(character, direction):
    move = DIRECTION_MAP[direction.upper()]
    current_coordinate = character['coordinate']
    character['coordinate'] = tuple(sum(coordinates) for coordinates in zip(current_coordinate, move))


def pick_up_item(character, board):
    if board[2] != "Empty Room" or "Chocolate Room" or "Door":
        new_item = board[2]
        character["shopping_bag"].append(new_item)

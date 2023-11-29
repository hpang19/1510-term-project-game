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


def move_character(character, direction, steps):
    move = DIRECTION_MAP[direction.upper()]
    move = (move[0] * steps, move[1] * steps)
    current_coordinate = character['coordinate']
    character['coordinate'] = tuple(sum(coordinates) for coordinates in zip(current_coordinate, move))


def pick_up_item(character, board):
    """
    Pick up item.

    A simple function that appends new item to character's shopping bag.

    :param character: a non-empty dictionary
    :param board: a non-empty dictionary
    :precondition:
    :return:
    """
    item = board[character["coordinate"]][2]
    if item not in ("Nothing", "Door", "Chocolate", "Origin"):
        print(f'Oh! There is a {item} to pick up! You picked it up and put in your shopping bag.')
        character["shopping_bag"].append(item)
        board[character["coordinate"]][2] = "Nothing"


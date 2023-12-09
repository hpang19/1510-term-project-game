"""
This module includes all features related to the character.
"""

from board import DIRECTION_MAP
import tkinter as tk
from GUI import prompts


def make_character() -> dict:
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


def move_character(character: dict, direction: str, steps: int, frame_object=None, current_room_text=None,
                   current_relief=None):
    """
    Move the character on the game board in a specified direction.

    The "step" arguent is not in used for the most recent version. Will be deprecated in the next update.

    :param character: a dictionary representing the game character with a 'coordinate' key
    :param direction: a string indicating the direction of movement ('W', 'S', 'A', 'D')
    :param steps: an integer indicating the number of steps to move
    :precondition: character is a dictionary that has a key called "coordinate"
    :postcondition: move the character on the game board in a specified direction

    >>> character_test = {'coordinate': (3, 3)}
    >>> move_character(character_test, 'S', 2)
    >>> character_test['coordinate']
    (1, 3)
    >>> move_character(character_test, 'A', 1)
    >>> character_test['coordinate']
    (1, 2)
    """
    move = DIRECTION_MAP[direction.upper()]
    move = (move[0] * steps, move[1] * steps)
    current_coordinate = character['coordinate']
    character['coordinate'] = tuple(sum(coordinates) for coordinates in zip(current_coordinate, move))

    if frame_object:
        frame = tk.Frame(master=frame_object, width=50, height=50, relief=current_relief, borderwidth=2)
        frame.grid(row=current_coordinate[0], column=current_coordinate[1])
        if current_room_text == 'Door':
            label = tk.Label(master=frame, text=current_room_text, width=10, height=4, bg='LightCyan2')
        else:
            label = tk.Label(master=frame, text=current_room_text, width=10, height=4)
        label.grid(row=0, column=0)

        frame = tk.Frame(master=frame_object, width=50, height=50, relief=tk.SUNKEN, borderwidth=2)
        frame.grid(row=character['coordinate'][0], column=character['coordinate'][1])
        label = tk.Label(master=frame, text='Chris', width=10, height=4, bg='gray40', fg='white')
        label.grid(row=0, column=0)


def pick_up_item(character: dict, board: dict, text_area_object=None):
    """
    Pick up item by appending new item to character's shopping bag.

    :param character: a dictionary
    :param board: a dictionary
    :precondition: board is a dictionary with keys in tuples of coordinates
    :precondition: character is a dictionary that has a key called "coordinate"
    :postcondition: appending new item to character's shopping bag and remove item from the board

    >>> character_test = {'coordinate': (2, 3), 'shopping_bag': []}
    >>> board_test = {(2, 3): [1, 'Kitchen', 'Tea']}
    >>> pick_up_item(character_test, board_test)
    'Oh! There is a Tea to pick up! You picked it up and put in your shopping bag.'
    >>> character_test['shopping_bag']
    ['Tea']
    >>> board_test[(2, 3)]
    [1, 'Kitchen', 'Nothing']
    """
    item = board[character["coordinate"]][2]
    if item not in ("Nothing", "Door", "Chocolate", "Origin"):
        message = f'Oh! There is a {item} to pick up! You picked it up and put in your shopping bag.\n'
        prompts.print_message(message, text_area_object)
        character["shopping_bag"].append(item)
        board[character["coordinate"]][2] = "Nothing"

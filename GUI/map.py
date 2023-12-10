"""
This module includes all features related to the GUI map.
"""

import json
import tkinter as tk
from GUI import BORDER_EFFECTS


def get_relief(room_description: list, current_level: int) -> str:
    """
    Get the relief effect for a room description based on the current level.

    :param room_description: a list [level, room, item] describing the room
    :param current_level: an integer representing the current level in the game
    :postcondition: get the relief effect for a room description and return the relief effect for the room
    :return: a string representing the relief effect for the room

    >>> get_relief([1, 'Kitchen', 'Hot Water'], 1)
    'raised'

    >>> get_relief([2, 'Street', 'Nothing'], 3)
    'sunken'
    """
    level, room, item = room_description
    if level > current_level:
        relief = BORDER_EFFECTS['locked']
    elif item == 'Door':
        relief = BORDER_EFFECTS['door']
    elif item == 'Nothing':
        relief = BORDER_EFFECTS['other']
    else:
        relief = BORDER_EFFECTS['item']
    return relief


def get_text(room_description: list, current_level: int):
    """
    Get the text to display for a room description based on the current level.

    :param room_description: a list [level, room, item] describing the room
    :param current_level: an integer representing the current level in the game
    :postcondition: return the text to display for the room
    :return: a string representing the text to display for the room

    >>> get_text([1, 'Kitchen', 'Matcha Powder'], 1)
    'Matcha Powder'

    >>> get_text([2, 'Street', 'Nothing'], 3)
    ''
    """
    level, room, item = room_description
    text = ''
    if level <= current_level:
        if room in ('Kitchen', 'Grocery Store', 'Market'):
            text += room
        if item != 'Nothing':
            text = item
    return text


def create_main_window(game_board: dict, rows: int, columns: int, current_level: int):
    """
    Create the main window of the game with rooms based on the game board.

    :param game_board: a dictionary representing the game board
    :param rows: an integer representing the number of rows in the game board
    :param columns: an integer representing the number of columns in the game board
    :param current_level: an integer representing the current level in the game
    """
    root = tk.Tk()
    root.title('Cup of Tea')

    main_frame = tk.Frame(root, width=600, height=600)
    main_frame.pack(side=tk.LEFT, expand=1)

    for row in range(rows):
        for column in range(columns):
            room_description = game_board[(row, column)]
            relief = get_relief(room_description, current_level)
            text = get_text(room_description, current_level)
            frame = tk.Frame(master=main_frame, width=50, height=50, relief=relief, borderwidth=2)
            frame.grid(row=row, column=column)
            label = tk.Label(master=frame, text=text, width=10, height=4)
            label.grid(row=0, column=0)
            if row == 0 and column == 0:
                label = tk.Label(master=frame, text='Chris', width=10, height=4)
                label.grid(row=0, column=0)
    root.mainloop()


if __name__ == '__main__':
    import sys
    sys.path.append('..')
    with open('data/board.json') as file_object:
        board_json = json.load(file_object)
    board = {}
    for k, v in board_json.items():
        board[tuple(int(x) for x in k.replace('(', '').replace(')', '').split(', '))] = v
    create_main_window(board, 10, 10, 4)

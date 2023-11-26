"""
This module includes all features related to the game board.
"""

from random import randint
from rooms import kitchen_map, grocery_store, traditional_market


def make_board(rows, columns):
    """
    Create a board for the game and return the board in dictionary.

    Initialize one room in level 1 scope with a chocolate room. The level 1 scope will have a size rows/2 x
    columns/2, the level 2 scope will have half of the board, and level 3 scope will include the whole board except
    the (rows-1, columns-1) location, which is reserved for the final boss and destination.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows is a positive integer not less than 10
    :precondition: columns is a positive integer not less than 10
    :postcondition: create a board for the game and return the board in dictionary
    :return: a dictionary representing the game board
    """
    board = {}
    kitchen_rows = int(rows / 2)
    kitchen_columns = int(columns / 2)
    chocolate_room = (randint(0, kitchen_rows - 1), randint(0, kitchen_columns - 1))
    for row in range(rows):
        for column in range(columns):
            if row < kitchen_rows:
                if column < kitchen_columns:
                    kitchen = kitchen_map((0, 0), kitchen_rows, kitchen_columns, chocolate_room)
                    room = kitchen[(row, column)] if (row, column) in kitchen else 'Empty Room'
                    board[(row, column)] = ['L1', 'Kitchen', room]
                else:
                    board[(row, column)] = ['L2', 'Street', 'Empty Room']
            else:
                board[(row, column)] = ['L3', 'Street', 'Empty Room']
    board[(rows - 1, columns - 1)] = ['L4', 'Destination', 'Joey and Hsin']
    return board
print(make_board(10, 10))

def validate_move(level, board, character, direction):
    pass


def get_current_location(board, character):
    pass


def move_chocolate(board):
    pass

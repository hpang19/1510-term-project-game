"""
This module includes all rooms on the game board.
"""

from random import choice


def random_choice_coordinate(row_range, column_range):
    return choice(row_range), choice(column_range)


def kitchen_map(origin_coordinate, rows, columns, chocolate_room):
    row_range = list(range(origin_coordinate[0], origin_coordinate[0]+rows))
    column_range = list(range(origin_coordinate[1], origin_coordinate[1] + columns))
    kitchen = {(0, 0): 'Origin', chocolate_room: 'Chocolate Room'}
    for item in ['Cup', 'Spoon', 'Grinder', 'Hot Water', 'Tea Bag']:
        row, column = random_choice_coordinate(row_range, column_range)
        while (row, column) in kitchen:
            row, column = random_choice_coordinate(row_range, column_range)
        kitchen[row, column] = item
    return kitchen


def grocery_store():
    pass


def traditional_market():
    pass

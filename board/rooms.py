"""
This module includes all items in the rooms on the game board.
"""

from random import choice


def random_choice_coordinate(origin_coordinate: tuple, rows: int, columns: int) -> tuple:
    """
    Choose a random coordinate within a specified range.

    :param origin_coordinate: a tuple representing the starting coordinate (row, column)
    :param rows: an integer representing the number of rows
    :param columns: an integer representing the number of columns
    :precondition: rows is an integer not less than 10
    :precondition: columns is an integer not less than 10
    :postcondition: choose and return a coordinate within a specified range
    :return: a tuple representing a random coordinate within the specified range
    """
    row_range = list(range(origin_coordinate[0], origin_coordinate[0] + rows))
    column_range = list(range(origin_coordinate[1], origin_coordinate[1] + columns))
    return choice(row_range), choice(column_range)


def kitchen_map(rows: int, columns: int, chocolate_room_coordinate: tuple) -> dict:
    """
    Create a map for the kitchen area.

    :param rows: an integer representing the number of rows in the kitchen area
    :param columns: an integer representing the number of columns in the kitchen area
    :param chocolate_room_coordinate: a tuple representing the coordinate of the chocolate room
    :precondition: rows is an integer not less than 10
    :precondition: columns is an integer not less than 10
    :return: a dictionary representing the kitchen area map
    """
    kitchen = {(0, 0): 'Origin', chocolate_room_coordinate: 'Chocolate', (choice(range(rows)), columns-1): 'Door'}
    for item in ['Mug', 'Spoon', 'Grater', 'Hot Water', 'Tea Bag']:
        row, column = random_choice_coordinate((0, 0), rows, columns)
        while (row, column) in kitchen:
            row, column = random_choice_coordinate((0, 0), rows, columns)
        kitchen[row, column] = item
    return kitchen


def grocery_store_map(origin_coordinate: tuple, rows: int, columns: int) -> dict:
    """
    Create a map for the grocery store area.

    :param origin_coordinate: a tuple representing the starting coordinate (row, column) of the grocery store
    :param rows: an integer representing the number of rows in the grocery store area
    :param columns: an integer representing the number of columns in the grocery store area
    :precondition: rows is an integer not less than 10
    :precondition: columns is an integer not less than 10
    :return: a dictionary representing the grocery store area map
    """
    grocery_store = {(origin_coordinate[0] + choice(range(rows)), origin_coordinate[1]): 'Door'}
    for item in ['Matcha Powder', 'Honey', 'Almond Milk']:
        row, column = random_choice_coordinate(origin_coordinate, rows, columns)
        while (row, column) in grocery_store:
            row, column = random_choice_coordinate(origin_coordinate, rows, columns)
        grocery_store[row, column] = item
    return grocery_store


def traditional_market_map(origin_coordinate: tuple, rows: int, columns: int) -> dict:
    """
    Create a map for the traditional market area.

    :param origin_coordinate: a tuple representing the starting coordinate (row, column) of the traditional market
    :param rows: an integer representing the number of rows in the traditional market area
    :param columns: an integer representing the number of columns in the traditional market area
    :precondition: rows is an integer not less than 10
    :precondition: columns is an integer not less than 10
    :return: a dictionary representing the traditional market area map
    """
    market = {(origin_coordinate[0], origin_coordinate[1] + choice(range(columns))): 'Door'}
    for item in ['Ginger', 'Turmeric']:
        row, column = random_choice_coordinate(origin_coordinate, rows, columns)
        while (row, column) in market:
            row, column = random_choice_coordinate(origin_coordinate, rows, columns)
        market[row, column] = item
    return market

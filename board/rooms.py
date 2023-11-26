"""
This module includes all items in the rooms on the game board.
"""

from random import choice


def random_choice_coordinate(origin_coordinate, rows, columns):
    row_range = list(range(origin_coordinate[0], origin_coordinate[0] + rows))
    column_range = list(range(origin_coordinate[1], origin_coordinate[1] + columns))
    return choice(row_range), choice(column_range)


def kitchen_map(origin_coordinate, rows, columns, chocolate_room_coordinate):
    kitchen = {(0, 0): 'Origin', chocolate_room_coordinate: 'Chocolate Room'}
    for item in ['Cup', 'Spoon', 'Grinder', 'Hot Water', 'Tea Bag']:
        row, column = random_choice_coordinate(origin_coordinate, rows, columns)
        while (row, column) in kitchen:
            row, column = random_choice_coordinate(origin_coordinate, rows, columns)
        kitchen[row, column] = item
    return kitchen


def grocery_store_map(origin_coordinate, rows, columns):
    grocery_store = {(origin_coordinate[0] + choice(range(rows)), origin_coordinate[1]): 'Door'}
    for item in ['Match Powder', 'Honey', 'Almond Milk']:
        row, column = random_choice_coordinate(origin_coordinate, rows, columns)
        while (row, column) in grocery_store:
            row, column = random_choice_coordinate(origin_coordinate, rows, columns)
        grocery_store[row, column] = item
    return grocery_store


def traditional_market_map(origin_coordinate, rows, columns):
    market = {(origin_coordinate[0], origin_coordinate[1] + choice(range(columns))): 'Door'}
    for item in ['Ginger', 'Turmeric']:
        row, column = random_choice_coordinate(origin_coordinate, rows, columns)
        while (row, column) in market:
            row, column = random_choice_coordinate(origin_coordinate, rows, columns)
        market[row, column] = item
    return market

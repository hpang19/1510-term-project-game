"""
This module includes all features related to the game board.
"""

from random import randint, choice
from .rooms import kitchen_map, grocery_store_map, traditional_market_map
from . import DIRECTION_MAP
from GUI import prompts


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
    get_board_components_result = get_board_component(rows, columns)
    (kitchen_rows, kitchen_columns, chocolate_room, kitchen, grocery_store_origin, grocery_store, grocery_row_range,
     grocery_column_range, market_origin, market, market_row_range, market_column_range) = get_board_components_result
    for row in range(rows):
        for column in range(columns):
            if row < kitchen_rows:
                if column < kitchen_columns:
                    item = kitchen[(row, column)] if (row, column) in kitchen else 'Nothing'
                    board[(row, column)] = [1, 'Kitchen', item]
                else:
                    item = grocery_store[(row, column)] if (row, column) in grocery_store else 'Nothing'
                    location = 'Grocery Store' if (row in grocery_row_range and column in grocery_column_range) else 'Street'
                    board[(row, column)] = [2, location, item]
            else:
                item = market[(row, column)] if (row, column) in market else 'Nothing'
                location = 'Market' if (row in market_row_range and column in market_column_range) else 'Street'
                board[(row, column)] = [3, location, item]
    board[(rows - 1, columns - 1)] = [4, 'Destination', 'Joey and Hsin']
    return board


def get_board_component(rows, columns):
    kitchen_rows = int(rows / 2)
    kitchen_columns = int(columns / 2)
    chocolate_room = (randint(0, kitchen_rows - 1), randint(0, kitchen_columns - 1))
    kitchen = kitchen_map(kitchen_rows, kitchen_columns, chocolate_room)
    grocery_store_origin = (choice(range(0, kitchen_rows - 2)), choice(range(kitchen_columns, columns - 3)) + 1)
    grocery_store = grocery_store_map(grocery_store_origin, 3, 3)
    grocery_row_range = range(grocery_store_origin[0], grocery_store_origin[0] + 3)
    grocery_column_range = range(grocery_store_origin[1], grocery_store_origin[1] + 3)
    market_origin = (choice(range(kitchen_rows, rows - 3)) + 1, choice(range(0, columns - 3)))
    market = traditional_market_map(market_origin, 3, 3)
    market_row_range = range(market_origin[0], market_origin[0] + 3)
    market_column_range = range(market_origin[1], market_origin[1] + 3)
    return (kitchen_rows, kitchen_columns, chocolate_room, kitchen, grocery_store_origin, grocery_store,
            grocery_row_range, grocery_column_range, market_origin, market, market_row_range, market_column_range)


def validate_move(level, board, character, direction, steps):
    move = DIRECTION_MAP[direction.upper()]
    move = (move[0] * steps, move[1] * steps)
    current_coordinate = character['coordinate']
    new_coordinate = tuple(sum(coordinates) for coordinates in zip(current_coordinate, move))
    valid_move = False
    if new_coordinate in board and board[new_coordinate][0] <= level:
        current_location = board[current_coordinate][1]
        new_location = board[new_coordinate][1]
        if new_location == current_location:
            valid_move = True
        else:
            if new_location == 'Destination' or 'Door' in (board[new_coordinate][2], board[current_coordinate][2]):
                valid_move = True
    return valid_move


def move_chocolate(board, character):
    coordinate = choice(list(board.keys()))
    level = board[character['coordinate']][0]
    while not (board[coordinate][2] == 'Nothing' and board[coordinate][0] > min(level, 2)):
        coordinate = choice(list(board.keys()))
    board[character['coordinate']][2] = 'Nothing'
    board[coordinate][2] = 'Chocolate'


def print_map(character, board, level):
    current_location = character['coordinate']
    for row in range(10):
        for column in range(10):
            map_level, room, item = board[(row, column)]
            if map_level <= level:
                if (row, column) == current_location:
                    print('[*]', end='')
                elif item == 'Origin':
                    print('[_]', end='')
                elif room == 'Destination':
                    print('[+]', end='')
                elif item == 'Door':
                    print('[/]', end='')
                elif item == 'Nothing':
                    if room in ('Kitchen', 'Grocery Store', 'Market'):
                        print('[_]', end='')
                    else:
                        print('[ ]', end='')
                elif item == 'Chocolate':
                    print('[C]', end='')
                else:
                    print('[!]', end='')
            else:
                print('[X]', end='')
        print()


def describe_current_status(board, character, level, text_area_object=None):
    _, room, item = board[character['coordinate']]
    caffeine = character['caffeine']
    shopping_bag = character['shopping_bag']
    tea = character['tea']
    location_message = f'Current Level: level {level}\nYou are in the {room} with {item.lower()}.\n'
    caffeine_message = f'Caffeine Level: {caffeine}\nShopping Bag: {shopping_bag}\nTeas you have made:{tea}.\n'
    prompts.print_message(location_message, text_area_object, clear=True)
    prompts.print_message(caffeine_message, text_area_object)
    if not text_area_object:
        print_map(character, board, level)


if __name__ == '__main__':
    import pandas as pd
    test_board = make_board(10, 10)
    df = pd.DataFrame(index=range(10), columns=range(10))
    for coord, data in test_board.items():
        df.iloc[*coord] = data
    df.to_excel('map_demo.xlsx')

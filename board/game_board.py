"""
This module includes all features related to the game board.
"""

import random
from board.rooms import kitchen_map, grocery_store_map, traditional_market_map
from board import DIRECTION_MAP
from GUI import prompts


def make_board(rows: int, columns: int) -> dict:
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
                    location = 'Grocery Store' if (row in grocery_row_range and column in grocery_column_range) else \
                        'Street'
                    board[(row, column)] = [2, location, item]
            else:
                item = market[(row, column)] if (row, column) in market else 'Nothing'
                location = 'Market' if (row in market_row_range and column in market_column_range) else 'Street'
                board[(row, column)] = [3, location, item]
    board[(rows - 1, columns - 1)] = [4, 'Destination', 'Joey and Hsin']
    return board


def get_board_component(rows: int, columns: int) -> tuple:
    """
    Get board components for creating the game board.

    :param rows: a positive integer
    :param columns: a positive integer
    :precondition: rows is a positive integer not less than 10
    :precondition: columns is a positive integer not less than 10
    :return: a tuple of various board components
    """
    kitchen_rows = int(rows / 2)
    kitchen_columns = int(columns / 2)
    chocolate_room = (random.randint(0, kitchen_rows - 1), random.randint(0, kitchen_columns - 1))
    kitchen = kitchen_map(kitchen_rows, kitchen_columns, chocolate_room)
    grocery_store_origin = (random.choice(range(0, kitchen_rows - 2)),
                            random.choice(range(kitchen_columns, columns - 3)) + 1)
    grocery_store = grocery_store_map(grocery_store_origin, 3, 3)
    grocery_row_range = range(grocery_store_origin[0], grocery_store_origin[0] + 3)
    grocery_column_range = range(grocery_store_origin[1], grocery_store_origin[1] + 3)
    market_origin = (random.choice(range(kitchen_rows, rows - 3)) + 1, random.choice(range(0, columns - 3)))
    market = traditional_market_map(market_origin, 3, 3)
    market_row_range = range(market_origin[0], market_origin[0] + 3)
    market_column_range = range(market_origin[1], market_origin[1] + 3)
    return (kitchen_rows, kitchen_columns, chocolate_room, kitchen, grocery_store_origin, grocery_store,
            grocery_row_range, grocery_column_range, market_origin, market, market_row_range, market_column_range)


def validate_move(level: int, board: dict, character: dict, direction: str, steps: int) -> bool:
    """
    Validate a move in the game.

    :param level: an integer representing the current level
    :param board: a dictionary representing the game board
    :param character: a dictionary representing the game character
    :param direction: a string representing the direction in ('W', 'S', 'A', or 'D')
    :param steps: an integer representing the number of steps to move
    :precondition: board is a dictionary with keys in tuples of coordinates
    :precondition: character is a dictionary that has a key called "coordinate"
    :postcondition: validate the move and return a boolean for whether move is valid
    :return: a boolean indicating if the move is valid

    >>> board_test = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'], (1, 0): [2, 'Kitchen',
    ... 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
    >>> character_test = {'coordinate': (0, 0)}
    >>> validate_move(1, board_test, character_test, 'D', 1)
    True

    >>> validate_move(1, board_test, character_test, 'S', 1)
    False
    """
    move = DIRECTION_MAP[direction.upper()]
    move = (move[0] * steps, move[1] * steps)
    current_coordinate = character['coordinate']
    new_coordinate = tuple(sum(coordinates) for coordinates in zip(current_coordinate, move))
    valid_move = False
    if new_coordinate in board and board[new_coordinate][0] <= level:
        current_location = board[current_coordinate][1]
        new_location = board[new_coordinate][1]
        if new_location == current_location or current_location == 'Destination':
            valid_move = True
        else:
            if new_location == 'Destination' or 'Door' in (board[new_coordinate][2], board[current_coordinate][2]):
                valid_move = True
    return valid_move


def move_chocolate(board: dict, character: dict):
    """
    Move the chocolate item in the game board.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the game character
    :precondition: board is a dictionary with keys in tuples of coordinates
    :precondition: character is a dictionary that has a key called "coordinate"
    :precondition: character's current location has chocolate
    :postcondition: move the chocolate on the board

    >>> board_test = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'], (1, 0): [2, 'Kitchen',
    ... 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
    >>> character_test = {'coordinate': (0, 1)}
    >>> move_chocolate(board_test, character_test)
    >>> board_test[character_test['coordinate']][2]
    'Nothing'
    """
    coordinate = random.choice(list(board.keys()))
    level = board[character['coordinate']][0]
    while not (board[coordinate][2] == 'Nothing' and board[coordinate][0] > min(level, 2)):
        coordinate = random.choice(list(board.keys()))
    board[character['coordinate']][2] = 'Nothing'
    board[coordinate][2] = 'Chocolate'


def print_map(character: dict, board: dict, level: int, rows=10, columns=10):
    """
    Print a map representation of the game board to the terminal.

    :param character: a dictionary representing the game character
    :param board: a dictionary representing the game board
    :param level: an integer representing the current level
    :param rows: an integer representing the number of rows in the game board default to 10
    :param columns: an integer representing the number of columns in the game board default to 10
    :precondition: board is a dictionary with keys in tuples of coordinates
    :precondition: character is a dictionary that has a key called "coordinate"
    :postcondition: print the map in the terminal for non-gui game version
    """
    current_location = character['coordinate']
    for row in range(rows):
        for column in range(columns):
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


def describe_current_status(board: dict, character: dict, level: int, text_area_object=None):
    """
    Describe the current status of the game.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the game character
    :param level: an integer representing the current level
    :precondition: board is a dictionary with keys in tuples of coordinates
    :precondition: character is a dictionary that has a key called "coordinate"
    :postcondition: print the current status of the game
    """
    _, room, item = board[character['coordinate']]
    caffeine = character['caffeine']
    shopping_bag = character['shopping_bag']
    tea = character['tea']
    location_message = f'Current Level: level {level}\nYou are in the {room}\n'
    if item in ('Origin', 'Nothing'):
        location_message.replace('\n', f' with {item.lower()}.\n')
    caffeine_message = (f'Caffeine Level: {caffeine}\nItems in Shopping Bag: {shopping_bag}\nTeas you made successfully'
                        f':{tea}.\n')
    prompts.print_message(location_message, text_area_object, clear=True)
    prompts.print_message(caffeine_message, text_area_object)
    prompts.print_message('-- ' * 23 + '\n', text_area_object)
    if not text_area_object:
        print_map(character, board, level)

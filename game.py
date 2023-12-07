"""
This module serves as a main module to execute the game program.
"""

from board.game_board import make_board, validate_move, move_chocolate, describe_current_status
from character.game_character import make_character, move_character, pick_up_item
from challenges.foes import check_for_foes, fight_with_foe
from teas.teas import ready_to_make_tea, make_tea
from levels.levels import assign_new_task, print_ASCII
import json
import os
import atexit
import itertools


class Game:
    """
    Class representing the game.
    """
    def __init__(self):
        """
        Initialize the Game class.
        """
        self.move_count = itertools.count(0)
        self.rows = 10
        self.columns = 10

        if os.path.exists('data/board.json'):
            with open('data/board.json') as json_file:
                board = json.load(json_file)
            self.board = {}
            for key, value in board.items():
                self.board[tuple(int(coord) for coord in key.replace('(', '').replace(')', '').split(', '))] = value
        else:
            self.board = make_board(self.rows, self.columns)

        if os.path.exists('data/character.json'):
            with open('data/character.json') as json_file:
                self.character = json.load(json_file)
            self.character['coordinate'] = tuple(self.character['coordinate'])
        else:
            self.character = make_character()

    def game(self):
        """
        Run the game loop.

        :precondition: The board and character data must be initialized before starting the game.
        :postcondition: The game ends when the player's caffeine level reaches zero or the final boss is defeated.
        """
        level = len(self.character.get('tea', [])) + 1
        print('Welcome to the game!')
        describe_current_status(self.board, self.character, level)
        while self.character['caffeine'] > 0:
            direction = input('Please select your direction: [W]: Up  [S]: Down  [A]: Left  [D]: Right: ')
            print(f'==================================== {next(self.move_count)} ====================================')
            if direction.upper() not in ['W', 'S', 'A', 'D']:
                print("!!! Invalid direction !!!")
                continue
            valid_move = validate_move(level, self.board, self.character, direction, steps=1)
            if not valid_move:
                print('!!! You can not go in this direction, please choose direction again. !!!')
                continue
            move_character(self.character, direction, steps=1)
            current_room_description = self.board[self.character['coordinate']]
            if current_room_description[2] == 'Chocolate':
                self.character['caffeine'] += 10
                print(f'You consumed chocolate, now your caffeine level increased to {self.character["caffeine"]}.')
                move_chocolate(self.board, self.character)
            if current_room_description[2] not in ('Nothing', 'Door', 'Joey and Hsin', 'Origin'):
                pick_up_item(self.character, self.board)
                tea_ingredients_all_set = ready_to_make_tea(level, self.character)
                if tea_ingredients_all_set:
                    make_tea(level, self.character)
                    level += 1
                    print(f'Nice job! You leveled up. Now your level is {level}.')
                    assign_new_task(level)
            describe_current_status(self.board, self.character, level)
            there_is_a_challenger = check_for_foes(current_room_description)
            if there_is_a_challenger:
                fight_with_foe(current_room_description, self.character)
            if self.character['kill_final_boss']:
                print('Congratulation! You won!')
                print_ASCII()
                break
        if self.character['caffeine'] <= 0:
            print('Game Over!')

    def __exit__(self):
        """
        Saves the game state when exit.
        """
        if not os.path.exists('data'):
            os.makedirs('data')
        board_to_file = {}
        for coordinate, room_description in self.board.items():
            board_to_file[str(coordinate)] = room_description
        with open('data/board.json', 'w') as file_object:
            json.dump(board_to_file, file_object)

        with open('data/character.json', 'w') as file_object:
            json.dump(self.character, file_object)


def main():
    """
    Drive the program.
    """
    game_instance = Game()
    atexit.register(game_instance.__exit__)
    game_instance.game()


if __name__ == '__main__':
    main()
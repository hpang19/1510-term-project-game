"""
This module serves as a main module to execute the game program.
"""

from board.game_board import make_board, validate_move, move_chocolate, describe_current_status
from character.game_character import make_character, move_character, pick_up_item
from challenges.foes import check_for_foes, fight_with_foe
from teas.tea import ready_to_make_tea, make_tea
from levels.level import assign_new_task
from levels import ASCII_ART
import tkinter as tk
from GUI.map import get_relief, get_text
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
        self.rows = 10
        self.columns = 10
        self.root = tk.Tk()
        self.root.title('Cup of Tea')
        self.main_frame = tk.Frame(self.root, width=600, height=600)
        self.main_frame.pack(side=tk.LEFT, expand=1)
        self.text_area = tk.Text(self.root, height=20, width=70)
        self.text_area.pack()
        self.input_frame = tk.Frame(self.root, height=2, width=5)
        self.input_frame.pack()

        board_file = self.__check_file_exist('data', 'board_', '.json')
        character_file = self.__check_file_exist('data', 'character_', '.json')
        if board_file and character_file:
            current_try = int(board_file.split('_')[1].split('.')[0])
            self.current_count = itertools.count(current_try)
            self.__load_player(board_file, character_file)
            if self.character['kill_final_boss'] or self.character['game_over']:
                self.board = make_board(self.rows, self.columns)
                self.character = make_character()
        else:
            self.board = make_board(self.rows, self.columns)
            self.character = make_character()
            self.current_count = itertools.count(0)
        self.level = len(self.character.get('tea', [])) + 1
        self.create_gui_game_board(self.character['coordinate'])
        self.create_buttons()

    def __load_player(self, board_file, character_file):
        """
        Load the player's game state from the saved file.

        :param board_file: a string representing the file name of the saved board
        :param character_file: a string representing the file name of the saved character
        :precondition: board_file and character_file are validated by __check_file_exist function
        :postcondition: loads the player's game state from the saved file
        """
        with open(f'data/{board_file}') as json_file:
            board = json.load(json_file)
        self.board = {}
        for key, value in board.items():
            self.board[tuple(int(coord) for coord in key.replace('(', '').replace(')', '').split(', '))] = value
        with open(f'data/{character_file}') as json_file:
            self.character = json.load(json_file)
        self.character['coordinate'] = tuple(self.character['coordinate'])

    def __check_file_exist(self, directory, prefix, suffix):
        """
        Check if the file exists in the given directory.

        File name will be matched with given prefix and suffix. If there are multiple files that match the given
        prefix, the latest one will be returned.

        :param directory: a string representing the directory to check
        :param prefix: a string representing the prefix of the file name
        :param suffix: a string representing the suffix of the file name
        :postcondition: returns the file name if exists, otherwise returns None
        :return: a string representing the file name if exists, otherwise None
        """
        if os.path.exists(directory):
            files = os.listdir(directory)
            matching_files = [file for file in files if file.startswith(prefix) and file.endswith(suffix)]
            if matching_files:
                return sorted(matching_files, reverse=True)[0]

    def move(self, direction):
        """
        Move the character in the specified direction and execute the corresponding task in new location.

        Foes will be fought if there is one in the new location. Items will be picked up if there is one in the new
        location. Character will level up if all tea ingredients are collected make drank. Character's caffeine level
        will be increased or decreased based on the challenge or achievement. Game will be over if caffeine level drops
        below 0.

        :param direction: a string representing direction to move
        :precondition: direction must be one of 'W', 'S', 'A', or 'D'
        :postcondition: moves the character in the given direction and updates the game status and GUI accordingly
        """

        steps = 1
        valid_move = validate_move(self.level, self.board, self.character, direction, steps)

        if not valid_move:
            self.text_area.delete('1.0', tk.END)
            message = 'You can not go in this direction, please choose direction again.\n'
            self.text_area.insert(tk.END, message)
            return

        current_text = get_text(self.board[self.character['coordinate']], self.level)
        current_relief = get_relief(self.board[self.character['coordinate']], self.level)
        move_character(self.character, direction, steps, self.main_frame, current_text, current_relief)
        describe_current_status(self.board, self.character, self.level, self.text_area)

        current_room_description = self.board[self.character['coordinate']]
        there_is_a_challenger = check_for_foes(current_room_description)

        if current_room_description[2] == 'Chocolate':
            self.character['caffeine'] += 10
            message = f'You consumed chocolate, now your caffeine level increased to {self.character["caffeine"]}.\n'
            self.text_area.insert(tk.END, message)
            move_chocolate(self.board, self.character)

        if self.character['kill_final_boss']:
            self.text_area.insert(tk.END, 'Congratulations! You won!\n')
            return

        if current_room_description[2] not in ('Nothing', 'Door', 'Joey and Hsin', 'Origin'):
            pick_up_item(self.character, self.board, self.text_area)
            tea_ingredients_all_set = ready_to_make_tea(self.level, self.character)

            if tea_ingredients_all_set:
                make_tea(self.level, self.character, self.text_area)
                self.level += 1
                self.text_area.insert(tk.END, f'Nice job! You leveled up. Now your level is {self.level}.\n')
                assign_new_task(self.level, self.text_area)
                self.create_gui_game_board(self.character['coordinate'])

        if there_is_a_challenger:
            self.disable_buttons()
            fight_with_foe(current_room_description, self.character, self.input_frame, self.text_area, self.button_frame)

        if self.character['caffeine'] <= 0:
            self.character['game_over'] = True
            self.text_area.insert(tk.END, 'Game Over!\n')

    def create_gui_game_board(self, player=(0, 0)):
        """
        Create the GUI representation of the game board.

        :param player: a tuple representing the coordinates of the player's position, default to (0,0)
        :precondition: player should be a tuple of two integers representing the player's position.
        :postcondition: creates a graphical representation of the game board using tkinter.
        """
        for row in range(self.rows):
            for column in range(self.columns):
                room_description = self.board[(row, column)]
                relief = get_relief(room_description, self.level)
                text = get_text(room_description, self.level)
                frame = tk.Frame(master=self.main_frame, width=50, height=50, relief=relief, borderwidth=2)
                frame.grid(row=row, column=column)
                if text == 'Door':
                    label = tk.Label(master=frame, text=text, width=10, height=4, bg='LightCyan2')
                else:
                    label = tk.Label(master=frame, text=text, width=10, height=4)
                label.grid(row=0, column=0)
                if player[0] == row and player[1] == column:
                    label = tk.Label(master=frame, text='Chris', width=10, height=4, bg='gray40', fg='white')
                    label.grid(row=0, column=0)

    def create_buttons(self):
        """
        Create navigation buttons for the GUI.

        When the button is clicked, the "move" function will be called and the character will move in the corresponding direction.

        :precondition: GUI root must be initialized already.
        :postcondition: creates navigation buttons for the GUI.
        """
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(side=tk.LEFT, pady=1)
        button_north = tk.Button(self.button_frame, text="Up", command=lambda: self.move('W'))
        button_north.grid(row=0, column=1)
        button_south = tk.Button(self.button_frame, text="Down", command=lambda: self.move('S'))
        button_south.grid(row=2, column=1)
        button_west = tk.Button(self.button_frame, text="Left", command=lambda: self.move('A'))
        button_west.grid(row=1, column=0)
        button_east = tk.Button(self.button_frame, text="Right", command=lambda: self.move('D'))
        button_east.grid(row=1, column=2)

        describe_current_status(self.board, self.character, self.level, self.text_area)
        self.text_area.insert("1.0", ASCII_ART + '\n')

    def create_gui(self):
        """
        Start the main loop.

        :precondition: GUI root must be initialized already.
        :postcondition: main loop started here
        """
        self.root.mainloop()

    def disable_buttons(self):
        """
        Disable the navigation buttons.

        :precondition: GUI root must be initialized already.
        :postcondition: all buttons will be disabled.
        """
        for widget in self.button_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state=tk.DISABLED)

    def __exit__(self):
        """
        Saves the game state when exit.
        """
        current_count = next(self.current_count)
        if not os.path.exists('data'):
            os.makedirs('data')
        board_to_file = {}
        for coordinate, room_description in self.board.items():
            board_to_file[str(coordinate)] = room_description
        with open(f'data/board_{current_count}.json', 'w') as file_object:
            json.dump(board_to_file, file_object)

        with open(f'data/character_{current_count}.json', 'w') as file_object:
            json.dump(self.character, file_object)
        if not self.character['kill_final_boss']:
            print('Your current state is saved. You will be resumed to the same state next time!')


def main():
    """
    Drive the program.
    """
    game_instance = Game()
    atexit.register(game_instance.__exit__)
    game_instance.create_gui()


if __name__ == '__main__':
    main()

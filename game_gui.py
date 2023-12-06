"""
This module serves as a main module to execute the game program.
"""

from board.game_board import make_board, validate_move, move_chocolate, describe_current_status
from character.game_character import make_character, move_character, pick_up_item
from challenges.foes import check_for_foes, fight_with_foe
from teas.teas import ready_to_make_tea, make_tea
from levels.levels import assign_new_task
import tkinter as tk
from GUI.map import get_relief, get_text
import json
import os
import atexit


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

        self.level = len(self.character.get('tea', [])) + 1
        self.create_gui_game_board(self.character['coordinate'])
        self.create_buttons()

    def move(self, direction):
        """
        Move the character in the specified direction and execute the corresponding task in new location.

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
            fight_with_foe(current_room_description, self.character, self.input_frame, self.text_area)

        if self.character['caffeine'] <= 0:
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
                label = tk.Label(master=frame, text=text, width=10, height=4)
                label.grid(row=0, column=0)
                if player[0] == row and player[1] == column:
                    label = tk.Label(master=frame, text='Chris', width=10, height=4, bg='green', fg='white')
                    label.grid(row=0, column=0)

    def create_buttons(self):
        """
        Create navigation buttons for the GUI.

        :precondition: GUI root must be initialized already.
        :postcondition: creates navigation buttons for the GUI.
        """
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.LEFT)
        button_north = tk.Button(button_frame, text="Up", command=lambda: self.move('W'))
        button_north.grid(row=0, column=1)
        button_south = tk.Button(button_frame, text="Down", command=lambda: self.move('S'))
        button_south.grid(row=2, column=1)
        button_west = tk.Button(button_frame, text="Left", command=lambda: self.move('A'))
        button_west.grid(row=1, column=0)
        button_east = tk.Button(button_frame, text="Right", command=lambda: self.move('D'))
        button_east.grid(row=1, column=2)

        describe_current_status(self.board, self.character, self.level, self.text_area)

    def create_gui(self):
        """
        Start the main loop.

        :precondition: GUI root must be initialized already.
        :postcondition: main loop started here
        """
        self.root.mainloop()

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
    game_instance.create_gui()


if __name__ == '__main__':
    main()

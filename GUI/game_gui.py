"""
This module serves as a main module to execute the game program.
"""

import sys
sys.path.append('..')

from board.game_board import make_board, validate_move, move_chocolate, describe_current_status
from character.game_character import make_character, move_character, pick_up_item
from challenges.foes import check_for_foes, fight_with_foe
from teas.teas import ready_to_make_tea, make_tea
from levels.levels import assign_new_task, unlock_next_level_rooms, steps_to_move

import tkinter as tk
from map import create_main_window, get_relief, get_text
from prompts import Prompts


class Game:
    def __init__(self):
        self.rows = 10
        self.columns = 10
        self.character = make_character()
        self.level = 1
        self.board = make_board(self.rows, self.columns)
        self.root = tk.Tk()
        self.root.title('Cup of Tea')
        self.main_frame = tk.Frame(self.root, width=600, height=600)
        self.main_frame.pack(side=tk.LEFT, expand=1)
        self.text_area = tk.Text(self.root, height=10, width=50)
        self.text_area.pack()
        self.input_frame = tk.Frame(self.root, height=2, width=5)
        self.input_frame.pack()
        self.create_gui_game_board()
        self.create_buttons()

    def move(self, direction):
        # steps = steps_to_move(self.level, direction, self.input_frame)
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
        describe_current_status(self.board, self.character, self.text_area)

        current_room_description = self.board[self.character['coordinate']]
        there_is_a_challenger = check_for_foes(current_room_description)

        if there_is_a_challenger:
            fight_with_foe(current_room_description, self.character, self.input_frame)

        if current_room_description[2] == 'Chocolate':
            self.character['caffeine'] += 10
            message = f'You consumed chocolate, now your caffeine level increased to {self.character["caffeine"]}.\n'
            self.text_area.insert(tk.END, message)
            move_chocolate(self.board, self.character)

        if self.character['kill_final_boss']:
            self.text_area.insert(tk.END, 'Congratulations! You won!\n')
            return

        if current_room_description[2] not in ('Nothing', 'Door', 'Joey and Hsin', 'Origin'):
            pick_up_item(self.character, self.board)
            tea_ingredients_all_set = ready_to_make_tea(self.level, self.character)

            if tea_ingredients_all_set:
                make_tea(self.level, self.character)
                self.level += 1
                self.text_area.insert(tk.END, f'Nice job! You leveled up. Now your level is {self.level}.\n')
                assign_new_task(self.level)
                # unlock_next_level_rooms(self.level, self.board)
                self.create_gui_game_board(self.character['coordinate'])

        if self.character['caffeine'] <= 0:
            self.text_area.insert(tk.END, 'Game Over!\n')

    def create_gui_game_board(self, player=(0, 0)):
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
                    label = tk.Label(master=frame, text='Chris', width=10, height=4)
                    label.grid(row=0, column=0)

    def create_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.LEFT)
        button_north = tk.Button(button_frame, text="North", command=lambda: self.move('N'))
        button_north.grid(row=0, column=1)
        button_south = tk.Button(button_frame, text="South", command=lambda: self.move('S'))
        button_south.grid(row=2, column=1)
        button_west = tk.Button(button_frame, text="West", command=lambda: self.move('W'))
        button_west.grid(row=1, column=0)
        button_east = tk.Button(button_frame, text="East", command=lambda: self.move('E'))
        button_east.grid(row=1, column=2)

        describe_current_status(self.board, self.character, self.text_area)

    def create_gui(self):
        self.root.mainloop()


def main():
    Game().create_gui()


if __name__ == '__main__':
    main()
    import json
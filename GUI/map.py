import json
import tkinter as tk
from prompts import prompt


def get_relief(room_description, current_level):
    border_effects = {
        "locked": tk.FLAT,
        "other": tk.SUNKEN,
        "item": tk.RAISED,
        "chocolate": tk.GROOVE,
        "door": tk.RIDGE,
    }
    level, room, item = room_description
    if level > current_level:
        relief = border_effects['locked']
    elif item == 'Door':
        relief = border_effects['door']
    elif item == 'Nothing':
        relief = border_effects['other']
    else:
        relief = border_effects['item']
    return relief


def get_text(room_description, current_level):
    level, room, item = room_description
    text = ''
    if level <= current_level:
        if room in ('Kitchen', 'Grocery Store', 'Market'):
            text += room
        if item != 'Nothing':
            text = item
    return text


def create_main_window(game_board, rows, columns, current_level):
    root = tk.Tk()
    root.title('Cup of Tea')

    main_frame = tk.Frame(root, width=600, height=600)
    main_frame.pack(side=tk.LEFT, expand=1)

    for row in range(rows):
        for column in range(columns):
            room_description = game_board[(row, column)]
            relief = get_relief(room_description, current_level)
            text = get_text(room_description, current_level)
            frame = tk.Frame(master=main_frame, width=50, height=50, relief=relief, borderwidth=2)
            frame.grid(row=row, column=column)
            label = tk.Label(master=frame, text=text, width=10, height=4)
            label.grid(row=0, column=0)
            if row == 0 and column == 0:
                label = tk.Label(master=frame, text='Chris', width=10, height=4)
                label.grid(row=0, column=0)
    prompt(root)
    root.mainloop()


if __name__ == '__main__':
    import sys
    sys.path.append('..')
    with open('data/board.json') as file_object:
        board_json = json.load(file_object)
    board = {}
    for k, v in board_json.items():
        board[tuple(int(x) for x in k.replace('(', '').replace(')', '').split(', '))] = v
    create_main_window(board, 10, 10, 4)

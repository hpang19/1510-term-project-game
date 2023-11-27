"""
This module serves as a main module to execute the game program.
"""

from board.game_board import make_board, validate_move, move_chocolate
from character.game_character import make_character, move_character, pick_up_item
from challenges.foes import check_for_foes, fight_with_foe
from teas.teas import ready_to_make_tea, make_tea
from levels.levels import assign_new_task, unlock_next_level_rooms


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character()
    level = 1
    print('Welcome to the game!')
    while character['caffeine'] > 0:
        direction = input('Please select your direction: [N]: North  [S]: South  [W]: West  [E]: East: ')
        if direction.upper() not in ['N', 'S', 'W', 'E']:
            print("Invalid direction!")
            continue
        valid_move = validate_move(level, board, character, direction)
        if not valid_move:
            print('You can not go in this direction, please choose direction again.')
            continue
        move_character(character, direction)
        current_room = board[character['coordinate']]
        there_is_a_challenger = check_for_foes(current_room)
        print(there_is_a_challenger)
        if there_is_a_challenger:
            fight_with_foe(current_room, character)
        if character['kill_final_boss']:
            print('Congratulation! You won!')
            break
        if current_room[2] == 'Chocolate Room':
            character['caffeine'] += 10
            move_chocolate(board)
        elif current_room[2] != 'Empty Room':
            pick_up_item(character, board)
            tea_ingredients_all_set = ready_to_make_tea(level, character)
            if tea_ingredients_all_set:
                make_tea(level, character)
                level += 1
                assign_new_task(level)
                unlock_next_level_rooms(level, board)
    if character['caffeine'] <= 0:
        print('Game Over!')


def main():
    game()


if __name__ == '__main__':
    main()

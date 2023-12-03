"""
This module serves as a main module to execute the game program.
"""

from board.game_board import make_board, validate_move, move_chocolate, describe_current_status
from character.game_character import make_character, move_character, pick_up_item
from challenges.foes import check_for_foes, fight_with_foe
from teas.teas import ready_to_make_tea, make_tea
from levels.levels import assign_new_task, unlock_next_level_rooms, steps_to_move


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character()
    level = 1
    total_moves = 0
    print('Welcome to the game!')
    describe_current_status(board, character, level)
    while character['caffeine'] > 0:
        direction = input('Please select your direction: [W]: Up  [S]: Down  [A]: Left  [D]: Right: ')
        print(f'=========================================== {total_moves} ===========================================')
        total_moves += 1
        if direction.upper() not in ['W', 'S', 'A', 'D']:
            print("!!! Invalid direction !!!")
            continue
        # steps = steps_to_move(level, direction.upper())
        valid_move = validate_move(level, board, character, direction, steps=1)
        if not valid_move:
            print('!!! You can not go in this direction, please choose direction again. !!!')
            continue
        move_character(character, direction, steps=1)
        current_room_description = board[character['coordinate']]
        if current_room_description[2] == 'Chocolate':
            character['caffeine'] += 10
            print(f'You consumed chocolate, now your caffeine level increased to {character["caffeine"]}.')
            move_chocolate(board, character)
        if current_room_description[2] not in ('Nothing', 'Door', 'Joey and Hsin', 'Origin'):
            pick_up_item(character, board)
            tea_ingredients_all_set = ready_to_make_tea(level, character)
            if tea_ingredients_all_set:
                make_tea(level, character)
                level += 1
                print(f'Nice job! You leveled up. Now your level is {level}.')
                assign_new_task(level)
                unlock_next_level_rooms(level, board)
        describe_current_status(board, character, level)
        there_is_a_challenger = check_for_foes(current_room_description)
        if there_is_a_challenger:
            fight_with_foe(current_room_description, character)
        if character['kill_final_boss']:
            print('Congratulation! You won!')
            break
    if character['caffeine'] <= 0:
        print('Game Over!')


def main():
    game()


if __name__ == '__main__':
    main()

"""
This module serves as a main module to execute the game program.
"""


def make_board(rows, columns):
    pass


def make_character():
    """
    Create a character.

    The character's caffeine starts at 50 at level 1, and it has empty shopping bag and no tea consumed at the
    beginning of the game, the final boss hasn't been killed.

    :postcondition: return a dictionary as an initial character
    :return: a dictionary representing the character

    >>> make_character()
    {'caffeine': 50, 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
    """
    character = {
        'caffeine': 50,
        'shopping_bag': [],
        'tea': [],
        'kill_final_boss': False
    }
    return character


def validate_move(level, board, character, direction):
    pass


def move_character(character, direction):
    pass


def get_current_location(board, character):
    pass


def check_for_foes(current_room):
    pass


def fight_with_foe(current_room, character):
    pass


def move_chocolate(board):
    pass


def pick_up_item(character, board):
    pass


def ready_to_make_tea(level, character):
    pass


def make_tea(level, character):
    pass


def assign_new_task(level):
    pass


def unlock_next_level_rooms(level, board):
    pass


def game():
    rows = 10
    columns = 10
    board = make_board(rows, columns)
    character = make_character()
    level = 1
    print('Welcome to the game!')
    while character['caffeine'] > 0:
        direction = input('Please select your direction: [1]: North  [2]: South  [3]: West  [4]: East: ')
        valid_move = validate_move(level, board, character, direction)
        if not valid_move:
            print('You can not go in this direction, please choose direction again.')
            continue
        move_character(character, direction)
        current_room = get_current_location(board, character)
        there_is_a_challenger = check_for_foes(current_room)
        if there_is_a_challenger:
            fight_with_foe(current_room, character)
        if character['kill_final_boss']:
            print('Congratulation! You won!')
            break
        if current_room == 'Chocolate Room':
            character['caffeine'] += 10
            move_chocolate(board)
        elif current_room != 'Empty Room':
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

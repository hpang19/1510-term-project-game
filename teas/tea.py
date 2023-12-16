"""
This module includes all features related to the teas.
"""

from teas import TEA_MAP
from GUI import prompts
from board.game_board import describe_current_status


def ready_to_make_tea(level: int, character: dict) -> bool:
    """
    Checks if the character is ready to make the tea at the given level.

    :param level: an integer representing the current level
    :param character: a dictionary representing the game character
    :precondition: character contains "shopping_bag" in the key
    :postcondition: return True if the character has all required materials, False otherwise
    :return: a boolean

    >>> character_test = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
    >>> ready_to_make_tea(1, character_test)
    False

    >>> character_test = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': ["Hot Water", "Mug", "Tea Bag"],
    ... 'tea': [], 'kill_final_boss': False}
    >>> ready_to_make_tea(1, character_test)
    True
    """
    if level == 1:
        tea_bag_materials = {"Hot Water", "Mug", "Tea Bag"}
        return tea_bag_materials.issubset(character["shopping_bag"])
    if level == 2:
        matcha_materials = {'Hot Water', 'Mug', 'Matcha Powder', 'Honey', 'Almond Milk', 'Spoon'}
        return matcha_materials.issubset(character["shopping_bag"])
    if level == 3:
        ginger_tea_materials = {'Hot Water', 'Mug', 'Ginger', 'Turmeric', 'Grater', 'Spoon'}
        return ginger_tea_materials.issubset(character["shopping_bag"])


def make_tea(board: dict, level: int, character: dict, text_area_object=None):
    """
    Print a message saying player has made tea for the character at the given level and increases their caffeine.

    :param board: a dictionary representing the board
    :param level: an integer representing the current level
    :param character: a dictionary representing the game character
    :precondition: character contains "tea" and "caffeine" in the key
    :postcondition: increase character's caffeine level

    >>> character_test = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
    >>> make_tea(1, character_test)
    You made Tea Bag, drink it, and your caffeine increased to 100
    """
    character['tea'].append(TEA_MAP[level])
    character['caffeine'] += 50 * level
    items_to_remove = set(character['shopping_bag']).symmetric_difference({'Hot Water', 'Mug', 'Spoon'})
    for item in items_to_remove:
        character['shopping_bag'].remove(item)
    message = f'You made {TEA_MAP[level]}, drink it, and your caffeine increased to {character["caffeine"]}\n'
    describe_current_status(board, character, level, text_area_object)
    prompts.print_message(message, text_area_object)

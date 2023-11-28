"""
This module includes all features related to the teas.
"""


def ready_to_make_tea(level, character):
    """
    >>> level_doctest01 = 1
    >>> character_doctest01 = {
    ...    'caffeine': 50,
    ...    'coordinate': (0, 0),
    ...    'shopping_bag': [],
    ...    'tea': [],
    ...    'kill_final_boss': False
    ...}
    >>> ready_to_make_tea(level_doctest01, character_doctest01)
    False

    """
    if level == 1 and all("Hot Water" and "Mug" and "Tea Bag") in character["shopping_bag"]:
        return True
    if (level == 2 and all("Hot Water" and "Mug" and "Matcha Powder" and "Honey" and "Almond Milk" and "Spoon")
            in character["shopping_bag"]):
        return True
    if (level == 3 and all("Hot Water" and "Mug" and "Ginger" and "Turmeric" and "Grater" and "Spoon")
            in character["shopping_bag"]):
        return True


def make_tea(level, character):
    pass

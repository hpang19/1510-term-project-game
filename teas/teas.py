"""
This module includes all features related to the teas.
"""


def ready_to_make_tea(level, character):
    """
    >>> level_doctest01 = 1
    >>> character_doctest01 = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
    >>> ready_to_make_tea(level_doctest01, character_doctest01)
    False

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


def make_tea(level, character):
    pass

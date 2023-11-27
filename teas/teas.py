"""
This module includes all features related to the teas.
"""


def ready_to_make_tea(level, character):
    if level == 1:
        if "Hot Water" and "Mug" and "Tea Bag" in character["shopping_bag"]:
            return True
    if level == 2:
        if ("Hot Water" and "Mug" and "Matcha Powder" and "Honey" and "Almond Milk" and "Spoon"
                in character["shopping_bag"]):
            return True



def make_tea(level, character):
    pass

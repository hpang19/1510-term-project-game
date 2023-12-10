from unittest import TestCase
from teas.tea import ready_to_make_tea


class Test(TestCase):
    def test_level_1_ready(self):
        character = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': ["Hot Water", "Mug", "Tea Bag"],
                     'tea': [], 'kill_final_boss': False}
        self.assertTrue(ready_to_make_tea(1, character))

    def test_level_1_not_ready(self):
        character = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
        self.assertFalse(ready_to_make_tea(1, character))

    def test_level_2_ready(self):
        character = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': ['Hot Water', 'Mug', 'Matcha Powder',
                     'Honey', 'Almond Milk', 'Spoon'], 'tea': [], 'kill_final_boss': False}
        self.assertTrue(ready_to_make_tea(2, character))

    def test_level_2_not_ready(self):
        character = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': ["Hot Water", "Mug", "Tea Bag"], 'tea': [],
                     'kill_final_boss': False}
        self.assertFalse(ready_to_make_tea(2, character))

    def test_level_3_ready(self):
        character = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': ['Hot Water', 'Mug', 'Ginger', 'Turmeric',
                     'Grater', 'Spoon'], 'tea': [], 'kill_final_boss': False}
        self.assertTrue(ready_to_make_tea(3, character))

    def test_level_3_not_ready(self):
        character = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': ["Hot Water", "Mug", "Tea Bag"], 'tea': [],
                     'kill_final_boss': False}
        self.assertFalse(ready_to_make_tea(3, character))


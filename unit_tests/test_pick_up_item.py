from unittest import TestCase
from character.game_character import pick_up_item

class Test(TestCase):
    def test_ingredients_check_shopping_bag(self):
        character_test = {'coordinate': (3, 3), 'shopping_bag': []}
        board_test = {(3, 3): ['Room', 'Room', 'Matcha Powder']}
        pick_up_item(character_test, board_test)
        actual_output = character_test['shopping_bag']
        expected_output = ['Matcha Powder']
        self.assertEqual(actual_output, expected_output)

    def test_ingredients_check_board(self):
        character_test = {'coordinate': (3, 3), 'shopping_bag': []}
        board_test = {(3, 3): ['Room', 'Room', 'Matcha Powder']}
        pick_up_item(character_test, board_test)
        actual_output = board_test[(3, 3)][2]
        expected_output = "Nothing"
        self.assertEqual(actual_output, expected_output)

    def test_no_item_check_shopping_bag(self):
        character_test = {'coordinate': (2, 2), 'shopping_bag': []}
        board_test = {(2, 2): ['Room', 'Room', 'Nothing']}
        pick_up_item(character_test, board_test)
        actual_output = character_test['shopping_bag']
        expected_output = []
        self.assertEqual(actual_output, expected_output)

    def test_no_item_check_board(self):
        character_test = {'coordinate': (2, 2), 'shopping_bag': []}
        board_test = {(2, 2): ['Room', 'Room', 'Nothing']}
        pick_up_item(character_test, board_test)
        actual_output = board_test[(2, 2)][2]
        expected_output = "Nothing"
        self.assertEqual(actual_output, expected_output)

    def test_door_check_shopping_bag(self):
        character_test = {'coordinate': (4, 4), 'shopping_bag': []}
        board_test = {(4, 4): ['Room', 'Room', 'Door']}
        pick_up_item(character_test, board_test)
        actual_output = character_test['shopping_bag']
        expected_output = []
        self.assertEqual(actual_output, expected_output)

    def test_door_check_board(self):
        character_test = {'coordinate': (4, 4), 'shopping_bag': []}
        board_test = {(4, 4): ['Room', 'Room', 'Door']}
        pick_up_item(character_test, board_test)
        actual_output = board_test[(4, 4)][2]
        expected_output = "Door"
        self.assertEqual(actual_output, expected_output)

    def test_chocolate_check_shopping_bag(self):
        character_test = {'coordinate': (1, 1), 'shopping_bag': []}
        board_test = {(1, 1): ['Room', 'Room', 'Chocolate']}
        pick_up_item(character_test, board_test)
        actual_output = character_test['shopping_bag']
        expected_output = []
        self.assertEqual(actual_output, expected_output)

    def test_chocolate_check_board(self):
        character_test = {'coordinate': (1, 1), 'shopping_bag': []}
        board_test = {(1, 1): ['Room', 'Room', 'Chocolate']}
        pick_up_item(character_test, board_test)
        actual_output = board_test[(1, 1)][2]
        expected_output = "Chocolate"
        self.assertEqual(actual_output, expected_output)

    def test_origin_check_shopping_bag(self):
        character_test = {'coordinate': (0, 0), 'shopping_bag': []}
        board_test = {(0, 0): ['Room', 'Room', 'Origin']}
        pick_up_item(character_test, board_test)
        actual_output = character_test['shopping_bag']
        expected_output = []
        self.assertEqual(actual_output, expected_output)

    def test_origin_check_board(self):
        character_test = {'coordinate': (0, 0), 'shopping_bag': []}
        board_test = {(0, 0): ['Room', 'Room', 'Origin']}
        pick_up_item(character_test, board_test)
        actual_output = board_test[(0, 0)][2]
        expected_output = "Origin"
        self.assertEqual(actual_output, expected_output)

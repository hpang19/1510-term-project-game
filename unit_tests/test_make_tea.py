from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from teas.tea import make_tea


class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_1_print(self, mock_output):
        character = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [],
                     'kill_final_boss': False}
        expected_output = "You made Tea Bag, drink it, and your caffeine increased to 100\n"
        make_tea(1, character)
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_level_1_tea_list(self):
        character = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
        make_tea(1, character)
        self.assertIn('Tea Bag', character['tea'])

    def test_level_1_caffeine(self):
        character = {'caffeine': 50, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
        current_caffeine = character['caffeine']
        make_tea(1, character)
        self.assertEqual(current_caffeine + 50, character['caffeine'])

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_2(self, mock_output):
        character = {'caffeine': 150, 'coordinate': (6, 8), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
        expected_output = "You made Matcha, drink it, and your caffeine increased to 250\n"
        make_tea(2, character)
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_level_2_tea_list(self):
        character = {'caffeine': 150, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
        make_tea(2, character)
        self.assertIn('Matcha', character['tea'])

    def test_level_2_caffeine(self):
        character = {'caffeine': 150, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
        current_caffeine = character['caffeine']
        make_tea(2, character)
        self.assertEqual(current_caffeine + 100, character['caffeine'])

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_3(self, mock_output):
        character = {'caffeine': 250, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
        expected_output = "You made Ginger Tea, drink it, and your caffeine increased to 400\n"
        make_tea(3, character)
        self.assertEqual(mock_output.getvalue(), expected_output)

    def test_level_3_tea_list(self):
        character = {'caffeine': 250, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
        make_tea(3, character)
        self.assertIn('Ginger Tea', character['tea'])

    def test_level_3_caffeine(self):
        character = {'caffeine': 250, 'coordinate': (0, 0), 'shopping_bag': [], 'tea': [], 'kill_final_boss': False}
        current_caffeine = character['caffeine']
        make_tea(3, character)
        self.assertEqual(current_caffeine + 150, character['caffeine'])
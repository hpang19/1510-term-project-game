from unittest import TestCase
from unittest.mock import patch
from board.rooms import random_choice_coordinate


class Test(TestCase):
    @patch('random.choice', side_effect=lambda sequence: sequence[0])
    def test_choose_origin(self, _):
        actual_output = random_choice_coordinate((5, 5), 3, 3)
        expected_output = (5, 5)
        self.assertEqual(actual_output, expected_output)

    @patch('random.choice', side_effect=lambda sequence: sequence[-1])
    def test_choose_destination(self, _):
        actual_output = random_choice_coordinate((5, 5), 3, 3)
        expected_output = (7, 7)
        self.assertEqual(actual_output, expected_output)

    @patch('random.choice', side_effect=lambda sequence: sequence[1])
    def test_choose_middle(self, _):
        actual_output = random_choice_coordinate((5, 5), 3, 3)
        expected_output = (6, 6)
        self.assertEqual(actual_output, expected_output)

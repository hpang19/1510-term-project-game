from unittest import TestCase
from character.game_character import move_character


class Test(TestCase):
    def test_move_down_from_center(self):
        character = {'coordinate': (5, 5)}
        move_character(character, 'S', 2)
        expected_output = (7, 5)
        self.assertEqual(character['coordinate'], expected_output)

    def test_move_down_from_down(self):
        character = {'coordinate': (8, 5)}
        move_character(character, 'S', 1)
        expected_output = (9, 5)
        self.assertEqual(character['coordinate'], expected_output)

    def test_move_up_from_center(self):
        character = {'coordinate': (5, 5)}
        move_character(character, 'W', 2)
        expected_output = (3, 5)
        self.assertEqual(character['coordinate'], expected_output)

    def test_move_up_from_up(self):
        character = {'coordinate': (1, 5)}
        move_character(character, 'W', 1)
        expected_output = (0, 5)
        self.assertEqual(character['coordinate'], expected_output)

    def test_move_left_from_center(self):
        character = {'coordinate': (5, 5)}
        move_character(character, 'A', 2)
        expected_output = (5, 3)
        self.assertEqual(character['coordinate'], expected_output)

    def test_move_left_from_left(self):
        character = {'coordinate': (5, 1)}
        move_character(character, 'A', 1)
        expected_output = (5, 0)
        self.assertEqual(character['coordinate'], expected_output)

    def test_move_right_from_center(self):
        character = {'coordinate': (5, 5)}
        move_character(character, 'D', 2)
        expected_output = (5, 7)
        self.assertEqual(character['coordinate'], expected_output)

    def test_move_right_from_right(self):
        character = {'coordinate': (5, 8)}
        move_character(character, 'D', 1)
        expected_output = (5, 9)
        self.assertEqual(character['coordinate'], expected_output)

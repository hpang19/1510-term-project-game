from unittest import TestCase
from board.game_board import validate_move


class Test(TestCase):
    def test_valid_move_right(self):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
        character = {'coordinate': (0, 0)}
        result = validate_move(1, board, character, 'D', 1)
        self.assertTrue(result)

    def test_valid_move_left(self):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
        character = {'coordinate': (0, 1)}
        result = validate_move(1, board, character, 'A', 1)
        self.assertTrue(result)

    def test_valid_move_up(self):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
        character = {'coordinate': (1, 0)}
        result = validate_move(1, board, character, 'W', 1)
        self.assertTrue(result)

    def test_valid_move_down(self):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
        character = {'coordinate': (0, 0)}
        result = validate_move(2, board, character, 'S', 1)
        self.assertTrue(result)

    def test_invalid_move_left(self):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
        character = {'coordinate': (0, 0)}
        result = validate_move(1, board, character, 'A', 1)
        self.assertFalse(result)

    def test_invalid_move_right(self):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
        character = {'coordinate': (0, 1)}
        result = validate_move(1, board, character, 'D', 1)
        self.assertFalse(result)

    def test_invalid_move_up(self):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
        character = {'coordinate': (0, 0)}
        result = validate_move(1, board, character, 'W', 1)
        self.assertFalse(result)

    def test_invalid_move_down(self):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
        character = {'coordinate': (1, 0)}
        result = validate_move(2, board, character, 'S', 1)
        self.assertFalse(result)

    def test_cross_level_move_valid(self):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
        character = {'coordinate': (0, 0)}
        result = validate_move(2, board, character, 'S', 1)
        self.assertTrue(result)

    def test_cross_level_move_invalid(self):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Door']}
        character = {'coordinate': (0, 0)}
        result = validate_move(1, board, character, 'S', 1)
        self.assertFalse(result)

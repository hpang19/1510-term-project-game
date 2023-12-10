from unittest import TestCase
from unittest.mock import patch
from board.game_board import move_chocolate


class Test(TestCase):
    @patch('random.choice', return_value=(1, 1))
    def test_chocolate_removed_from_cuurent_location(self, _):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 1)}
        move_chocolate(board, character)
        self.assertEqual(board[character['coordinate']][2], 'Nothing')

    @patch('random.choice', return_value=(1, 1))
    def test_chocolate_appears_in_new_location(self, _):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 1)}
        move_chocolate(board, character)
        self.assertEqual(board[(1, 1)][2], 'Chocolate')

    @patch('random.choice', side_effect=[(0, 0), (1, 1)])
    def test_chocolate_removed_from_cuurent_location_second_try(self, _):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 1)}
        move_chocolate(board, character)
        self.assertEqual(board[character['coordinate']][2], 'Nothing')

    @patch('random.choice', side_effect=[(0, 0), (1, 1)])
    def test_chocolate_appears_in_new_location_second_try(self, _):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Chocolate'],
                 (1, 0): [2, 'Kitchen', 'Nothing'], (1, 1): [2, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 1)}
        move_chocolate(board, character)
        self.assertEqual(board[(1, 1)][2], 'Chocolate')

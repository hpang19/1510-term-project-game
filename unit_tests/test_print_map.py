from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from board.game_board import print_map


class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_in_special_room(self, mock_stdout):
        board = {(0, 0): [1, 'Kitchen', 'Nothing'], (0, 1): [1, 'Kitchen', 'Nothing'],
                 (1, 0): [1, 'Kitchen', 'Nothing'], (1, 1): [1, 'Kitchen', 'Nothing']}
        character = {'coordinate': (1, 0)}
        expected_map_output = (
            '[_][_]\n'
            '[*][_]\n'
        )
        print_map(character, board, 1, 2, 2)
        printed_output = mock_stdout.getvalue()
        self.assertEqual(printed_output, expected_map_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_on_the_street(self, mock_stdout):
        board = {(0, 0): [1, 'Street', 'Nothing'], (0, 1): [1, 'Street', 'Nothing'],
                 (1, 0): [1, 'Street', 'Nothing'], (1, 1): [1, 'Street', 'Nothing']}
        character = {'coordinate': (1, 0)}
        expected_map_output = (
            '[ ][ ]\n'
            '[*][ ]\n'
        )
        print_map(character, board, 1, 2, 2)
        printed_output = mock_stdout.getvalue()
        self.assertEqual(printed_output, expected_map_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_door(self, mock_stdout):
        board = {(0, 0): [1, 'Street', 'Nothing'], (0, 1): [1, 'Street', 'Nothing'],
                 (1, 0): [1, 'Street', 'Nothing'], (1, 1): [1, 'Street', 'Door']}
        character = {'coordinate': (1, 0)}
        expected_map_output = (
            '[ ][ ]\n'
            '[*][/]\n'
        )
        print_map(character, board, 1, 2, 2)
        printed_output = mock_stdout.getvalue()
        self.assertEqual(printed_output, expected_map_output)

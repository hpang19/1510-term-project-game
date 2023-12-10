from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from board.game_board import describe_current_status, print_map


class Test(TestCase):
    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_kitchen_level_1(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Origin'], (0, 1): [1, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 1)
        printed_output = mock_stdout.getvalue()
        self.assertIn('Current Level: level 1', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_kitchen_level_2(self, mock_stdout, _):
        board = {(0, 0): [2, 'Grocery Store', 'Door'], (0, 1): [2, 'Grocery Store', 'Nothing']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 2)
        printed_output = mock_stdout.getvalue()
        self.assertIn('Current Level: level 2', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_kitchen_level_3(self, mock_stdout, _):
        board = {(0, 0): [3, 'Market', 'Ginger'], (0, 1): [3, 'Market', 'Nothing']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 3)
        printed_output = mock_stdout.getvalue()
        self.assertIn('Current Level: level 3', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_kitchen_level_4(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Origin'], (0, 1): [4, 'Destination', 'Joey and Hsin']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 4)
        printed_output = mock_stdout.getvalue()
        self.assertIn('Current Level: level 4', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_kitchen_item(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Grater'], (0, 1): [1, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 0), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 1)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Kitchen with grater', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_kitchen_door(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Door'], (0, 1): [1, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 0), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 1)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Kitchen with door', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_kitchen_nothing(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Origin'], (0, 1): [1, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 1)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Kitchen with nothing', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_grocery_store_item(self, mock_stdout, _):
        board = {(0, 0): [2, 'Grocery Store', 'Honey'], (0, 1): [2, 'Grocery Store', 'Nothing']}
        character = {'coordinate': (0, 0), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 2)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Grocery Store with honey', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_grocery_store_door(self, mock_stdout, _):
        board = {(0, 0): [2, 'Grocery Store', 'Door'], (0, 1): [2, 'Grocery Store', 'Nothing']}
        character = {'coordinate': (0, 0), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 2)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Grocery Store with door', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_grocery_store_nothing(self, mock_stdout, _):
        board = {(0, 0): [2, 'Grocery Store', 'Origin'], (0, 1): [2, 'Grocery Store', 'Nothing']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 2)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Grocery Store with nothing', printed_output)


    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_market_item(self, mock_stdout, _):
        board = {(0, 0): [3, 'Market', 'Ginger'], (0, 1): [3, 'Market', 'Nothing']}
        character = {'coordinate': (0, 0), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 3)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Market with ginger', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_market_door(self, mock_stdout, _):
        board = {(0, 0): [3, 'Market', 'Door'], (0, 1): [3, 'Market', 'Nothing']}
        character = {'coordinate': (0, 0), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 3)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Market with door', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_market_nothing(self, mock_stdout, _):
        board = {(0, 0): [3, 'Market', 'Ginger'], (0, 1): [3, 'Market', 'Nothing']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 3)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Market with nothing', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_street(self, mock_stdout, _):
        board = {(0, 0): [2, 'Street', 'Nothing'], (0, 1): [2, 'Grocery Store', 'Nothing']}
        character = {'coordinate': (0, 0), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 2)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Street with nothing', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_origin(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Origin'], (0, 1): [1, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 0), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 1)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Kitchen with origin', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_destination(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Origin'], (0, 1): [4, 'Destination', 'Joey and Hsin']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 4)
        printed_output = mock_stdout.getvalue()
        self.assertIn('You are in the Destination', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_shopping_bag_empty(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Origin'], (0, 1): [1, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 1)
        printed_output = mock_stdout.getvalue()
        self.assertIn('Shopping Bag: []', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_shopping_bag_not_empty(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Origin'], (0, 1): [1, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': ['Spoon'], 'tea': []}
        describe_current_status(board, character, 1)
        printed_output = mock_stdout.getvalue()
        self.assertIn("Shopping Bag: ['Spoon']", printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_teas_empty(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Origin'], (0, 1): [1, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': []}
        describe_current_status(board, character, 1)
        printed_output = mock_stdout.getvalue()
        self.assertIn('Teas you have made:[]', printed_output)

    @patch('board.game_board.print_map', return_value='')
    @patch('sys.stdout', new_callable=StringIO)
    def test_teas_not_empty(self, mock_stdout, _):
        board = {(0, 0): [1, 'Kitchen', 'Origin'], (0, 1): [1, 'Kitchen', 'Nothing']}
        character = {'coordinate': (0, 1), 'caffeine': 100, 'shopping_bag': [], 'tea': ['Tea Bag']}
        describe_current_status(board, character, 1)
        printed_output = mock_stdout.getvalue()
        self.assertIn("Teas you have made:['Tea Bag']", printed_output)

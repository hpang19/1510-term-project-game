from unittest import TestCase
from challenges.foes import penalty


class Test(TestCase):
    def test_deducted_caffeine_positive(self):
        character = {'caffeine': 100, 'game_over': False}
        penalty('A', character, 10, None)
        actual_output = character['caffeine']
        expected_output = 90
        self.assertEqual(actual_output, expected_output)

    def test_deducted_caffeine_positive_game_over(self):
        character = {'caffeine': 100, 'game_over': False}
        penalty('A', character, 10, None)
        actual_output = character['game_over']
        expected_output = False
        self.assertEqual(actual_output, expected_output)

    def test_deducted_caffeine_zero(self):
        character = {'caffeine': 100, 'game_over': False}
        penalty('A', character, 100, None)
        actual_output = character['caffeine']
        expected_output = 0
        self.assertEqual(actual_output, expected_output)

    def test_deducted_caffeine_zero_game_over(self):
        character = {'caffeine': 100, 'game_over': False}
        penalty('A', character, 100, None)
        actual_output = character['game_over']
        expected_output = True
        self.assertEqual(actual_output, expected_output)

    def test_deducted_caffeine_negative(self):
        character = {'caffeine': 100, 'game_over': False}
        penalty('A', character, 150, None)
        actual_output = character['caffeine']
        expected_output = -50
        self.assertEqual(actual_output, expected_output)

    def test_deducted_caffeine_negative_game_over(self):
        character = {'caffeine': 100, 'game_over': False}
        penalty('A', character, 150, None)
        actual_output = character['game_over']
        expected_output = True
        self.assertEqual(actual_output, expected_output)

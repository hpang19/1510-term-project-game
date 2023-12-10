from unittest import TestCase
from challenges.foes import boss_callback


class Test(TestCase):
    def test_wrong_answer_kill_final_boss(self):
        character = {'kill_final_boss': False, 'caffeine': 100, 'game_over': False}
        boss_callback('A', 'B', character, None)
        self.assertFalse(character['kill_final_boss'])

    def test_wrong_answer_game_over(self):
        character = {'kill_final_boss': False, 'caffeine': 100, 'game_over': False}
        boss_callback('A', 'B', character, None)
        self.assertTrue(character['game_over'])

    def test_wrong_answer_caffeine(self):
        character = {'kill_final_boss': False, 'caffeine': 100, 'game_over': False}
        boss_callback('A', 'B', character, None)
        actual_output = character['caffeine']
        expected_output = -400
        self.assertEqual(actual_output, expected_output)

    def test_correct_answer_kill_final_boss(self):
        character = {'kill_final_boss': False, 'caffeine': 100, 'game_over': False}
        boss_callback('A', 'A', character, None)
        self.assertTrue(character['kill_final_boss'])

    def test_correct_answer_game_over(self):
        character = {'kill_final_boss': False, 'caffeine': 100, 'game_over': False}
        boss_callback('A', 'A', character, None)
        self.assertFalse(character['game_over'])

    def test_correct_answer_caffeine(self):
        character = {'kill_final_boss': False, 'caffeine': 100, 'game_over': False}
        boss_callback('A', 'A', character, None)
        self.assertEqual(character['caffeine'], 100)

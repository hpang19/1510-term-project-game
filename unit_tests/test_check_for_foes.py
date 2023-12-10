from unittest import TestCase
from unittest.mock import patch
from challenges.foes import check_for_foes


class Test(TestCase):
    @patch('random.choice', side_effect=[0, 0])
    def test_check_for_rats_true(self, _):
        current_room_description = [1, 'Kitchen', 'Nothing']
        self.assertTrue(check_for_foes(current_room_description))

    @patch('random.choice', side_effect=[1, 0])
    def test_check_for_rats_false(self, _):
        current_room_description = [1, 'Kitchen', 'Hot Water']
        self.assertFalse(check_for_foes(current_room_description))

    @patch('random.choice', side_effect=[1, 1])
    def test_check_for_dogs_true(self, _):
        current_room_description = [2, 'Grocery Store', 'Nothing']
        self.assertTrue(check_for_foes(current_room_description))

    @patch('random.choice', side_effect=[1, 2])
    def test_check_for_dogs_false(self, _):
        current_room_description = [2, 'Street', 'Nothing']
        self.assertFalse(check_for_foes(current_room_description))

    @patch('random.choice', side_effect=[2, 2])
    def test_check_for_kids_true(self, _):
        current_room_description = [3, 'Street', 'Nothing']
        self.assertTrue(check_for_foes(current_room_description))

    @patch('random.choice', side_effect=[2, 1])
    def test_check_for_kids_false(self, _):
        current_room_description = [3, 'Market', 'Nothing']
        self.assertFalse(check_for_foes(current_room_description))

    def test_check_for_boss_true(self):
        current_room_description = [4, 'Destination', 'Joey and Hsin']
        self.assertTrue(check_for_foes(current_room_description))

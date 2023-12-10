from unittest import TestCase
from challenges.foes import get_foe


class Test(TestCase):
    def test_kitchen(self):
        current_room_description = [1, 'Kitchen', 'Nothing']
        actual_output = get_foe(current_room_description)
        expected_output = 'rats'
        self.assertEqual(actual_output, expected_output)

    def test_kitchen_with_item(self):
        current_room_description = [1, 'Kitchen', 'Hot Water']
        actual_output = get_foe(current_room_description)
        expected_output = 'rats'
        self.assertEqual(actual_output, expected_output)

    def test_grocery_store(self):
        current_room_description = [2, 'Grocery Store', 'Nothing']
        expected_output = 'dogs'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

    def test_grocery_store_with_item(self):
        current_room_description = [2, 'Grocery Store', 'Matcha Powder']
        expected_output = 'dogs'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

    def test_street_level_2(self):
        current_room_description = [2, 'Street', 'Nothing']
        expected_output = 'dogs'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

    def test_traditional_market(self):
        current_room_description = [2, 'Market', 'Nothing']
        expected_output = 'kids'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

    def test_traditional_market_with_item(self):
        current_room_description = [2, 'Market', 'Ginger']
        expected_output = 'kids'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

    def test_street_level_3(self):
        current_room_description = [3, 'Street', 'Nothing']
        expected_output = 'kids'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

    def test_destination(self):
        current_room_description = [4, 'Destination', 'Joey and Hsin']
        expected_output = 'Joey and Hsin'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

    def test_origin(self):
        current_room_description = [4, 'Kitchen', 'Origin']
        expected_output = 'rats'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

    def test_kitchen_door(self):
        current_room_description = [1, 'Kitchen', 'Door']
        expected_output = 'rats'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

    def test_grocery_store_door(self):
        current_room_description = [2, 'Grocery Store', 'Door']
        expected_output = 'dogs'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

    def test_market_door(self):
        current_room_description = [2, 'Market', 'Door']
        expected_output = 'kids'
        actual_output = get_foe(current_room_description)
        self.assertEqual(actual_output, expected_output)

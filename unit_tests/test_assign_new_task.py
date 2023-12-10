from unittest import TestCase
from unittest.mock import patch
from io import StringIO
from levels.level import assign_new_task


class Test(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_level_1(self, mock_output):
        assign_new_task(1)
        expected_output = ("Your next task is making a Tea Bag. In order to make Tea Bag, place a tea bag in a mug, "
                           "add hot water, let it steep for 3 to 5 minutes, then remove the bag and enjoy your tea!\n")
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_2(self, mock_output):
        assign_new_task(2)
        expected_output = ("Your next task is making a Matcha. In order to make Matcha, in a mug, "
                           "whisk together 1 teaspoon of matcha powder, 1 tablespoon of honey, and a splash of hot "
                           "water to form a paste, then add ¾ cup of almond milk, whisk until combined, "
                           "and enjoy your matcha latte!\n")
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_3(self, mock_output):
        assign_new_task(3)
        expected_output = ("Your next task is making a Ginger Tea. In order to make Ginger Tea, grate a thumb-sized "
                           "piece of ginger into a mug, add a pinch of turmeric, pour hot water over it, "
                           "stir well with a spoon, and savor your soothing ginger-turmeric tea!\n")
        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_level_4(self, mock_output):
        assign_new_task(4)
        expected_output = ("You are almost there! Now go to the destination, Joey and Hsin are waiting to challenge "
                           "you!\n")
        self.assertEqual(mock_output.getvalue(), expected_output)

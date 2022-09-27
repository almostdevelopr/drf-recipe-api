"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module. """

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 9)

        self.assertEqual(res, 14)

    def test_subtract_numbers(self):
        """Subtract numbers."""
        res = calc.subtract(10, 5)

        self.assertEqual(res, 5)

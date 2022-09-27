"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    """ Test the calc module. """

    def test_add_number(self):
        """Test adding numbers together."""
        res = calc.add(5,9)

        self.assertEqual(res, 14)

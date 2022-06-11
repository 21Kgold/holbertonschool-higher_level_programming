"""
Unittest for rectangle class
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Tests ractangle class
    """

    def test_attributes(self):
        """
        Test attributes
        """
        rec = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.id, 5)
        
        rec = Rectangle(1, 2)
        self.assertEqual(rec.width, 1)
        self.assertEqual(rec.height, 2)
        self.assertEqual(rec.x, 0)
        self.assertEqual(rec.y, 0)
        self.assertEqual(rec.id, 3) 

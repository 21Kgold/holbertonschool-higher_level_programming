"""
Unittest for Square class
"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """
    Tests ractangle class
    """

    def test_attributes(self):
        """
        Test attributes
        """
        sq = Square(1, 2, 3, 4)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 3)
        self.assertEqual(sq.id, 4)
        
        sq = Square(1)
        self.assertEqual(sq.size, 1)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertEqual(sq.id, 4) 

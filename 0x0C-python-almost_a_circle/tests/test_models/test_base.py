"""
Unittest for the Base class
"""


from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest

class TestBase(unittest.TestCase):
    def test_id(self):
        """
        Test id's
        """
        Base.__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(100)
        self.assertEqual(b2.id, 100)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base(0)
        self.assertEqual(b4.id, 0)
        b5 = Base(-100)
        self.assertEqual(b5.id, -100)


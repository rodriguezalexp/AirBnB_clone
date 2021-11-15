#!/usr/bin/python3
""" Test_Amenity: unittest for User module"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """unittest for class Amenity"""
    def setUp(self):
        self.object = Amenity

    def testdocstring(self):
        """class check"""
        self.assertIsNotNone(Amenity.__doc__)

    def testinstance(self):
        """Test if instance belongs to Amenity"""
        self.assertIsInstance(self.object, Amenity)


if __name__ == '__main__':
    unittest.main()

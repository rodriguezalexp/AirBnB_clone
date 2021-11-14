#!/usr/bin/python3
""" Test_BaseModel: unittest for base_model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Class to test BaseModel"""

    def setUp(self):
        self.object = BaseModel()

    def testDocstring_class(self):
        """Check docstring  in class"""
        self.assertIsNotNone(BaseModel.__doc__)

    def test_id(self):
        """Check if id is a string"""
        self.assertEqual(type(self.object.id), str)

    def testinstance(self):
        """Test if the instance belongs to BaseModel class"""
        self.assertIsInstance(self.object, BaseModel)

    def test_addattr(self):
        """Test adding a new attribute"""
        self.object.name = "Edgar"
        self.object.age = 66
        self.assertTrue(isinstance(self.object, BaseModel))

    def test_to_dict(self):
        """Tests the retrieved object is a dictionary"""
        nu_dict = self.object.to_dict()
        self.assertTrue(isinstance(nu_dict, dict))

    def test_save(self):
        """updating a public instance attr updated _at"""
        temp = self.object.updated_at
        self.object.save()
        self.assertNotEqual(temp, self.object.updated_at)


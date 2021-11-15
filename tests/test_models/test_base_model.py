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
        test = BaseModel()
        nu_dict = test.to_dict()
        i_d = test.id
        created = test.created_at.isoformat()
        updated = test.updated_at.isoformat()
        expected = {'_class__': 'Basemodel', 'id': i_d,
                    'updated_at': updated, 'created_at': created}
        self.assertTrue(isinstance(nu_dict, dict))
        self.assertDictEqual(nu_dict, expected)
        test.save()
        self.assertNotEqual(updated, test.updated_at.isoformat())
        self.assertEqual(created, test.created_at.isoformat())

    def test_save(self):
        """updating a public instance attr updated _at"""
        temp = self.object.updated_at
        self.object.save()
        self.assertNotEqual(temp, self.object.updated_at)

    def test_str_repr(self):
        """testing string representation"""
        test = BaseModel()
        t_str = "[{}] ({}) {}".format(test.__class__.__name__,
                                      test.id, test.__dict__)
        self.assertEqual(test.__str__(), t_str)

if __name__ == '__main__':
    unittest.main()

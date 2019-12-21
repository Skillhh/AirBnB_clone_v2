#!/usr/bin/python3
""" Importing necessary modules """
from models.amenity import Amenity
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Test Class. A testcase is created by subclassing unittest.TestCase. """
    def test_class(self):
        """ Testing if class exists. """
        my_model = Amenity()
        help = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(my_model)), help)

    def test_docstring(self):
        """ Testing if docstring is correct """

        self.assertIsNotNone(Amenity.__doc__)

    def test_Is_SubClass_BaseModel(self):
        """ Testing if User() is a subclass of BaseModel"""

        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_has_attr(self):
        """ Testing if user has all of it's attributes """
        my_model = Amenity()

        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertTrue(hasattr(my_model, 'name'))

    def test_type_attr(self):
        """ Testing types of the attributes of the Class """
        my_model = Amenity()

        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.name), str)

if __name__ == '__main__':
    unittest.main()

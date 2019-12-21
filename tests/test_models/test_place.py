#!/usr/bin/python3
""" Importing necessary modules """
from models.place import Place
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """ Test Class. A testcase is created by subclassing unittest.TestCase. """
    def test_class(self):
        """ Testing if class exists. """
        my_model = Place()

        self.assertEqual(str(type(my_model)), "<class 'models.place.Place'>")

    def test_docstring(self):
        """ Testing if docstring is correct """

        self.assertIsNotNone(Place.__doc__)

    def test_Is_SubClass_BaseModel(self):
        """ Testing if User() is a subclass of BaseModel"""

        self.assertTrue(issubclass(Place, BaseModel))

    def test_has_attr(self):
        """ Testing if user has all of it's attributes """
        my_model = Place()

        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertTrue(hasattr(my_model, 'city_id'))
        self.assertTrue(hasattr(my_model, 'user_id'))
        self.assertTrue(hasattr(my_model, 'name'))
        self.assertTrue(hasattr(my_model, 'description'))
        self.assertTrue(hasattr(my_model, 'number_rooms'))
        self.assertTrue(hasattr(my_model, 'number_bathrooms'))
        self.assertTrue(hasattr(my_model, 'max_guest'))
        self.assertTrue(hasattr(my_model, 'price_by_night'))
        self.assertTrue(hasattr(my_model, 'latitude'))
        self.assertTrue(hasattr(my_model, 'longitude'))
        self.assertTrue(hasattr(my_model, 'amenity_ids'))

    def test_type_attr(self):
        """ Testing types of the attributes of the Class """
        my_model = Place()

        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.city_id), str)
        self.assertEqual(type(my_model.user_id), str)
        self.assertEqual(type(my_model.name), str)
        self.assertEqual(type(my_model.description), str)
        self.assertEqual(type(my_model.number_rooms), int)
        self.assertEqual(type(my_model.number_bathrooms), int)
        self.assertEqual(type(my_model.max_guest), int)
        self.assertEqual(type(my_model.price_by_night), int)
        self.assertEqual(type(my_model.latitude), float)
        self.assertEqual(type(my_model.longitude), float)
        self.assertEqual(type(my_model.amenity_ids), list)

if __name__ == '__main__':
    unittest.main()

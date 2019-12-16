#!/usr/bin/python3
""" Importing necessary modules """
from models.review import Review
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ Test Class. A testcase is created by subclassing unittest.TestCase. """
    def test_class(self):
        """ Testing if class exists. """
        my_model = Review()

        self.assertEqual(str(type(my_model)), "<class 'models.review.Review'>")

    def test_docstring(self):
        """ Testing if docstring is correct """

        self.assertIsNotNone(Review.__doc__)

    def test_Is_SubClass_BaseModel(self):
        """ Testing if User() is a subclass of BaseModel"""

        self.assertTrue(issubclass(Review, BaseModel))

    def test_has_attr(self):
        """ Testing if user has all of it's attributes """
        my_model = Review()

        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertTrue(hasattr(my_model, 'place_id'))
        self.assertTrue(hasattr(my_model, 'user_id'))
        self.assertTrue(hasattr(my_model, 'text'))

    def test_type_attr(self):
        """ Testing types of the attributes of the Class """
        my_model = Review()

        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.place_id), str)
        self.assertEqual(type(my_model.user_id), str)
        self.assertEqual(type(my_model.text), str)

if __name__ == '__main__':
    unittest.main()

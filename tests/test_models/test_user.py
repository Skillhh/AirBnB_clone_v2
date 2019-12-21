#!/usr/bin/python3
""" Importing necessary modules """
from models.user import User
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Test Class. A testcase is created by subclassing unittest.TestCase. """
    def test_class(self):
        """ Testing if class exists. """
        my_model = User()

        self.assertEqual(str(type(my_model)), "<class 'models.user.User'>")

    def test_docstring(self):
        """ Testing if docstring is correct """

        self.assertIsNotNone(User.__doc__)

    def test_Is_SubClass_BaseModel(self):
        """ Testing if User() is a subclass of BaseModel"""

        self.assertTrue(issubclass(User, BaseModel))

    def test_has_attr(self):
        """ Testing if user has all of it's attributes """
        my_model = User()

        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))
        self.assertTrue(hasattr(my_model, 'email'))
        self.assertTrue(hasattr(my_model, 'password'))
        self.assertTrue(hasattr(my_model, 'first_name'))
        self.assertTrue(hasattr(my_model, 'last_name'))

    def test_type_attr(self):
        """ Testing types of the attributes of the Class """
        my_model = User()

        self.assertEqual(type(my_model.id), str)
        self.assertEqual(type(my_model.created_at), datetime)
        self.assertEqual(type(my_model.updated_at), datetime)
        self.assertEqual(type(my_model.email), str)
        self.assertEqual(type(my_model.password), str)
        self.assertEqual(type(my_model.first_name), str)
        self.assertEqual(type(my_model.last_name), str)

if __name__ == '__main__':
    unittest.main()

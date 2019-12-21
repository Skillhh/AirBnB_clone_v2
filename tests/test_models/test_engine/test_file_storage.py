#!/usr/bin/python3
""" Importing necessary modules """
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
from datetime import datetime
from os import remove
from models.state import State
from models import storage


class TestFileStorage(unittest.TestCase):
    """ Test class. A testcase is created by subclassing unittest.TestCase. """
    def test_Storage_Instance(self):
        """ Testing if storage is an instance of FileStorage """
        self.assertIsInstance(storage, FileStorage)

    def test_docstring(self):
        """ Testing if docstring are correct """
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_all_method(self):
        """ Testing the all method """
        my_model = FileStorage()
        objects = my_model.all()

        self.assertEqual(type(objects), dict)
        self.assertIsNotNone(objects)
        self.assertIs(objects, my_model._FileStorage__objects)

    def test_new_method(self):
        """ Testing the new method """
        storage = FileStorage()
        objects = storage.all()
        my_model = State()
        my_model.name = 'Holberton'

        storage.new(my_model)
        self.assertEqual(type(objects), dict)
        self.assertIsNotNone(objects)
        self.assertIs(objects, storage._FileStorage__objects)
        key = my_model.__class__.__name__ + '.' + my_model.id
        self.assertIsNotNone(objects[key])

    def test_save_method(self):
        """ Testing if save method is correct """
        my_model = FileStorage()
        my_model.save()
        with open('file.json', encoding='utf-8') as my_file:
            read_lines = my_file.readlines()

        try:
            remove('file.json')
        except:
            pass

        my_model.save()
        with open('file.json', encoding='utf-8') as my_file2:
            read_lines2 = my_file2.readlines()

        self.assertEqual(read_lines, read_lines2)

    def test_save_method_2(self):
        """ Testing if the save method works completely """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.save()

        dict_objs = my_model.to_dict()
        objects = storage.all()

        key = dict_objs['__class__'] + '.' + dict_objs['id']
        self.assertEqual(key in objects, True)
        self.assertEqual(my_model.name, dict_objs['name'])

        temp_create1 = dict_objs['created_at']
        temp_update1 = dict_objs['updated_at']

        my_model.name = "School"
        my_model.save()
        dict_objs = my_model.to_dict()
        objects = storage.all()
        self.assertEqual(key in objects, True)
        self.assertEqual(my_model.name, dict_objs['name'])

        temp_create2 = dict_objs['created_at']
        temp_update2 = dict_objs['updated_at']

        self.assertEqual(temp_create1, temp_create2)
        self.assertNotEqual(temp_update1, temp_update2)

if __name__ == '__main__':
    unittest.main()

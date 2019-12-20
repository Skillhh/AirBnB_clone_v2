#!/usr/bin/python3
""" Importing neccesary modules """
from models.engine.file_storage import FileStorage
from os import environ


if "HBNB_TYPE_STORAGE" in environ and environ["HBNB_TYPE_STORAGE"] == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()

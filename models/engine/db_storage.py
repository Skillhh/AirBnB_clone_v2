#!/usr/bin/python3
""" Engine Class """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.session import Session
from os import environ
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """ Public Instance """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(environ['HBNB_MYSQL_USER'],
                                             environ['HBNB_MYSQL_PWD'],
                                             environ['HBNB_MYSQL_HOST'],
                                             environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)

        if environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """  """

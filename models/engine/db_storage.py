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
    __classes = [User, State, City, Place, Review, Amenity]

    def __init__(self):
        """ Public Instance """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(environ['HBNB_MYSQL_USER'],
                                             environ['HBNB_MYSQL_PWD'],
                                             environ['HBNB_MYSQL_HOST'],
                                             environ['HBNB_MYSQL_DB']),
                                      pool_pre_ping=True)

        if 'HBNB_ENV' in environ and environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ Show all method """
        __objs = {}
        if cls is not None:
            objs = self.__session.query(eval(cls))
            for value in objs:
                key = "{}.{}".format(cls, value.id)
                __objs.update({key: value})
        else:
            for __class in self.__classes:
                objs = self.__session.query(__class)
                for value in objs:
                    key = "{}.{}".format(cls, value.id)
                    __objs.update({key: value})
        return __objs

    def new(self, obj):
        """ Create New method """
        self.__session.add(obj)

    def save(self):
        """ Save """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete  """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Open session """
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine,
                               expire_on_commit=False)
        self.__session = scoped_session(session)()

    def close(self):
        """ Close session """
        Session.close(self.__session)

#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class User(BaseModel, Base):
    """
    Class User
    email(str): mail address
    password (str): password
    first_name (str): first name
    last_name (str): last name

    """
    __tablename__ = 'users'

    if "HBNB_TYPE_STORAGE" in environ and environ["HBNB_TYPE_STORAGE"] == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        place = relationship("Place", cascade="all, delete", backref='user')
        reviews = relationship("Review", cascade="all, delete", backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

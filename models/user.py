#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """
    Class User
    email(str): mail address
    password (str): password
    first_name (str): first name
    last_name (str): last name

    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

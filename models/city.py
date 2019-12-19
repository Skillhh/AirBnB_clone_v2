#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """
    Class City

    Attributes:
        state_id (str): it will be the State.id
        name (str): city name

    """
    __tablename__ = 'cities'
    state_id = Column(String(60), nullable=False)
    name = Column(String(128), nullable=Falsei, ForeignKey('states.id'))

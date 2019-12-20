#!/usr/bin/python3
""" Imports """
import models
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """
    Class State

    name (str): name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if "HBNB_TYPE_STORAGE" in environ and environ["HBNB_TYPE_STORAGE"] == "db":
        cities = relationship('City', backref="state")
    else:
        @property
        def cities(self):
            """ Get cities """
            __cities = []
            for key, value in models.storage.all().itmes():
                if 'City' in key and value.state_id == self.id:
                    __cities.append(value)
            return __cities

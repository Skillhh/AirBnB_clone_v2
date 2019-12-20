#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
    Class City

    Attributes:
        state_id (str): it will be the State.id
        name (str): city name

    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    place = relationship("Place", cascade="all, delete", backref='cities')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

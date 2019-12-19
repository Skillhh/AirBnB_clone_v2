#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """
    Class State

    name (str): name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

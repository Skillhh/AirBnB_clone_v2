#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class City

    Attributes:
        state_id (str): it will be the State.id
        name (str): city name

    """
    state_id = ""
    name = ""

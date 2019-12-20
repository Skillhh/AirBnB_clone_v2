#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String, ForeignKey, Table


class Review(BaseModel, Base):
    """
    Class Review

    place_id (str): it will be the Place.id
    user_id (str): it will be the User.id
    text (str): string

    """
    __tablename__ = 'reviews'

    if "HBNB_TYPE_STORAGE" in environ and environ["HBNB_TYPE_STORAGE"] == "db":
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'))
        user_id = Column(String(60),
                         ForeignKey('users.id'), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

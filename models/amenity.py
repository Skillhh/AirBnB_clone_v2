#!/usr/bin/python3
"""
Imports

"""
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class Amenity(BaseModel, Base):
    """
    Class Amenity

    Attributes:
        name (str): level amiability

    """
    if "HBNB_TYPE_STORAGE" in environ and environ["HBNB_TYPE_STORAGE"] == "db":
        __tablename__ = 'amenities'
        name = Column(String(128),  nullable=False)
        place_amenities = relationship('Place',
                                       secondary=place_amenity)
    else:
        name = ""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

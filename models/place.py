#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """
    Class Place

    city_id (str): it will be the City.id
    user_id (str): it will be the User.id
    name (str): plae name
    description (str): only description
    number_rooms (int): rooms quantity
    number_bathrooms (int): bathrooms quantity
    max_guest (int): number guest
    price_by_night (int): price
    latitude (float): locate number
    longitude (float): locate number
    amenity_ids (str): it will be the list of Amenity.id later

    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

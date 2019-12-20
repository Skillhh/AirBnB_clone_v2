#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Float

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
    __table__ = "places"

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = (Integer, default=0, nullable=False)
    price_by_night = (Integer, default=0, nullable=False)
    latitude = (Float, nullable=False)
    longitude = (Float, nullable=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

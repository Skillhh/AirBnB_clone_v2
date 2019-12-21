#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, Float, Table
from sqlalchemy import ForeignKey, Table
from sqlalchemy.orm import relationship
from os import environ, getenv


envstorage = getenv("HBNB_TYPE_STORAGE")
if envstorage == "db":
    place_amenity = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


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

    if "HBNB_TYPE_STORAGE" in environ and environ["HBNB_TYPE_STORAGE"] == "db":
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
        reviews = relationship(
            "Review", cascade="all, delete", backref="place")
        amenities = relationship('Amenity', secondary='place_amenity',
                                 viewonly=False,
                                 back_populates='place_amenities')

    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_roons = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0
        longitude = 0

        @property
        def reviews(self):
            """Method getter setter for return Cities
            instance of current state_id"""
            reviews = []
            objs = models.storage.all(models.review.Review)
            for val in objs:
                if objs[key].place_id is self.id:
                    cities.append(objs[key])
            return reviews

        @property
        def amenities(self):
            """Method getter setter for return Cities
            instance of current state_id"""
            amenities = []
            objs = models.storage.all(models.amenity.Amenity)
            for val in objs:
                if objs[val].place_id is self.id:
                    amenities.append(objs[val])
            return amenities

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

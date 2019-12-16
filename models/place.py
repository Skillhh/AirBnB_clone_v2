#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel


class Place(BaseModel):
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
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

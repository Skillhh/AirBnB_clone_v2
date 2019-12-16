#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class Review

    place_id (str): it will be the Place.id
    user_id (str): it will be the User.id
    text (str): string

    """
    place_id = ""
    user_id = ""
    text = ""

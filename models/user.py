#!/usr/bin/python3
""" Imports """
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class User

    email(str): mail address
    password (str): password
    first_name (str): first name
    last_name (str): last name

    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

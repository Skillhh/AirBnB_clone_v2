#!/usr/bin/python3
""" Importing necessary modules """
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """ SuperClass from which the rest of the classes will inherit """
    id = Column(String(60), unique=True,
                nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """ Constructor method """
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, key, value)
            if "id" is not kwargs:
                self.id = str(uuid4())
            if 'created_at' is not kwargs:
                self.created_at = datetime.now()
            if 'updated_at' is not kwargs:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """ Returns the string representation of class name, id and dict """
        class_name = str("[" + self.__class__.__name__ + "]")
        instance_id = str("(" + self.id + ")")
        instance_dict = str(self.__dict__)
        return (class_name + " " + instance_id + " " + instance_dict)

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all key/values of instance """
        dict_objs = {}
        tmp_var = self.__dict__

        for key, values in tmp_var.items():
            if key == 'created_at' or key == 'updated_at':
                dict_objs[key] = values.strftime('%Y-%m-%dT%H:%M:%S.%f')
            else:
                if not values:
                    pass
                else:
                    dict_objs[key] = values
        dict_objs['__class__'] = self.__class__.__name__

        return (dict_objs)

    def delete(self):
        """ Method Delet

        Delete the current instance
        """
        models.storage.delete(self)

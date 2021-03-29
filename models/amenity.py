""" This module contains a class Amenity that inherits from BaseModel """

from datetime import datetime
import json
from models.engine import file_storage
from models.base_model import BaseModel
import uuid


class Amenity(BaseModel):
    """ Amenity class
    """

    name = ""

# below is the updated amenity class that ashley started for task 10
# #!/usr/bin/python3
# """ State Module for HBNB project """
# from models.base_model import BaseModel
#
#
# class Amenity(BaseModel, Base):
#    __tablename__= 'amenities'
#    name = Column(String(128), nullable=False)
# """ class attribute place_amenities must represent relationship Many-To-Many
# between the class Place and Amenity."""
#
#    place_amenities =
#

#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), nullable=False,
                             primary_key=True),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), nullable=False,
                             primary_key=True))

class Place(BaseModel, Base):
    """ A place to stay """
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

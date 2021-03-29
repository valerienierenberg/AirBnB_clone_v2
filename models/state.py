#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
#    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """getter for cities (for FileStorage)
        Returns:
        list of City instances with state_id equal to the current State.id
        """
        cities = []
        allcities = models.storageg.all(City)
        for city in allcities.values():  # values() method returns an obj
            # that contains the values of the dictionary as a list.
            if city.state_id == self.id:
                cities.append(city)
        return cities

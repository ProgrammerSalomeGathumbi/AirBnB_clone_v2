#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="states",
                              cascade="all, delete")
        name = Column(String(128), nullable=False)
    else:
        @property
        def cities(self):
            """ return the list of City objects"""
            cities = list()

            for _id, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)

            return cities

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
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="states",
                              cascade="all, delete")
    else:
        @property
        def cities(self):
            """ return the list of City objects"""
            cities = storage.all(City)
            city_list = []
            for city in cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list

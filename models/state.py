#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade="all, delete")

    @property
    def cities(self):
        """ return the list of City objects"""
        cities = models.storage.all(City)
        city_list = []
        for city in cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

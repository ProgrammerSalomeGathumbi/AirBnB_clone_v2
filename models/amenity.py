#!/usr/bin/python3
""" Amenity Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class Amenity(BaseModel, Base):
    """
    Amenities class
    """
    __tablename__ = "amenities"

    if getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        place_amenity = relationship("Place", secondary='place_amenity',
                                     back_populates='place_amenities',
                                     viewonly=False)
    else:
        name = ""

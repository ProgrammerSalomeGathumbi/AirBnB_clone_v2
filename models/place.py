#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Table, Float, Integer
import models
from models.review import Review
from models.amenity import Amenity

place_table = Table('place_amenity', Base.metadata,
                    Column('place_id', String(60),
                           ForeignKey('places.id'),
                           primary_key=True, nullable=False),
                    Column('amenity_id', String(60),
                           ForeignKey('amenities.id'),
                           primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv('HBNB_TYPE_STORAGE') == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(128))
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship('Amenity', secondary="place_amenity",
                                 back_populates='place_amenities',
                                 viewonly=False)
        amenity_ids = []
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0

        @property
        def reviews(self):
            """
            returns reviews
            """
            reviews = models.storage.all(Review).values()
            rev_list = []
            for review in reviews:
                if review.place_id == self.id:
                    rev_list.append(review)
            return rev_list

    @property
    def amenities(self):
        """
        returns all Amenity.id linked to the Place
        """
        a = models.storage.all(Amenity).values()
        a_list = []
        for amenity in a:
            if amenity.id in self.amenity_ids:
                a_list.append(amenity)
        return a_list

    @amenities.setter
    def amenities(self, obj):
        """
        adds an Amenity.id
        """
        if value(obj) == "Amenity":
            self.amenity_ids.append(obj.id)

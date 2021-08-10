#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from models.city import City
from os import getenv
from sqlalchemy.orm import relationship
from models.review import Review
import models
from sqlalchemy import table
from models.user import User


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="all, delete")

    if models.storage_t == "FileStorage":
        @getter
        def reviews(self):
            """ returns the list of Review instances with place_id equals
            to the current Place.id"""
            my_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    my_list.append(review)
            return my_list

#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    city = relationship('City', back_populates="cities")

    @property
    city(self):
        from model.filestorage import storage
        return [city for city in storage.all(City).values()
                if city.state_id == self.id]

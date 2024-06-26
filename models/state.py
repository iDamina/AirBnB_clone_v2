#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        from model.filestorage import storage
        from models.city import City
        return [city for city in storage.all(City).values()
                if city.state_id == self.id]

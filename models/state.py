#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
import models
import shlex

class State(BaseModel, Base):
    """State class."""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Citites prob."""
        al = models.storage.all()
        lis = []
        res = []
        for key in al:
            if (shlex.split(key.replace('.', ' '))[0] == 'City'):
                lis.append(al[key])
        for ele in lis:
            if (ele.state_id == self.id):
                res.append(ele)
        return (res)

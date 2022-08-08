#!/usr/bin/python3
"""
File that contains the class definition of a City
"""
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    # class City is a child of class State
    state = relationship("State", back_populates="cities")

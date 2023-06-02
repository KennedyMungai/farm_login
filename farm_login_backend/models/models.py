"""The file that holds all the models for the app"""
from database.db import Base
from enum import Enum
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from datetime import datetime


class Sex(str, Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Person(Base):
    """The person model

    Args:
        Base (Declarative Base): The base for the model data
    """
    __tablename__ = "persons"
    
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String(255))
    birth = Column(Date)
    sex = Column(Sex)
    profile = Column(String(255))
    phone_number = Column(String(12))
    created_at = Column(datetime(), default=datetime.now())
    updated_at = Column(datetime(), onupdate=datetime.now())
    
    users = relationship("User", back_populates="person", cascade="all, delete")
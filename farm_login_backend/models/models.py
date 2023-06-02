"""The file that holds all the models for the app"""
from datetime import datetime
from enum import Enum

from database.db import Base
from sqlalchemy import Column, Date, Integer, String, ForeignKey


class Sex(str, Enum):
    """The gender enum

    Args:
        str (_type_): String
        Enum (_type_): Enum
    """
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


class Users(Base):
    """The Users model

    Args:
        Base (Declarative Base): The base for all the models
    """
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True, nullable=False)
    username = Column(String(255), unique=True)
    email = Column(String(255), unique=True)
    password = Column(String(255))
    created_at = Column(datetime(), default=datetime.now())
    updated_at = Column(datetime(), onupdate=datetime.now())

    person_id = Column(String, ForeignKey("persons.id", ondelete="CASCADE"), nullable=False)

#!/usr/bin/python3
"""python file that contains the class definition of a State and an instance"""

import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declative_base

Base = declarative_base()


class State(Base):
    """state representation"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

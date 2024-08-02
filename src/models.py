import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    id = Column(Integer, primary_key=True)
    userName = Column(String(32), nullable = False)
    password = Column(String(32), nullable = False)

class Character(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable = False)
    weapon = Column(String(32), nullable = False)

class Planet(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable = False)
    gravity = Column(String(32), nullable = False)
    climate = Column(String(32), nullable = False)

class Vehicles(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable = False)
    weapon = Column(String(32), nullable = False)
    faction = Column(String(32), nullable = False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')



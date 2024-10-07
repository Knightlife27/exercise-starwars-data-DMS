import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
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

favorite_characters = Table(
    "favorite_characters",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("character_id", ForeignKey("character.id")),
)

favorite_planets = Table(
    "favorite_planets",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("planet_id", ForeignKey("planet.id")),
)

favorite_vehicles = Table(
    "favorite_vehicles",
    Base.metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("vehicle_id", ForeignKey("vehicle.id")),
)

class User(Base):
    __tablename__= "user"
    id = Column(Integer, primary_key=True)
    userName = Column(String(32), nullable = False)
    password = Column(String(32), nullable = False)
    favorite_characters = relationship("Character", secondary=favorite_characters)
    favorite_planets = relationship("Planet", secondary=favorite_planets)
    favorite_vehicles = relationship("Vehicle", secondary=favorite_vehicles)

class Character(Base):
    __tablename__= "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable = False)
    weapon = Column(String(32), nullable = False)

class Planet(Base):
    __tablename__= "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable = False)
    gravity = Column(String(32), nullable = False)
    climate = Column(String(32), nullable = False)

class Vehicle(Base):
    __tablename__= "vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable = False)
    weapon = Column(String(32), nullable = False)
    faction = Column(String(32), nullable = False)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')



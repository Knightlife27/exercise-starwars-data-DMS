import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine, Table
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

# favorites = Table("favorites", Column("character_id", Integer, ForeignKey('character.id'), nullable=True),
#     Column("planets_id", Integer, ForeignKey('planets.id'), nullable=True),
#     Column("vehicles_id", Integer, ForeignKey('vehicles.id'), nullable=True),
#     Column("ships_id", Integer, ForeignKey('ships.id'), nullable=True),
#     Column("user_id", Integer, ForeignKey('user.id'), primary_key=True))

class Favorites(Base):
    __tablename__ = "favorites"
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    vehicles_id = Column(Integer, ForeignKey('vehicles.id'), nullable=True)
    ships_id = Column(Integer, ForeignKey('ships.id'), nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    userName = Column(String(32), nullable = False)
    password = Column(String(32), nullable = False)
    favorites = relationship(Favorites)

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable = False)
    weapon = Column(String(32), nullable = False)
    favorites = relationship(Favorites)

class Planet(Base):
    __tablename__ = "planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable = False)
    gravity = Column(String(32), nullable = False)
    climate = Column(String(32), nullable = False)
    favorites = relationship(Favorites)

class Vehicles(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable = False)
    weapon = Column(String(32), nullable = False)
    faction = Column(String(32), nullable = False)
    favorites = relationship(Favorites)

class Ships(Base):
    __tablename__ = "ships"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable = False)
    weapon = Column(String(32), nullable = False)
    faction = Column(String(32), nullable = False)
    favorites = relationship(Favorites)




# ## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')



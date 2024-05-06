import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    date = Column(Integer)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Caracter(Base):
    __tablename__ = 'caracter'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'caracter_fav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    caracter_name = Column(String, ForeignKey('caracter.name'))
    caracter = relationship(Caracter)
    user_name = Column(String, ForeignKey('user.name'))
    def to_dict(self):
        return {}

class Address(Base):
    __tablename__ = 'vehicles_fav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String, ForeignKey('vehicle.name'))
    vehicle = relationship(Vehicle)
    user_name = Column(String, ForeignKey('user.name'))
    def to_dict(self):
        return {}

class Address(Base):
    __tablename__ = 'planetas_fav'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String, ForeignKey('planet.name'))
    planet = relationship(Planet)
    user_name = Column(String, ForeignKey('user.name'))
    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

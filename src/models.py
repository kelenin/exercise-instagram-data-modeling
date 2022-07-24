import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Numeric, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Pais(Base):
    __tablename__ = 'country'
    # Here we define columns for the table country
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Estado(Base):
    __tablename__ = 'state'
    # Here we define columns for the table state
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Ciudad(Base):
    __tablename__ = 'city'
    # Here we define columns for the table city
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    usuario = Column(String(15), nullable=False)
    password = Column(String(100), nullable=False , unique=True)
    email = Column(String(100),nullable=False , unique=True)
    fecha = Column(Date, nullable=False , unique=True)

class Noticias(Base):
    __tablename__ = 'noticias'
    # Here we define columns for the table noticias
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    fecha = Column(Date, nullable=False , unique=True)

class Ubicacions(Base):
    __tablename__ = 'ubicacion'
    # Here we define columns for the table ubicancion
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    pais_id = Column(Integer, ForeignKey('country.id'))
    pais = relationship(Pais)
    estado_id = Column(Integer, ForeignKey('state.id'))
    estado = relationship(Estado)
    ciudad_id = Column(Integer, ForeignKey('city.id'))
    ciudad = relationship(Ciudad)
    noticias_id = Column(Integer, ForeignKey('noticias.id'))
    noticias = relationship(Noticias)

class Seguidor(Base):
    __tablename__ = 'seguidor'
    # Here we define columns for the table seguidor
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    person_from = Column(Integer, ForeignKey('person.id'))
    person_to = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

class Comentarios(Base):
    __tablename__ = 'comentarios'
    # Here we define columns for the table comentarios
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=True)
    person_from = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    noticias_from = Column(Integer, ForeignKey('noticias.id'))
    noticias = relationship(Noticias)
    name_modif = Column(String(250), nullable=True)
    fecha = Column(Date, nullable=False )
    fecha_editado = Column(Date, nullable=True)
    fecha_eliminado = Column(Date, nullable=True)

class Estadisticas(Base):
    __tablename__ = 'estadisticas'
    # Here we define columns for the table estadisticas
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name_like = Column(Numeric, nullable=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    noticias_id = Column(Integer, ForeignKey('noticias.id'))
    noticias = relationship(Noticias)
    seguidor_id = Column(Integer, ForeignKey('seguidor.id'))
    seguidor = relationship(Seguidor)
    fecha = Column(Date, nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
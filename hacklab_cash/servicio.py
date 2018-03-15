from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from base import Base


class Servicio(Base):
    __tablename__ = 'servicios'
    id = Column(Integer,primary_key=True)
    nombre = Column('nombre',String(32))
    descripcion = Column('descripcion',String(64))

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

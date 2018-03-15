from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Date
from sqlalchemy.orm import relationship
from base import Base

class Donacion(Base):
    __tablename__ = 'donaciones'
    id = Column(Integer,primary_key=True)
    bono=Column('bono', Boolean)
    descripcion = Column('descripcion',String(64))
    monto=Column('monto',Integer)
    fecha=Column('fecha',Date)


    def __init__(self, bono, descripcion, monto, fecha):
        self.bono=bono
        self.descripcion = descripcion
        self.monto = monto
        self.fecha = fecha

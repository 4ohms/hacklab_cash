from sqlalchemy import Column, String, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from base import Base

class Pago(Base):
    __tablename__ = 'pagos'
    id = Column(Integer,primary_key=True)
    deuda_id =Column(Integer, ForeignKey('deudas.id'))
    deuda = relationship("Deuda",back_populates="pagos")
    fecha = Column('fecha', Date)

    def __init__(self, deuda, fecha):
        self.deuda = deuda
        self.fecha = fecha

from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from base import Base

class Deuda(Base):
    __tablename__='deudas'
    id = Column(Integer,primary_key=True)
    servicio_id = Column(Integer, ForeignKey('servicios.id'))
    servicio = relationship("Servicio")
    fecha_vencimiento = Column('fecha_vencimiento', Date)
    monto = Column('monto', Integer)
    descripcion=Column("descripcion", String(32))
    pago= relationship("Pago", uselist=False, back_populates="Deuda")

    def __init__(self, servicio, fecha_vencimiento, monto, descripcion):
        self.servicio = servicio
        self.fecha_vencimiento = fecha_vencimiento
        self.monto = monto
        self.descripcion = descripcion

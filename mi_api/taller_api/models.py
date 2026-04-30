from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    matricula = Column(String, unique=True, index=True)
    marca = Column(String)
    modelo = Column(String)
    descripcion = Column(String, nullable=True)
    precio = Column(Float)
    completado = Column(Boolean, default=False)

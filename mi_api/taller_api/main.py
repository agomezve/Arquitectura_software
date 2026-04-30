from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Vehiculo
from database import engine, Base
from dependencies import get_db
from pydantic import BaseModel

app = FastAPI(title="Taller de Coches API")

# Schemas
class VehiculoCreate(BaseModel):
    matricula: str
    marca: str
    modelo: str
    descripcion: str | None = None
    precio: float
    completado: bool = False

class VehiculoResponse(VehiculoCreate):
    id: int

    class Config:
        from_attributes = True

@app.post("/vehiculos/", response_model=VehiculoResponse)
async def create_vehiculo(vehiculo: VehiculoCreate, db: AsyncSession = Depends(get_db)):
    db_vehiculo = Vehiculo(**vehiculo.model_dump())
    db.add(db_vehiculo)
    try:
        await db.commit()
        await db.refresh(db_vehiculo)
        return db_vehiculo
    except Exception as e:
        await db.rollback()
        raise HTTPException(status_code=400, detail="Error al crear el vehículo (la matrícula ya existe)")

@app.get("/vehiculos/", response_model=list[VehiculoResponse])
async def list_vehiculos(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Vehiculo))
    return result.scalars().all()

@app.get("/vehiculos/{vehiculo_id}", response_model=VehiculoResponse)
async def read_vehiculo(vehiculo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Vehiculo).where(Vehiculo.id == vehiculo_id))
    vehiculo = result.scalar_one_or_none()
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo

@app.put("/vehiculos/{vehiculo_id}", response_model=VehiculoResponse)
async def update_vehiculo(vehiculo_id: int, vehiculo: VehiculoCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Vehiculo).where(Vehiculo.id == vehiculo_id))
    db_vehiculo = result.scalar_one_or_none()
    if not db_vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    
    for key, value in vehiculo.model_dump().items():
        setattr(db_vehiculo, key, value)
    
    await db.commit()
    await db.refresh(db_vehiculo)
    return db_vehiculo

@app.delete("/vehiculos/{vehiculo_id}")
async def delete_vehiculo(vehiculo_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Vehiculo).where(Vehiculo.id == vehiculo_id))
    vehiculo = result.scalar_one_or_none()
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    
    await db.delete(vehiculo)
    await db.commit()
    return {"mensaje": "Vehículo eliminado"}
